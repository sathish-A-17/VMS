from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('vendors/', vendors_view, name='vendors'),
    path('orders/', orders_view, name='orders'),
    path('historical_performance/', historical_performance_view, name='historical_performance'),
    path('api/', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorViewSet.performance, name='vendor_performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderViewSet.acknowledge, name='acknowledge_purchase_order'),
]