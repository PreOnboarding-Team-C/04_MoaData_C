from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .job_controller import JobExecutor
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST


# api/v1/jobs [C, R]
class JobListView(APIView):
    
    def get(self, request):
        executor = JobExecutor()
        data = executor.read()
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        executor = JobExecutor()
        data = executor.create(request.data)
        return Response(data, status=HTTP_200_OK)


# api/v1/jobs/<int:id> [R, U, D]
class JobDetailRUDViews(APIView):

    def get(self, request, id):
        executor = JobExecutor()
        data = executor.read(id)
        if type(data) == str:
            return Response(data, status=HTTP_404_NOT_FOUND)
        return Response(data, status=HTTP_200_OK)

    def put(self, request, id):
        executor = JobExecutor()
        data = executor.update(id, request.data)
        if type(data) == str:
            return Response(data, status=HTTP_400_BAD_REQUEST)
        return Response(data, status=HTTP_200_OK)

    def delete(self, request, id):
        executor = JobExecutor()
        executor.delete(id)
        return Response(None, status=HTTP_204_NO_CONTENT)



# api/v1/jobs/<int:id>/run
class JobTaskView(APIView):

    def get(self, request, id):
        executor = JobExecutor()
        data = executor.run(id)
        return Response(data, status=HTTP_200_OK)
