from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import utils

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = utils.PhotoSerializer
