from rest_framework import generics, permissions
from library_api.serializers import BookSerializer
from library_api.models import Book


# auth users can get and create books
# GET, POST api/books/
class BookListCreate(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# only admin users can update and delete books
# GET, PUT, DELETE api/books/<int:pk>
class BookUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAdminUser]
