"""drf_versioning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include, path

from alpha.api_v1.urls import router as alpha_router_v1
from alpha.api_v2.urls import router as alpha_router_v2
from alpha.api_v3.urls import router as alpha_router_v3


from beta.api.urls import router as beta_router
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.registry.extend(alpha_router_v1.registry)
v1_router.registry.extend(beta_router.registry)

v2_router = DefaultRouter()
v2_router.registry.extend(alpha_router_v2.registry)
v2_router.registry.extend(beta_router.registry)

v3_router = DefaultRouter()
v3_router.registry.extend(alpha_router_v3.registry)
v3_router.registry.extend(beta_router.registry)

urlpatterns = [
    path('api/v1/', include((v1_router.urls, 'api'), namespace='v1')),
    path('api/v2/', include((v2_router.urls, 'api'), namespace='v2')),
    path('api/v3/', include((v3_router.urls, 'api'), namespace='v3')),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
