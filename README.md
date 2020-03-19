# drf-versioning
Example app with two approaches for versioning API with django rest framework

First approach implemented in `alpha` django application.
With this approach api v1 and v2 shares model, but has it's own views and serializers.

Second approach implemented in `beta` django application.
With this approach api v1 and v2 shares model and view, but has it's own serializers.
To share view for both versions `SerializerClassMixin` is introduced.

It's possible to mix both approaches even in same djanogo application.

### Composing urls in main urls.py

Each application exposes `router` which is drf SimpleRouter

    from rest_framework.routers import SimpleRouter
    router = SimpleRouter()
    router.register(r'app', AppViewSet)

Main urls.py instantiate DefaultRouter and extend it with application routers

    from rest_framework.routers import DefaultRouter
    from alpha.api_v1.urls import router as alpha_v1_router
    from alpha.api_v2.urls import router as alpha_v2_router
    from beta.api.urls imprt router as beta_router
    
    v1_router = DefaultRouter()
    v1_router.registry.extend(alpha_v1_router.registry)
    v1_router.registry.extend(beta_router)
    
    v2_router = DefaultRouter()
    v2_router.registry.extend(alpha_v2_router.registry)
    v2_router.registry.extend(beta_router.registry)
    
    urlpatterns = [
        path('api/v1/', include((v1_router.urls, 'api'), namespace='v1')),
        path('api/v2/', include((v2_router.urls, 'api'), namespace='v2')),
    ]

### Alpha - completely separated views and serializers for each api version
Application structure

    ├── api_v1
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── api_v2
    │   ├── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── apps.py
    └── models.py
    
The reason for copy and paste views, serializers and urls is to be able to change anything in specific version and do not affect another one.

### Beta - using same view set with different serializers
Application structure

    ├── api
    │   ├── v1
    │   │   └── serializers.py
    │   ├── v2
    │   │   └── serializers.py
    │   ├── urls.py
    │   └── views.py
    ├── apps.py
    ├── mixins.py
    └── models.py
    
In this case `SerializerClassMixin` is introduced, so we can define view this way:

    version_map = {
        'v1': BetaSerializer_v1,
        'v2': BetaSerializer_v2,
    }
    
    class BetaViewSet(SerializerClassMixin, viewsets.ModelViewSet):
        version_map = version_map
        queryset = Beta.objects.all()

Key for the `version_map` should be same we have in main `urls.py` namespace for specific path.