from django.shortcuts import render, redirect,HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.

# list all the books
def book_list(request):
    # return HttpResponse("Book list")
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books':books})

# Add a new books
def book_create(request):
    # return HttpResponse("Create book")
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html',{'form':form})

# update a book
def book_update(request, pk):
    # return HttpResponse("update book")
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html',{'form':form})

# delete a book
def book_delete(request, pk):
    # return HttpResponse("delete book")
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html',{'book':book})