from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddBookForm, AddAuthorForm
from .models import Book, Author

# Create your views here.

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'All Books', 'url_name': 'all_books'},
    {'title': 'All Authors', 'url_name': 'all_authors'},
    {'title': 'Add book', 'url_name': 'add_book'}
]


def home(request):
    books = Book.objects.all()

    context = {
        'books': books,
        'menu': menu
    }
    return render(request, 'book/home.html', context=context)


def about(request):
    return HttpResponse('About page')


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = AddAuthorForm()

    return render(request, 'book/addauthor.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm()
    context = {
        'menu': menu,
        'title': 'Add book',
        'form': form
    }
    return render(request, 'book/addbook.html', context=context)


def all_authors(request):
    authors = Author.objects.all()
    context = {
        'title': 'All Authors',
        'menu': menu,
        'authors': authors
    }
    return render(request, 'book/allauthors.html', context=context)


def all_books(request):
    books = Book.objects.all()
    context = {
        'title': 'All Books',
        'menu': menu,
        'books': books
    }
    return render(request, 'book/allbooks.html', context=context)
