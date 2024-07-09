from django.shortcuts import render, get_object_or_404, redirect
from .models import BookAuthor, BookCategory,BookPublisher, BookLanguage, Book
from django.http import HttpResponse
from django.db.models import Q #This class is used to construct complex queries using OR, AND, and NOT operations

# Create your views here.


###########################################################################################

#Home View
def home(request): # User defined home function for "home" url to with "request" parameter used to sent http request to server by client
    book_objs = Book.objects.all().order_by('-id')[:2] #Retrive all records from Book model(Book database table) where it sorts in descending order and selects 2 books
    data = {'new_books': book_objs} #data Dictionary key=new_books, value= books_objs
    return render(request,'index.html', context=data) #Pass data dictionary to "index.html" template according to request


###########################################################################################

# BookAuthor Views CRUD
#Read
def author_list(request): # User defined author_list function for "author_list" url
    author_objs = BookAuthor.objects.all()  #Retrive all records from BookAuthor model(BookAuthor database table)
    data = {'authors': author_objs}
    return render(request,'author.html',context=data) #Pass data dictionary to author.html template according to request for diaplay

#Create
def author_add(request):
    if request.method == 'POST': # Checking request is "POST" or not means form is submitted or not
        name = request.POST.get('name') # Retribe (get) data from field with "name" attribut from request sent form(author-add.html)

        if BookAuthor.objects.filter(name=name).exists(): #Checks if there is already an author with the given name in the BookAuthor model.
            error_message = f"Author with name '{name}' already exists." #If an author with the same name already exists, an error message is generated.
            return render(request, 'author-add.html', {'error_message': error_message}) #The render function then re-renders the author-add.html template, passing the error message to the template for display.

        BookAuthor.objects.create(name=name) # Creates a new author record with the given name in the BookAuthor model.
        return HttpResponse('Author Added') # Display Author added if operation is successful

    return render(request,'author-add.html')# Template is rendered, which display form for adding a new author.

def author_edit(request, pk): # pk is a parameter that represents the primary key (id) of the BookAuthor object to be edited.
    author = get_object_or_404(BookAuthor, id=pk) #Retrieves the BookAuthor object with the given primary key (id=pk).

    if request.method == 'POST':
        name = request.POST.get('name') #  Retrieves the value of the form field with the name attribute 'name' for edit.
        author.name = name # Updates the name attribute of the author object with the new name.
        author.save() # Saves the changes to the database.
        return HttpResponse('Author Updated')

    return render(request, 'author-edit.html', {'author': author}) # author object passed to author-edit.html for display

def author_delete(request,pk):
    try:
        author= BookAuthor.objects.get(id=pk)
    except:
        return HttpResponse('Data is not Found beacause it may be  deleted. Please go one step back') # Data not found error handeling
    if request.method == 'POST':
        author.delete()
        return HttpResponse('Author Successfully Deleted')

    return render(request, 'author-delete-confirm.html', {'author': author})


###########################################################################################

# BookCategory Views CRUD
def category_list(request):
    category_objs = BookCategory.objects.all()
    data = {'categories': category_objs}
    return render(request, 'category.html', context=data)


def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if BookCategory.objects.filter(name=name).exists():
            error_message = f"Category with name '{name}' already exists."
            return render(request, 'category-add.html', {'error_message': error_message})

        BookCategory.objects.create(name=name)
        return HttpResponse('Category Added')

    return render(request, 'category-add.html')

def category_edit(request, pk):
    category = get_object_or_404(BookCategory, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        category.name = name
        category.save()
        return HttpResponse('Category Updated')

    return render(request, 'category-edit.html', {'category': category})

def category_delete(request,pk):
    try:
        category= BookCategory.objects.get(id=pk)
    except:
        return HttpResponse('Data is not Found beacause it may be  deleted. Please go one step back')    
    if request.method == 'POST':
        category.delete()
        return HttpResponse('Category Successfully Deleted')

    return render(request, 'category-delete-confirm.html', {'category': category})


###########################################################################################

#BookPublisher Views CRUD
def publisher_list(request):
    publisher_objs = BookPublisher.objects.all()
    data = {'publishers': publisher_objs}
    return render(request, 'publisher.html', context=data)

def publisher_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')

        if BookPublisher.objects.filter(name=name).exists():
            error_message = f"Publisher with name '{name}' already exists."
            return render(request, 'publisher-add.html', {'error_message': error_message})

        BookPublisher.objects.create(name=name, address=address)
        return HttpResponse('Publisher Added')

    return render(request, 'publisher-add.html')

def publisher_edit(request, pk):
    publisher = get_object_or_404(BookPublisher, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        publisher.name = name
        publisher.address = address
        publisher.save()
        return HttpResponse('Publisher Updated')

    return render(request, 'publisher-edit.html', {'publisher': publisher})

def publisher_delete(request,pk):
    try:
        publisher= BookPublisher.objects.get(id=pk)
    except:
        return HttpResponse('Data is not Found beacause it may be  deleted. Please go one step back')    
    if request.method == 'POST':
        publisher.delete()
        return HttpResponse('Publisher Successfully Deleted')

    return render(request, 'publisher-delete-confirm.html', {'publisher': publisher})

###########################################################################################

#BookLanguage View CRUD
def language_list(request):
    language_objs = BookLanguage.objects.all()
    data = {'languages': language_objs}
    return render(request, 'language.html', context=data)
    
def language_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if BookLanguage.objects.filter(name=name).exists():
            error_message = f"Language with name '{name}' already exists."
            return render(request, 'language-add.html', {'error_message': error_message})

        BookLanguage.objects.create(name=name)
        return HttpResponse('New Language Added')

    return render(request, 'language-add.html')

def language_edit(request, pk):
    language = get_object_or_404(BookLanguage, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        language.name = name
        language.save()
        return HttpResponse('Language Updated')

    return render(request, 'language-edit.html', {'language': language})

def language_delete(request,pk):
    try:
        language= BookLanguage.objects.get(id=pk)
    except:
        return HttpResponse('Data is not Found beacause it may be  deleted. Please go one step back')
    if request.method == 'POST':
        language.delete()
        return HttpResponse('Book Language Successfully Deleted')

    return render(request, 'language-delete-confirm.html', {'language': language})

###########################################################################################


#Book Views CRUD
def book_list(request):
    book_objs = Book.objects.all()
    data = {'books': book_objs}
    return render(request, 'book.html', context=data)


def book_get(request, pk):
    book_objs = get_object_or_404(Book, id=pk)
    return render(request, 'book-get.html', {'book': book_objs})


def book_add(request):
    if request.method == 'POST':
        name = request.POST.get('name') #Retrieves the name of book from single form field.
        author_ids = request.POST.getlist('author')  #Retrives list of authors in the form of id from multi form field.
        category_id = request.POST.get('category')
        edition = request.POST.get('edition')
        publisher_id = request.POST.get('publisher')
        publication_year = request.POST.get('publication_year')
        isbn = request.POST.get('isbn')
        language_id = request.POST.get('language')
        pages = request.POST.get('pages')
        description = request.POST.get('description')
        book_file = request.FILES.get('book_file') # Retrieves the uploaded file for the 'book_file' field.

        book = Book.objects.create(  # Creates a new Book object with the provided values and saves it to the database.
            name=name, 
            category_id=category_id, #Category_id field is assigned the corresponding ID for the category.
            edition=edition, 
            publisher_id=publisher_id, 
            publication_year=publication_year, 
            isbn=isbn, 
            language_id=language_id, 
            pages=pages, 
            description=description, 
            book_file=book_file
        ) 

        book.author.set(author_ids)  # Set the authors lists for the book object, many to many

        return HttpResponse('Book Added')

    authors = BookAuthor.objects.all()      # Retrives all data from BookAuthor Model to athors object used to populate in form field
    categories = BookCategory.objects.all()
    publishers = BookPublisher.objects.all()
    languages = BookLanguage.objects.all()

    return render(request, 'book-add.html', {
        'authors': authors,
        'categories': categories,
        'publishers': publishers,
        'languages': languages,
    }) #Retrives authors, categories, publishers, and languages are passed to the book-add.html, making them available for selection in the form.

def book_search(request):
    query = request.GET.get('query', '') # Retrieves the value of the query parameter from the URL. If the query parameter is not provided, it defaults to an empty string ('').

    if query: # Checks if a search query was provided.
        books = Book.objects.filter(
            Q(name__icontains=query) | # Matches books whose name contains the query string (case-insensitive).
            Q(author__name__icontains=query) | # The symbol "|" represent OR operator 
            Q(category__name__icontains=query) |
            Q(publisher__name__icontains=query) |
            Q(isbn__icontains=query)
        ).distinct() # Ensures that the results do not contain duplicate entries
    else:
        books = Book.objects.none() #If no query is provided, it returns an empty queryset.

    context = {
        'books': books, #  This allows the template to access the search results
        'query': query, #  This allows the template to display the current search query
    }
    
    return render(request, 'book-search.html', context)

def book_edit(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        author_ids = request.POST.getlist('author')
        category_id = request.POST.get('category')
        edition = request.POST.get('edition')
        publisher_id = request.POST.get('publisher')
        publication_year = request.POST.get('publication_year')
        isbn = request.POST.get('isbn')
        language_id = request.POST.get('language')
        pages = request.POST.get('pages')
        description = request.POST.get('description')

        book.name = name # Pass name value to the book object of name field for update
        book.category_id = category_id
        book.edition = edition
        book.publisher_id = publisher_id
        book.publication_year = publication_year
        book.isbn = isbn
        book.language_id = language_id
        book.pages = pages
        book.description = description

        book.author.set(author_ids) 
        book.save()

        return HttpResponse('Book Successfully Updated')

    authors = BookAuthor.objects.all()
    categories = BookCategory.objects.all()
    publishers = BookPublisher.objects.all()
    languages = BookLanguage.objects.all()

    return render(request, 'book-edit.html', {
        'book': book,
        'authors': authors,
        'categories': categories,
        'publishers': publishers,
        'languages': languages,
    })
def book_delete(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except:
        return HttpResponse('Data is not Found beacause it may be deleted. Please go one step back')    
    if request.method == 'POST':
        book.delete()
        return HttpResponse('Book Successfully Deleted')

    return render(request, 'book-delete-confirm.html', {'book': book})
