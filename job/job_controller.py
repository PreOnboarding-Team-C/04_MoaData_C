import os
import json


class JobExecutor:
    PATH = './job.json'

    def _read_all_job(self, id=None):
        print(os.path)
        with open(self.PATH, 'r') as f:
            job_list = json.load(f)

            if id:
                for job in job_list:
                    if int(job['job_id']) == int(id):
                        return job
            else:
                return job_list

        if id:
            return (f'404: 입력하신 [{id}] id는 존재하지 않는 id 입니다.')
    
    def _read_job(self, id=None):
        return self._read_all_job(id)

    # 실제 파일에 쓰기
    def _write_json(self, job):
        with open(self.PATH, 'w', encoding='utf-8') as f:
            json.dump(job, f, indent=4)

    def _get_index(self, job_list, id):
        for idx, job in enumerate(job_list):
            if int(job['job_id']) == int(id):
                return idx

    # 현재 존재하는 job_id 인지 판별
    def _exist_or_not(self, job_list, id):
        for job in job_list:
            if int(job['job_id']) == int(id):
                return False
        return True

    def read(self, id=None):
        return self._read_job(id)

    # job 데이터 추가
    def create(self, input_job):
        job_list = self._read_all_job()
        if self._exist_or_not(job_list, input_job['job_id']):
            job_list.append(input_job)
            self._write_json(job_list)
        else:
            return "이미 존재하는 job_id 입니다."

    def update(self, id, input_job):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, id)
        job_list[job_index] = input_job

        self._write_json(job_list)

    def delete(self, id):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, id)

        job_list.pop(job_index)

        self._write_json(job_list)

    
    # Job Task execute function

    def run(self, id=None):
        job = self._read_job(id)
        task_list = ['read']
        # read 다음 수행될 task 추가
        task_list.append(*job['task_list']['read'])
        # 다음 수행될 task 가 있다면 추가
        if task:=job['task_list'][task_list[-1]]:
            task_list.append(*task)
        
        task_executor = TaskExecutor()

class TaskExecutor:
    pass