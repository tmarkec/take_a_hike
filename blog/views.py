from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm, FormUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, SubcribersForm
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Subscription

# Create your views here.
# def index(request):
#     return render(request, 'index.html')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 8


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = True
        # if post.likes.filter(id=self.request.user.id).exist():
        #     liked = True

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
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = True
        # if post.likes.filter(id=self.request.user.id).exist():
        #     liked = True

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


def register(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been created')
            return redirect('post')
    else:
        form = FormUser()

    return render(request, 'account/signup-copy.html', {'form': form})


@login_required
def profile(request, user_id):
    user = request.user
    if request.method == 'POST':
        # If the user clicked on the "Update" button
        if 'update' in request.POST:
            form = ProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile', user_id=user_id)
        # If the user clicked on the "Delete" button
        elif 'delete' in request.POST:
            user.delete()
            logout(request)
            messages.success(request, 'Account deleted successfully.')
            return redirect('index')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form})


def logout_view(request):
    logout(request)


def subscribe(request):
    if request.method == 'POST':
        form = SubcribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SubcribersForm()
        # return redirect('/')

    context = {'form': form}
    return render(request, 'index.html', context)
    # if request.method == 'POST':
    #     email = request.POST.get('email', None)
    #     if not email:
    #         messages.error(request,
    #  'You must type legit email address to subscribe')
    #     try:
    #         validate_email(email)
    #     except ValidationError as e:
    #         messages.error(request, e.messages[0])
    #         return redirect("/")
    #     subscribe_model_instance = Subscription()
    #     subscribe_model_instance.save()
    #     # messages.success(request,
    #  f'{email} email was successfully subscribed to our newsletter!')
    #     return redirect(request.META.get("HTTP_REFERER", "/"))
    
