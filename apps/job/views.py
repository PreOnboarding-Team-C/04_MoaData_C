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

    def post(self, request):

        # print(f"request입니다, :  {request}")

        request = json.loads(request.body)

        with open('job.json', 'r', encoding='utf-8') as rf:
            json_data = json.load(rf)
            with open('job.json', 'w', encoding='utf-8') as wf:
                json_data['job'].append({
                    "job_id": request['job_id'],
                    "job_name": request['job_name'],
                    "task_list": request['task_list'],
                    "property": request['property']
                })

                json.dump(json_data, wf, indent=4)
        
        return Response('성공')

    def patch(self, request, job_id):

        print(f"request.data 입니다. :  {job_id}")

        request = json.loads(request.body)

        print(f"request입니다, :  {request}")

        return Response('성공')