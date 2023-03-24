from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Subscription, Profile
from .forms import CommentForm, FormUser, ProfileForm, SubcribersForm, BioForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 6


# def post_list(request):
#     post_list = Post.objects.filter(status=1).order_by('-created_on')
#     paginator = Paginator(post_list, 6)
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)
#     context = {
#         'posts': posts
#     }
#     return render(request, 'post.html', context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "single_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            })

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "single_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            })


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('single_post', args=[slug]))


def register(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Your profile has been created')
            return redirect('index')
    else:
        form = FormUser()

    return render(request, 'account/signup-copy.html', {'form': form})


@login_required
def profile(request, user_id):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=user)
    if request.method == 'POST':
        if 'update' in request.POST:
            profile_form = ProfileForm(request.POST, instance=user)
            bio_form = BioForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid() and bio_form.is_valid():
                profile_form.save()
                profile = bio_form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, 'Account updated successfully.')
                return redirect('profile', user_id=user_id)
        elif 'delete' in request.POST:
            user.delete()
            logout(request)
            messages.success(request, 'Account deleted successfully.')
            return redirect('index')
    else:
        profile_form = ProfileForm(instance=user)
        bio_form = BioForm(instance=profile)

    context = {
        'profile_form': profile_form,
        'bio_form': bio_form
    }
    return render(request, 'profile.html', context)

    # user = request.user
    # if request.method == 'POST':
    #     if 'update' in request.POST:
    #         form = ProfileForm(request.POST, instance=user)
    #         bio_form = BioForm(request.POST, instance=user)
    #         if form.is_valid() or bio_form.is_valid():
    #             form.save()
    #             bio_form.save()
    #             messages.success(request, 'Profile updated successfully.')
    #             return redirect('profile', user_id=user_id)
    #     elif 'delete' in request.POST:
    #         user.delete()
    #         logout(request)
    #         messages.success(request, 'Account deleted successfully.')
    #         return redirect('index')
    # else:
    #     form = ProfileForm(instance=user)
    #     bio_form = BioForm()
    # return render(request, 'profile.html', {'form': form, 'bio_form': bio_form, })


# def update_bio(request):
#     user = request.user
#     if request.method == 'POST':
#         if 'update' in request.POST:
#             bio_form = BioForm(request.POST, instance=user)
#             if bio_form.is_valid():
#                 bio_form.save()
#                 messages.success(request, 'Bio updated successfully.')
#                 return redirect('profile', user_id=user.id)
#     else:
#         bio_form = BioForm()

#     context = {'bio_form': bio_form}
#     return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)


def subscribe(request):
    if request.method == 'POST':
        form = SubcribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You subscribed to our newsletter!')
            email = request.POST.get('email')
            subject = 'Take a hike subscription'
            message = 'Thank you for subscribing to our newsletter, you will get updates for our future adventures! Go back https://blog-hike.herokuapp.com/'
            from_email = 'tmarkec@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('/')
    else:
        form = SubcribersForm()

    context = {'form': form}
    return render(request, 'index.html', context)
