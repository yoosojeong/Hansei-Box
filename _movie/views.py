from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import forms

class Main(APIView):

    def get(self, request, format=None):
        
        MovieDatas = models.MovieModel.objects.all()
        context = { 'MovieDatas' : MovieDatas }

        return render(request, "main.html", context)
