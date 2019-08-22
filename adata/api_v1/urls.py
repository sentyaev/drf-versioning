from rest_framework.routers import DefaultRouter

from .views import ADataViewSet

router = DefaultRouter()
router.register(r'a_data', ADataViewSet)

urlpatterns = router.urls
