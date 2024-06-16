from . import views
from django.urls import path

urlpatterns = [
    path('post-list/', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('newpost/', views.new_post, name='new_post'),
    path('<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    
]