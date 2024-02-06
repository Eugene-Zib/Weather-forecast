"""This is test task."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('accounts/login/', views.sign_in, name='sign_in'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('user/<int:user_id>/item delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('user/new/', views.sign_up, name='sign_up'),
    path('user/<int:user_id>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('accounts/logout/', views.log_out, name='log_out'),
]

handler404 = 'testapp.views.not_found'
