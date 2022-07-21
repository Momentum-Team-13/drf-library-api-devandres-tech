from rest_framework import generics, permissions
from library_api.serializers import BookSerializer, BookTrackerSerializer, UserSerializer
from library_api.models import Book, BookTracker
from library_api.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User
from library_api.permissions import IsOwner


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


# gets all users in db
class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


# lets any auth user create a book tracker and only users can see
# their own book trackers
# GET, POST api/book-trackers/
class BookTrackerListCreate(generics.ListCreateAPIView):
	# Album.objects.prefetch_related('tracks')
	queryset = BookTracker.objects.prefetch_related('book')
	serializer_class = BookTrackerSerializer
	permission_classes = [permissions.IsAuthenticated]
	filter_backends = [DjangoFilterBackend, IsOwnerFilterBackend]
	filterset_fields = ["status"]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


# only let object owners get, update and destroy a single instance
# GET, PUT, DELETE api/book-trackers/<int:pk>
class BookTrackerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = BookTracker.objects.all()
	serializer_class = BookTrackerSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwner]
	filter_backends = [IsOwnerFilterBackend]
