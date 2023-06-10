from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('about', views.about, name='about'),
    path('books', views.books, name='books'),
    path('books/create', views.create_book, name='create_book'),
]