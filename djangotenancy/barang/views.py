from .models import Barang
# from django.shortcuts import get_object_or_404
# from rest_framework import generics, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BarangSerializer


class DeleteBarang(APIView):

    def get(self, request, format=None):
        Barangs = Barang.objects.all()
        serializer = BarangSerializer(Barangs, many=True)
        return Response(serializer.data)

    # def get_queryset(self, request, format=None):
    #     qs = super(BarangSerializer, self).get_queryset(request)
    #     return qs.filter(createdby=request.user)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BarangDetail(APIView):
    """
    Retrieve, update or delete a Barang instance.
    """

    def get_object(self, pk):
        try:
            return Barang.objects.get(pk=pk)
        except Barang.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang = BarangSerializer(Barang)
        return Response(Barang.data)

    def put(self, request, pk, format=None):
        Barang = self.get_object(pk)
        serializer = BarangSerializer(Barang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BarangList(APIView):
    """
    Menampilkan semua data barang, atau tambah data barang baru.
    """

    def get(self, request, format=None):
        Barangs = Barang.objects.all()
        serializer = BarangSerializer(Barangs, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request):
        # ini merequest data dari serialized
        serializer = BarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse("Hello, world. Ini halaman utama")
