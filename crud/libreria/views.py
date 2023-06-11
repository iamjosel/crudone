from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

#Sección de acceso al sitio
def inicio(request):
    return render(request, 'pages/inicio.html')
    
def about(request):
    return render(request, 'pages/about.html')

#Sección de libros
def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create_book(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/create.html', {'form': form})

def edit_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('books')
    return render(request, 'books/edit.html', {'form': form})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')