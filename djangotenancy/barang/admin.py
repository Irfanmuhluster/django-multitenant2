from django.contrib import admin
# from resultregistration.models import Client
from .models import Barang
# from .models import Client
# from django.db import utils
# admin.site.register(Task)


class BarangAdmin(admin.ModelAdmin):
    list_display = ['nama_barang', 'stok', 'waktu']
    list_filter = ()
    search_fields = ['nama_barang']
    list_per_page = 25


admin.site.register(Barang, BarangAdmin)


# class ClientAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     list_filter = ()
#     search_fields = ['name']
#     list_per_page = 25


# admin.site.register(Client, ClientAdmin)

# from django.contrib import admin
# from django.db import utils
# from .models import Barang

# tidak mungkin karena databasenya mengakses public sdgkan public tdk ada tabel
# barang_barang atau tidak ada barang_client adanya customer_client !
# try:
#     Client.objects.get(schema_name='public')
# except utils.DatabaseError:
#     pass

# qs = Barang.objects.count() == 1
# if qs.exists():
#     class BarangAdmin(admin.ModelAdmin):
#         list_display = ['nama_barang', 'stok', 'waktu']
#         list_filter = ()
#         search_fields = ['nama_barang']
#         list_per_page = 25

#     admin.site.register(Barang, BarangAdmin)
# else:
#     pass
