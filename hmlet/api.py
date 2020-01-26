from rest_framework import routers
from photos import views as photo_views

router = routers.DefaultRouter()
router.register(r'photos', photo_views.PhotoViewSet)