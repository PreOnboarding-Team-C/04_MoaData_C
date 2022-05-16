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

        # json_data = request.data
        request = json.loads(request.body)

        # print(json_object)
        # print(json_object['job_id'])
        # print(json_object['job_name'])
        # print(json_object['task_list'])

        with open('job.json', 'r+', encoding='utf-8') as f:
            json_data = json.load(f)
            print(f"json_data 입니다. {json_data}")
            print(json_data['job'])
            # json_obj['job'].append(json_data)
            
            # json_data['job'].append({
            #     "job_id": json_object['job_id'],
            #     "job_name": json_object['job_name'],
            #     "task_list": json_object['task_list'],
            #     "property": json_object['property']
            # })

            # json_obj = json.load(f, indent=2)
            # print(f"json_obj 입니다 {json_obj}")
            # json_obj['job'].append(json_data)
        
        return Response('성공')
