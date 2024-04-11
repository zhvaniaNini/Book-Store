from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from market.models import Book
from market.serializer import BookSerializer

# Create your views here.
def listed_books(request):
    books = Book.objects.values_list('id', 'name', 'author_name', 'price')
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

def book_information(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'market/book_detail.html', {'book': book})
    
def list_books(request):
    books = Book.objects.all()
    return render(request, 'market/list_books.html', {'books': books})



    