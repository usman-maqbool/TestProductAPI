
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from products_app.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
