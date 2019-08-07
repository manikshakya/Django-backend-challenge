from django.db import models

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return 'ISBN: ' + str(self.ISBN) + '\nTitle: ' + str(self.title) + '\nAuthor: ' + str(self.author) + '\n'

class Vocabulary(models.Model):
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    words = models.CharField(primary_key=True, max_length=70)
    description = models.CharField(max_length=200)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return 'ISBN: ' + str(self.ISBN.ISBN) + '\nWords: ' + str(self.words) + '\nDescription: ' \
               + str(self.description) + '\nDate Added: ' + str(self.date_added) + '\n'
