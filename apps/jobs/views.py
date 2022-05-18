import os
import django
from rest_framework.views import APIView
from rest_framework.response import Response

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


class JobAPIView(APIView):
    JOBS_PATH = '..src.job.json'

    




    def post(self, request):
        data = request.data
        print(data)
        
        
        
        
        
        return Response({'message': 'OK'}, status=201)
