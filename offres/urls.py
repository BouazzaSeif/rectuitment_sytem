from rest_framework import routers
from .views import OffreViewSet, CondidatureViewSet, OffrePublicViewSet, SendMailView
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('offres', OffreViewSet, basename='condidatures')
router.register('condidatures', CondidatureViewSet)
router.register('public-offres', OffrePublicViewSet)
urls = router.urls
urls.append(url(r'^send-mail/$', SendMailView.as_view()))


urlpatterns = urls
