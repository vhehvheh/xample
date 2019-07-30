from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.newBoard, name='newBoard'),
    path('list/', views.listBoard, name='listBoard'),
    path('view/<int:id>/', views.viewBoard, name='viewBoard'),
    path('updateDelete/<int:id>', views.updateDelete, name='updateDelete'),
    path('updatepage/<int:id>',views.updatepage, name='updatepage'),
    path('comment/<int:id>',views.comment, name="comment"),
    path('write.<int:id>',views.write,name='write')
]
