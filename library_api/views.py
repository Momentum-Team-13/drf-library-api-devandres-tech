from rest_framework import generics, permissions
from library_api.serializers import BookSerializer, BookTrackerSerializer, UserSerializer
from library_api.models import Book, BookTracker
from library_api.filters import IsOwnerFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.models import User


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
	queryset = BookTracker.objects.all()
	serializer_class = BookTrackerSerializer
	permission_classes = [permissions.IsAuthenticated]
	filter_backends = [IsOwnerFilterBackend]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class BookTrackerUpdate(generics.UpdateAPIView):
	queryset = BookTracker.objects.all()
	serializer_class = BookTrackerSerializer
	permission_classes = [permissions.IsAuthenticated]
