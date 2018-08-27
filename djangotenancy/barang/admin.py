from django.contrib import admin
from .models import Barang

# admin.site.register(Task)


class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama_barang', 'stok', 'waktu']
    list_filter = ()
    search_fields = ['nama_barang']
    list_per_page = 25


admin.site.register(Barang, BarangAdmin)
