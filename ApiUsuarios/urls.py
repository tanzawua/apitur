from rest_framework import routers
from .api import ServicioviewSet


router = routers.DefaultRouter()
router.register('api/ApiUsuario',ServicioviewSet, 'ApiUsuario')

urlpatterns = router.urls