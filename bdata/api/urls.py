from rest_framework.routers import DefaultRouter

from .views import BDataViewSet

router = DefaultRouter()
router.register(r'b_data', BDataViewSet)

urlpatterns = router.urls
