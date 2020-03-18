from rest_framework.routers import SimpleRouter

from .views import BetaViewSet

router = SimpleRouter()
router.register(r'beta', BetaViewSet)

urlpatterns = router.urls
