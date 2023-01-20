from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
   path('board/', views.board_create, name='views.board_create'),
   path('', views.board_index, name='board_index'),
   path('<int:article_pk>/', views.board_detail, name = 'board_detail'),
   path('<int:article_pk>/delete/', views.board_delete, name = 'board_delete'),
   path('<int:board_delete_pk>/delete/', views.board_delete, name = 'board_delete'),    
]
