from rest_framework import routers

from database.views import CustomUserViewSet, RestaurantViewSet, OpenHoursWeekViewSet, ReviewViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'openhoursweek', OpenHoursWeekViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls
