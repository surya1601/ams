from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit-profile/', UserEditView.as_view(), name = 'edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name = 'change-password'),
    path('password/', PasswordsChangeView.as_view(), name = 'change-password'),
    path('password-success/', views.password_success, name = 'password-changed'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name = 'edit_profile_page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name = 'create_profile_page'),

]