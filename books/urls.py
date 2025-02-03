from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('',views.book_list, name = 'book_list'),
    path('new/',views.book_create, name = 'book_create'),
    path('edit/<int:pk>/',views.book_update, name = 'book_update'),
    path('delete/<int:pk>/',views.book_delete, name = 'book_delete'),
]