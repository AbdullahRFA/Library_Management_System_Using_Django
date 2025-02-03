from django.shortcuts import render, redirect,HttpResponse
from .models import Book

# Create your views here.

def book_list(request):
    # return HttpResponse("Book list")
    return render(request, 'books/book_list.html')
def book_create(request):
    # return HttpResponse("Create book")
    return render(request, 'books/book_form.html')
def book_update(request, pk):
    # return HttpResponse("update book")
    return render(request, 'books/book_form.html')
def book_delete(request, pk):
    # return HttpResponse("delete book")
    return render(request, 'books/book_confirm_delete.html')