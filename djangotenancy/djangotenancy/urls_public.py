from django.conf.urls import url
from djangotenancy.views import HomeView
from django.contrib import admin
# from todo.admin import MyAdminSite
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
]
