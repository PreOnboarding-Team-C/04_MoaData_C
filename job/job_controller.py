import os
import json
import pandas as pd


class JobExecutor:
    PATH = './job.json'

    # PATH 에 있는 모든 job 데이터 반환
    def _read_job(self, id=None):
        print(os.path)
        with open(self.PATH, 'r', encoding='utf-8') as f:
            job_list = json.load(f)

            if id:
                for job in job_list:
                    if int(job['job_id']) == int(id):
                        return job
            else:
                return job_list

        if id:
            return (f'404: 입력하신 [{id}] id는 존재하지 않는 id 입니다.')

    # 실제 파일에 쓰기
    def _write_json(self, job):
        with open(self.PATH, 'w', encoding='utf-8') as f:
            json.dump(job, f, indent=4, ensure_ascii=False)

    # job_id 에 해당하는 데이터의 index 반환
    def _get_index(self, job_list, id):
        for idx, job in enumerate(job_list):
            if int(job['job_id']) == int(id):
                return idx

    # 파일에 이미 존재하는 job_id 인지 판별 => 있으면 T 없으면 F
    def _is_exist_(self, job_list, id):
        for job in job_list:
            if int(job['job_id']) == int(id):
                return True
        return False

    def read(self, id=None):
        return self._read_job(id)

    # job 추가
    def create(self, input_job):
        job_list = self._read_job()
        if self._exist_or_not(job_list, input_job['job_id']):
            return "이미 존재하는 job_id 입니다."
        else:
            job_list.append(input_job)
            self._write_json(job_list)
        
    # job 업데이트
    def update(self, id, input_job):
        if id != input_job['job_id']:
            return f'job_id 값은 변경할 수 없습니다.'
        job_list = self._read_job()
        job_index = self._get_index(job_list, id)
        job_list[job_index] = input_job

        self._write_json(job_list)

    # job 삭제
    def delete(self, id):
        job_list = self._read_job()
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
        for task in task_list:
            task_function = getattr(task_executor, task)
            task_function(job)

        return task_executor.DF


class TaskExecutor:

    DF = None

    def read(self, job):
        task = job['property']['read']
        self.DF = pd.read_csv(task['filename'], delimiter=task['sep'])
        return self.DF

    def drop(self, job):
        task = job['property']['drop']
        self.DF = self.DF.drop(task['column_name'], axis=1)
        return self.DF

    def write(self, job):
        task = job['property']['write']
        self.DF.to_csv(task['filename'], sep=task['sep'], index=False)