from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Using class based views
# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = Post.objects.get(id = pk)
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args = [str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' ').title())
    if(category_posts):
        return render(request, 'categories.html', {'cats': cats.replace('-', ' ').title(), 'category_posts': category_posts})
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'category_posts': category_posts})
 

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data( *args, **kwargs)

        obj = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = obj.total_likes()

        liked = False
        if obj.likes.filter(id = self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
 

class AddArticleView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_article.html'
    #fields = '__all__'

    
    

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('article-detail', kwargs={"pk": self.kwargs['pk']})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdateArticleView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_article.html'
    # fields = ['title', 'title_tag', 'body']

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')