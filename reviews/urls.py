from django.urls import path
from .views import CommentCreateView, CommentListView, RatingCreateUpdateView, AverageRatingView

urlpatterns = [
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:book_id>/', CommentListView.as_view(), name='comment-list'),
    path('ratings/', RatingCreateUpdateView.as_view(), name='rating-create'),
    path('average-rating/<int:book_id>/', AverageRatingView.as_view(), name='average-rating'),
]

