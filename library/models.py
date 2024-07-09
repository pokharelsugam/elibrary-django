from django.db import models
import os # Used for operating system-dependent functionality

# Create your models here.


class BookAuthor(models.Model): # "BookAuthor" database table
    name = models.CharField(max_length=64)  # "name" field of database table that store string of maximum length 64

class BookCategory(models.Model):
    name = models.CharField(max_length=32)

class BookPublisher(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

class BookLanguage(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.ManyToManyField(BookAuthor) # "author" field which have Many-to-many relationship with the BookAuthor table, allowing a book to have multiple authors.
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null= True) # One to Many "ForeginKey Relationship"
    edition = models.CharField(max_length=32)
    publisher = models.ForeignKey(BookPublisher,on_delete=models.SET_NULL, null= True)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    language = models.ForeignKey(BookLanguage, on_delete=models.SET_NULL, null= True)
    pages = models.IntegerField()
    description = models.TextField()
    book_file = models.FileField(upload_to='books/')

    def delete(self, *args, **kwargs): # "delete" method to remove associated file from book file directory
        if self.book_file: # Retrieves the path of the file.
            if os.path.isfile(self.book_file.path): # Checks if the file exists
                os.remove(self.book_file.path) # Removes the file from the filesystem.
        super().delete(*args, **kwargs) #calls the delete method to perform the deletion of the Book object from the database.
