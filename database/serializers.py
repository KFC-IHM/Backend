from rest_framework import serializers

from database.models import CustomUser, Restaurant, OpenHoursWeek, Review, Comment


class OpenHoursWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHoursWeek
        fields = ('id', 'day', 'open', 'close', 'restaurant')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'description', 'review', 'author')


class ReviewSerializer(serializers.ModelSerializer):
    # related fields
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'description', 'rating', 'restaurant', 'comment_set', 'author', 'restaurant')


class RestaurantSerializer(serializers.ModelSerializer):
    # related fields
    openhoursweek_set = OpenHoursWeekSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'image', 'owner', 'openhoursweek_set', 'review_set', 'latitude',
                  'longitude')


class CustomUserSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    restaurant_set = RestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login',
                  'first_name', 'last_name', 'groups', 'is_moderator', 'is_restaurateur', 'is_consumer', 'review_set',
                  'comment_set', 'restaurant_set', 'profile_image']
