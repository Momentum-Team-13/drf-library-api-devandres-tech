from rest_framework import generics, permissions
from library_api.serializers import BookSerializer
from library_api.models import Book


# Create your views here.
class BookList(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
