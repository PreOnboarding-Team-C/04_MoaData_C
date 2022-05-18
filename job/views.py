from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .job_controller import JobExecutor


# api/v1/jobs [C, R]
class JobListView(APIView):
    def get(self, request):
        executor = JobExecutor()
        data = executor.read()
        return Response(data, status=200)

    def post(self, request):
        executor = JobExecutor()
        data = executor.create(request.data)
        return Response(data, status=200)


# api/v1/jobs/<int:id> [R, U, D]
class JobDetailRUDViews(APIView):

    def get(self, request, id):
        executor = JobExecutor()
        data = executor.read(id)
        if type(data) == str:
            return Response(data, status=404)
        return Response(data, status=200)

    def put(self, request, id):
        executor = JobExecutor()
        print('request.data 의 아이디 : ', request.data['job_id'])
        if id != request.data['job_id']:
            return Response(f'job_id 값은 변경할 수 없습니다.', status=400)
        data = executor.update(id, request.data)
        return Response(data, status=200)

    def delete(self, request, id):
        executor = JobExecutor()
        executor.delete(id)
        return Response(None, status=204)

# api/v1/jobs/<int:id>/run
class JobTaskView(APIView):

    def get(self, request, id):
        executor = JobExecutor()
        executor.run(id)
        return Response(None, status=204)
