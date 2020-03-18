from rest_framework.routers import SimpleRouter

from .views import AlphaViewSet

router = SimpleRouter()
router.register(r'alpha', AlphaViewSet)
