# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ()
    search_fields = ['name']
    list_per_page = 25


admin.site.register(Client, ClientAdmin)
