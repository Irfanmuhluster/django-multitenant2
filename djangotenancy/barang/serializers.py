from .models import Barang
from rest_framework import serializers


class BarangSerializer(serializers.ModelSerializer):
    nama_barang = serializers.CharField(max_length=200)
    stok = serializers.IntegerField()

    class Meta:
        model = Barang
        fields = ('__all__')
