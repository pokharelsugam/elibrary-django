"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from library.views import home, book_list, book_add, book_search, book_get, book_edit, book_delete, author_list, author_add, author_edit, author_delete, category_list, category_add, category_edit, category_delete, publisher_list, publisher_add, publisher_edit, publisher_delete, language_list, language_add, language_edit, language_delete   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    #For Book CRUD Operation Url
    path('book/',book_list, name='book_list'),
    path('book/add/',book_add, name= 'book_add'),
    path('book/search/', book_search, name='book_search'),
    path('book/get/<int:pk>/', book_get, name='book_get'),
    path('book/edit/<int:pk>/', book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', book_delete, name='book_delete'),
    #For Author CRUD Operation Url
    path('author/',author_list,name='author_list'),
    path('author/add/',author_add, name= 'author_add'),
    path('author/edit/<int:pk>/',author_edit, name = 'author_edit'),
    path('author/delete/<int:pk>/',author_delete, name = 'author_delete'),
    #For Category CRUD Operation Url
    path('category/',category_list, name='category_list'),
    path('category/add/', category_add, name='category_add'),
    path('category/edit/<int:pk>/', category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),
    #For Publisher CRUD Operation Url
    path('publisher/', publisher_list, name = 'publisher_list'),
    path('publisher/add/', publisher_add, name='publisher_add'),
    path('publisher/edit/<int:pk>/', publisher_edit, name='publisher_edit'),
    path('publisher/delete/<int:pk>/', publisher_delete, name='publisher_delete'),
    #For Language CRUD Operation Url
    path('language/', language_list, name = 'language_list'),
    path('language/add/', language_add, name='language_add'),
    path('language/edit/<int:pk>/', language_edit, name='language_edit'), 
    path('language/delete/<int:pk>/', language_delete, name='language_delete'), 

]

# Adds URL patterns to serve media files.

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)