from django.conf.urls import url, include
from djangotenancy.views import HomeView
from django.contrib import admin
# from todo.admin import MyAdminSite
from django.urls import path


urlpatterns = [
    url(r'^', include('customers.urls')),
    # path('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]
