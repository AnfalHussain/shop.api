from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app.views import (ProductListView, OrderItems)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path("orders/", OrderItems.as_view(), name="order-items"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
