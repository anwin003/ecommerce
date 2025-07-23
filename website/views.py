from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import CustomOrder
from .serializers import CustomOrderSerializer

# ================================
# 📦 CUSTOM ORDER VIEWSET
# ================================
class CustomOrderViewSet(viewsets.ModelViewSet):
    queryset = CustomOrder.objects.all()
    serializer_class = CustomOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ================================
# 🔐 ADMIN DASHBOARD ENDPOINTS
# ================================

# 🔸 BLOCK USER
@api_view(['POST'])
@permission_classes([IsAdminUser])
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return Response({"message": "User blocked"})

# 🔸 DELETE USER
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return Response({"message": "User deleted"})

# 🔸 UPDATE ORDER STATUS
@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_order_status(request, order_id):
    order = get_object_or_404(CustomOrder, id=order_id)
    status = request.data.get('status')
    if not status:
        return Response({"error": "Status not provided"}, status=400)
    order.status = status
    order.save()
    return Response({"message": f"Order status updated to {status}"})

# 🔸 CANCEL ORDER
@api_view(['POST'])
@permission_classes([IsAdminUser])
def cancel_order(request, order_id):
    order = get_object_or_404(CustomOrder, id=order_id)
    order.status = "Cancelled"
    order.save()
    return Response({"message": "Order cancelled"})
