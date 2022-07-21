from rest_framework import serializers
from library_api.models import Book, BookTracker
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ['id', 'title', 'publication_date', 'genre', 'featured', 'author']


class UserSerializer(serializers.ModelSerializer):
	book_tracker = serializers.PrimaryKeyRelatedField(many=True, queryset=BookTracker.objects.all())

	class Meta:
		model = User
		fields = ['id', 'username', 'book_tracker']


class BookTrackerSerializer(serializers.ModelSerializer):
	user = serializers.ReadOnlyField(source='user.username')
	def get_book_status(self, obj):
		return obj.get_status_display()

	book_status = serializers.SerializerMethodField(read_only=True, source='get_book_status')
	book_details = BookSerializer(source='book', read_only=True)

	class Meta:
		model = BookTracker
		fields = "__all__"
		# fields = ['id', 'book_status', 'book', 'user', 'book_details']

