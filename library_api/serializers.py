from rest_framework import serializers
from library_api.models import Book
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ['id', 'title', 'publication_date', 'genre', 'featured', 'author']