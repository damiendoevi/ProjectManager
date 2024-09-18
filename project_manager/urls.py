"""
URL configuration for project_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings                      
from django.conf.urls.static import static
from django.urls import re_path, path, include;
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from Project.views import ProjectViewSet, TaskViewSet
from Comment.views import CommentViewSet

simple_router = SimpleRouter()
simple_router.register(r'projects', ProjectViewSet, basename="projects"),
simple_router.register(r'tasks', TaskViewSet, basename="tasks"),
simple_router.register(r'comments', CommentViewSet, basename="comments"),

urlpatterns = [
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    re_path('api/', include(simple_router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:     
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)