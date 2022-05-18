import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.job import JobExecutor, TaskExecutor


je = JobExecutor()

# Create your views here.
class JsonAPI(APIView, JobExecutor):

    
    def get(self, request, format=None):

        jobs = je._read_all_job()

        return Response(jobs)

    def post(self, request):

        input_job = json.loads(request.body)

        jobs = je._read_all_job()
        jobs.append(input_job)

        return Response(jobs)

    # def post(self, request):

    #     # print(f"request입니다, :  {request}")

    #     request = json.loads(request.body)

    #     with open('job.json', 'r', encoding='utf-8') as rf:
    #         json_data = json.load(rf)
    #         print(f"json_data, :  {json_data}")
    #         with open('job.json', 'w', encoding='utf-8') as wf:
    #             json_data.append({
    #                 "job_id": request['job_id'],
    #                 "job_name": request['job_name'],
    #                 "task_list": request['task_list'],
    #                 "property": request['property']
    #             })

    #             json.dump(json_data, wf, indent=4)
        
    #     return Response('성공')


class JsonDetailAPI(APIView, JobExecutor):

    def get(self, request, job_id=None):

        job = je._read_job(job_id)

        return Response(job)

    def patch(self, request, job_id=None):

        input_job = json.loads(request.body)

        job = je.edit(job_id, input_job)

        return Response(job)