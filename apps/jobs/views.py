from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .job import JobExecutor


class JobCreateAPIView(ListCreateAPIView):
    '''
    Assignee : 장우경
    Reviewer : -
    '''
    job_executor = JobExecutor()
    
    # job.json에 추가
    def post(self, request):
        self.job_executor.create(request.data)
        
        # 정상적으로 추가되었는지 확인하기 위해 추가된 데이터 리턴
        job_list = self.job_executor.read_all_jobs()
        job_index = self.job_executor.get_index(job_list, request.data['job_id'])
        return Response(job_list[job_index], status=status.HTTP_201_CREATED)

    # job.json 전체 리스트 조회
    def get(self, request):
        jobs_list = self.job_executor.read_all_jobs()
        return Response(jobs_list, status=status.HTTP_200_OK)


class JobDetailAPIView(RetrieveUpdateDestroyAPIView):
    '''
    Assignee : 장우경
    Reviewer : -
    '''
    job_executor = JobExecutor()

    # 특정 job_id에 해당하는 데이터 조회
    def get(self, request, job_id):
        job = self.job_executor.read_job_detail(job_id)
        return Response(job, status=status.HTTP_200_OK)

    # 특정 job_id에 해당하는 데이터 수정
    def put(self, request, job_id):
        self.job_validate(request, job_id)

        job = self.job_executor.update_job(request.data)
        return Response(job, status=status.HTTP_200_OK)

    # 특정 job_id에 해당하는 데이터 삭제
    def delete(self, request, job_id):
        self.job_executor.delete(job_id)
        return Response({'message': 'job_id "{job_id}"가 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

    # job_id 유효성 체크
    def job_validate(self, request, job_id):
        if not request.data['job_id'] == job_id:
            raise(Exception(f'입력하신 job_id "{job_id}"가 같지 않습니다.'))
        return True


class TaskAPIView(APIView):
    def get(self, request, job_id):
        job_executor = JobExecutor()
        job_executor.run(job_id)
        return Response({'message': '진행 중'}, status=status.HTTP_200_OK)
