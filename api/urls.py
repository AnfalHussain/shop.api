from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from app.views import (ProductListView, OrderItems,
                       NewOrdersListView, UpdateOrderView)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path("orders/", OrderItems.as_view(), name="order-items"),
    path("admin/orders/", NewOrdersListView.as_view(), name="order-list"),
    path("admin/update/order/<int:order_id>/",
         UpdateOrderView.as_view(), name="order-edit"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
