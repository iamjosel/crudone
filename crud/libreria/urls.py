from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('about', views.about, name='about'),
    path('books', views.books, name='books'),
    path('books/create', views.create_book, name='create_book'),
    path('books/edit', views.edit_book, name='edit_book'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)