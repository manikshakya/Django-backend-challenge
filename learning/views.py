from django.shortcuts import render

from .models import (Book, Vocabulary)

# Create your views here.


def index(request):
    return render(request, "learning/index.html")


def addBook(request):

    books = None
    errorMessage = None

    if request.method == 'POST':
        name = request.POST['bookName']
        ISBN = request.POST['ISBN']
        author = request.POST['author']

        '''
            Check if the none of the fields are empty
        '''
        if name != '' and ISBN != '' and author != '':
            '''
                Check if the book is in the database
            '''
            try:
                exist = Book.objects.get(ISBN=ISBN)
                errorMessage = 'The Book is already in the database.'
            except:
                '''
                    If the Book doesn't Exists.
                '''
                try:
                    data = Book(title=str(name).lower(), ISBN=ISBN, author=str(author).lower())
                    data.save()
                    books = {
                        'name': name,
                        'ISBN': ISBN,
                        'author': author,

                    }
                    errorMessage = True
                except AssertionError:
                    errorMessage = 'The Book is already in the database.'
        else:
            errorMessage = 'Please fill all the details'

    return render(request, "learning/add_book.html", {'books': books, 'errorMessage': errorMessage})


def searchBook(request):
    return render(request, "learning/search_book.html")


def addVocabulary(request):
    books = None
    errorMessage = None

    if request.method == 'POST':
        name = request.POST['bookName']
        word = request.POST['word']
        description = request.POST['description']

        if name != '' and word != '' and description != '':
            '''
                Check if the book exist in the database to add the vocabulary.
            '''
            try:
                bookExist = Book.objects.get(title=str(name).lower())
                try:
                    wordExist = Vocabulary.objects.get(words=str(word).lower())
                    print(wordExist.ISBN)
                    print('Hello')
                    print(bookExist)

                    print(type(wordExist.ISBN.ISBN))
                    print(type(bookExist.ISBN))
                    if wordExist.ISBN.ISBN != bookExist.ISBN:
                        raise Exception
                    errorMessage = 'Word is already in the Vocabulary.'
                except:
                    try:
                        data = Vocabulary(ISBN=bookExist, words=str(word).lower(), description=str(description).lower())
                        data.save()
                        books = {
                            'name': name,
                            'word': word,
                            'description': description,

                        }
                        errorMessage = True
                    except AssertionError:
                        errorMessage = 'The Book is already in the database.'
            except:
                errorMessage = 'The Book is not available in the database.'
        else:
            errorMessage = 'Please fill all the details'

    return render(request, "learning/add_vocabulary.html", {'books': books, 'errorMessage': errorMessage})

def searchVocabulary(request):
    return render(request, "learning/search_vocabulary.html")
