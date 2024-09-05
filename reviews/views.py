from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer
from rest_framework.response import Response
from django.db.models import Avg
from rest_framework import status


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Comment.objects.filter(book_id=book_id)


class RatingCreateUpdateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        book_id = data.get('book')
        rating_value = data.get('rating')

        rating, created = Rating.objects.get_or_create(
            user=user,
            book_id=book_id,
            defaults={'rating': rating_value}
        )

        if not created:
            rating.rating = rating_value
            rating.save()

        serializer = self.get_serializer(rating)
        return Response({
            'status': 1 if created else 0,
            'data': serializer.data
        }, status=status.HTTP_200_OK)


class AverageRatingView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        book_id = self.kwargs['book_id']
        average_rating = Rating.objects.filter(book_id=book_id).aggregate(Avg('rating'))['rating__avg']
        return Response({'average_rating': average_rating})
