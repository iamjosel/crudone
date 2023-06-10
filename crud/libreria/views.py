from django.shortcuts import render
from django.http import HttpResponse

#Sección de acceso al sitio
def inicio(request):
    return render(request, 'pages/inicio.html')
    
def about(request):
    return render(request, 'pages/about.html')

#Sección de libros
def books(request):
    return render(request, 'books/index.html')

def create_book(request):
    return render(request, 'books/create.html')

def edit_book(request):
    return render(request, 'books/edit.html')