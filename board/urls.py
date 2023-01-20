from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
   path('create/', views.board_create, name='board_create'),
   path('', views.board_index, name='board_index'),   
   path('<int:board_edit_pk>/edit/', views.board_edit, name = 'board_edit'),
   path('<int:board_delete_pk>/delete/', views.board_delete, name = 'board_delete'),    
]
