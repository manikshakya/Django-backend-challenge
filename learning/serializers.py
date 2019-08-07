from rest_framework import serializers
from .models import Book, Vocabulary


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class VocabularySerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='ISBN.title')
    class Meta:
        model = Vocabulary
        fields = ['book', 'ISBN', 'words', 'description', 'date_added']
        # fields = "__all__"