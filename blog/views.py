from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post
from .forms import CommentForm, FormUser


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
            return redirect('post')
    else:
        form = FormUser()

    return render(request, 'account/signup-copy.html', {'form': form})