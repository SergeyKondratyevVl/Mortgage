from rest_framework.routers import DefaultRouter

from mortgage.views import MortgageViewSet


router = DefaultRouter()
router.register('offer', MortgageViewSet)
