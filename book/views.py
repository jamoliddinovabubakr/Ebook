from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddBookForm
from .models import Book, Author

# Create your views here.

menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add author', 'url_name': 'add_author'},
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
    return HttpResponse('Add author')


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
