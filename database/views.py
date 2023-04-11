from rest_framework import viewsets

from database.models import CustomUser, Restaurant, OpenHoursWeek, Review, Comment
from database.serializers import CustomUserSerializer, RestaurantSerializer, OpenHoursWeekSerializer, ReviewSerializer, \
    CommentSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OpenHoursWeekViewSet(viewsets.ModelViewSet):
    queryset = OpenHoursWeek.objects.all()
    serializer_class = OpenHoursWeekSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
