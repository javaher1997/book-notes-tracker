from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def book_list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book':book}
    return render(request, 'book_detail.html', context)

def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        Book.objects.create(
            title=title,
            author=author,
            description=description,
        )
        return redirect('book_list')
    
    return render(request, 'book_create.html')


