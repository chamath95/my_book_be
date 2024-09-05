from django.urls import path
from .views import BookListCreateView, BookDetailView, BookSearchView, BookListView, TotalBookCountView, UserBookCountView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
    path('books/all/<int:pk>/', BookListView.as_view(), name='book-list-all'),
    path('books/total-count/', TotalBookCountView.as_view(), name='total-book-count'),
    path('books/user-count/', UserBookCountView.as_view(), name='user-book-count'),
]