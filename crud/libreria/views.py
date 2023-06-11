from django.shortcuts import render
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
    form = BookForm(request.POST or None)
    return render(request, 'books/create.html', {'form': form})

def edit_book(request):
    return render(request, 'books/edit.html')