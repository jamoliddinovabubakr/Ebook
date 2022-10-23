from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('addauthor/', add_author, name='add_author'),
    path('addbook/', add_book, name='add_book')
]
