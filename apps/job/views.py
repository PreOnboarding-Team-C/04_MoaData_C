import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class JsonAPI(APIView):
    
    def get(self, request, format=None):

        with open('job.json', 'r') as f:

            json_data = json.load(f)

        # print(json.dumps(json_data))
        return Response(json_data)