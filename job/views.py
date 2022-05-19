from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, HTTP_201_CREATED

from .job_controller import JobExecutor


# api/v1/jobs [C, R]
class JobListView(APIView):
    '''
    Assignee : 홍은비, 장우경, 진병수
    Reviewer : -
    '''
    executor = JobExecutor()

    def get(self, request):
        data = self.executor.read()
        return Response(data, status=HTTP_200_OK)

    def post(self, request):
        try:
            self.executor.create(request.data)
            return Response(request.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=HTTP_409_CONFLICT)


# api/v1/jobs/<int:id> [R, U, D]
class JobDetailRUDViews(APIView):
    '''
    Assignee : 홍은비, 장우경, 진병수
    Reviewer : -
    '''
    executor = JobExecutor()

    def get(self, request, id):
        try:
            data = self.executor.read(id)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            data = self.executor.update(id, request.data)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            self.executor.delete(id)
            return Response("job이 정상적으로 삭제되었습니다.", status=HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)


# api/v1/jobs/<int:id>/run
class JobTaskView(APIView):
    '''
    Assignee : 홍은비
    Reviewer : 장우경, 진병수
    '''
    def get(self, request, id):
        job_executor = JobExecutor()
        try:
            data = job_executor.run(id)
            return Response(data, status=HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=HTTP_404_NOT_FOUND)
