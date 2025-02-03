from django.shortcuts import render, redirect,HttpResponse
from .models import Book

# Create your views here.

def book_list(request):
    return HttpResponse("Book list")
def book_create(request):
    return HttpResponse("Create book")
def book_update(request, pk):
    return HttpResponse("update book")
def book_delete(request, pk):
    return HttpResponse("delete book")