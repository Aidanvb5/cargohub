# your_app_name/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.warehouses import WarehouseViewSet
from .views.locations import LocationViewSet
from .views.transfers import TransferViewSet
from .views.items import ItemViewSet
from .views.suppliers import SupplierViewSet
from .views.orders import OrderViewSet
from .views.clients import ClientViewSet
from .views.shipments import ShipmentViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'transfers', TransferViewSet)
router.register(r'items', ItemViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'shipments', ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]