"""
URL configuration for furniture project.

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from furnitureapp import views



router = routers.DefaultRouter()
router.register(r'menus', views.MenuViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'features', views.FeatureViewSet)
router.register(r'feature-images', views.FeatureImageViewSet)
router.register(r'container-images', views.ContainerImageViewSet)
router.register(r'item-products', views.ItemProductViewSet)
router.register(r'testimonials', views.TestimonialViewSet)
router.register(r'post-images', views.PostViewSet)
router.register(r'product2s', views.ShopViewSet)
router.register(r'abouts', views.AboutViewSet)
router.register(r'feature-icons', views.FeatureIconViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'post-blogs', views.PostBlogViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'product1s', views.Product1ViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furnitureapp.urls'), name='furnitureapp'),
    path('api/', include(router.urls)),  # Include API routes from DRF router

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
