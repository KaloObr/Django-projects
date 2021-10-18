from django.shortcuts import render
from django.views import generic
from catalog.models import Book, BookInstance, Author


def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/books_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'authors/authors_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_details.html'

