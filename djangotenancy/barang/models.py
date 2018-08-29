# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Barang (models.Model):
    id = models.AutoField(primary_key=True)
    # createdby = models.ForeignKey(
    # User, null=True, on_delete=models.CASCADE, default=User, editable=False)
    nama_barang = models.CharField(max_length=100)
    stok = models.IntegerField(default=0)
    waktu = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama_barang

    class Meta:
        verbose_name_plural = "Barang"
