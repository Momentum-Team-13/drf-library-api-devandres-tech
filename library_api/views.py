from rest_framework import generics, permissions
from library_api.serializers import BookSerializer
from library_api.models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# auth users can get and create books
# GET, POST api/books/
# get all featured books
# GET, api/books?featured=True
class BookListCreate(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter]
	filterset_fields = ['featured']
	search_fields = ['author', 'title']


# auth users can see book details
# GET api/books/<int:pk>
class BookDetails(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]


# only admin users can update books
# PUT api/books/<int:pk>
class BookUpdate(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAdminUser]


# only admin users can destroy books
# DELETE api/books/<int:pk>
class BookDestroy(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAdminUser]
