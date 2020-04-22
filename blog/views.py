from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from blog.models import Post


def home(request):
    posts = Post.objects.all().order_by('date_posted')
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context=context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #app/model_viewtype
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #app/model_viewtype
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')




class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']


    #telling that the author of the post is the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']


    #telling that the author of the post is the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # only the author of the post can update the post not anyone
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    #telling that the author of the post is the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # only the author of the post can update the post not anyone
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

