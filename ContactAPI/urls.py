from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from contact.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contact',ContactViewSet)

urlpatterns = [
    url(r'^api/v1/',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
