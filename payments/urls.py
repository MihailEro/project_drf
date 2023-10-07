from rest_framework.routers import DefaultRouter
from payments.views import PaymentViewSet
from payments.apps import PaymentsConfig


app_name = PaymentsConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [

] + router.urls
