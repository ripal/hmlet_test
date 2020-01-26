from rest_framework import routers
from core import views as photos_views

router = routers.DefaultRouter()
router.register(r'photos', photos_views.PhotoViewSet)