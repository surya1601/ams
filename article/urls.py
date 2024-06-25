from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddArticleView, UpdateArticleView, DeleteArticleView, AddCategoryView, CategoryView, LikeView, AddCommentView

urlpatterns = [
    #path('', views.home, name = "home"),
    path('', HomeView.as_view(),  name = 'home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add-article/', AddArticleView.as_view(), name = 'add-article'),
    path('add-category/', AddCategoryView.as_view(), name = 'add-category'),   
    path('article/edit/<int:pk>', UpdateArticleView.as_view(), name = 'edit-article'),
    path('article/delete/<int:pk>', DeleteArticleView.as_view(), name = 'delete-article'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('like/<int:pk>', LikeView, name = 'like-article'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'add-comment'),

]