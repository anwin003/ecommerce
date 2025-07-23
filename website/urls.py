from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomOrderViewSet,
    block_user,
    delete_user,
    update_order_status,
    cancel_order,
)

router = DefaultRouter()
router.register(r'custom-orders', CustomOrderViewSet, basename='custom-orders')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/block-user/<int:user_id>/', block_user),
    path('admin/delete-user/<int:user_id>/', delete_user),
    path('admin/update-order-status/<int:order_id>/', update_order_status),
    path('admin/cancel-order/<int:order_id>/', cancel_order),
]
