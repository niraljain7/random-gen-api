from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import random


# Create your views here.
class Randomgen(APIView):

	def get(self, request, num, format=None):
		random.seed(datetime.now())
		lis = []
		for i in range(num):
			lis.append(random.randint(1,100))
		return Response(lis)
		