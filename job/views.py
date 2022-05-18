from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .executor import JobExecutor
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT


# api/v1/jobs [C, R]
class JobListView(APIView):
    '''
    Assignee : 홍은비
    Reviewer : -
    '''
    def get(self, request):
        executor = JobExecutor()
        data = executor.read()
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        executor = JobExecutor()
        try:
            data = executor.create(request.data)
            return Response(request.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_409_CONFLICT)


# api/v1/jobs/<int:id> [R, U, D]
class JobDetailRUDViews(APIView):
    '''
    Assignee : 홍은비
    Reviewer : -
    '''
    def get(self, request, id):
        executor = JobExecutor()
        try:
            data = executor.read(id)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)
        

    def put(self, request, id):
        executor = JobExecutor()
        try:
            data = executor.update(id, request.data)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)


    def delete(self, request, id):
        executor = JobExecutor()
        try:
            executor.delete(id)
            return Response("job이 정상적으로 삭제되었습니다.", status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)


# api/v1/jobs/<int:id>/run
class JobTaskView(APIView):
    '''
    Assignee : 홍은비
    Reviewer : -
    '''
    def get(self, request, id):
        executor = JobExecutor()
        try:
            data = executor.run(id)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)
