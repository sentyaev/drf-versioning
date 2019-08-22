"""rest1 URL Configuration

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

from adata.api_v1.urls import urlpatterns as adata_urlpatterns_v1
from adata.api_v2.urls import urlpatterns as adata_urlpatterns_v2
from adata.api_v3.urls import urlpatterns as adata_urlpatterns_v3


from bdata.api.urls import urlpatterns as bdata_urlpatterns


api_v1_urlpatterns = [*adata_urlpatterns_v1, *bdata_urlpatterns]
api_v2_urlpatterns = [*adata_urlpatterns_v2, *bdata_urlpatterns]
api_v3_urlpatterns = [*adata_urlpatterns_v3, *bdata_urlpatterns]

urlpatterns = [
    path('api/v1/', include((api_v1_urlpatterns, 'api'), namespace='v1')),
    path('api/v1/', include((api_v2_urlpatterns, 'api'), namespace='v2')),
    path('api/v3/', include((api_v3_urlpatterns, 'api'), namespace='v3')),


    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

