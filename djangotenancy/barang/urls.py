from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from barang.views import *

router = routers.DefaultRouter()
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # ini bisa diarahkan ke register
    url(r'^$', include(router.urls)),
    # url(r'^$', views.index, name='index'),
    url(r'^barang/(?P<pk>[0-9]+)', BarangDetail.as_view()),
    url(r'^barang', BarangList.as_view(), name='barang'),
    url(r'^barang/delete', DeleteBarang.as_view()),
]
