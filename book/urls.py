from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addauthor/', add_author, name='add_author'),
    path('addbook/', add_book, name='add_book'),
    path('allauthors/', all_authors, name='all_authors'),
    path('allbooks/', all_books, name='all_books')
]
