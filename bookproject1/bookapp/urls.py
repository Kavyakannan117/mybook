from django.urls import path
from .import views
urlpatterns = [
    path("createbook/", views.createBook ,name='createbook'),
    path("author/",views.createAuthor,name='author'),
    path('booklist/',views.listBook ,name='booklist'),
    path('detailsview/<int:book_id>/',views.detailsBook,name="details"),
    path('updateview/<int:book_id>/',views.updateBook,name="update"),
    path('deleteview/<int:book_id>/',views.deleteBook,name="delete"),

    path('updateAuthorView/<int:book_id>/',views.updateAuthorView,name="updateAuthor"),
    path('deleteAuthorView/<int:book_id>/',views.deleteAuthorView,name="deleteAuthor"),
    path('search/',views.SearchBook,name='search'),
    path('',views.home)
]
