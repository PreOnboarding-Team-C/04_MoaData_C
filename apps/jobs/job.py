import json
import pandas as pd


class TaskExecutor:
    data_frame = None
    
    def read(self, job):
        task = job['property']['read']
        
        self.data_frame = pd.read_csv(task['filename'], delimiter=task['sep'])
        return self.data_frame
    
    
    def drop(self, job):
        task = job['property']['drop']
        self.data_frame = self.data_frame.drop(task['column_name'], axis=1)
        return self.data_frame
        
    
    
    def write(self, job):
        task = job['property']['write']
        self.data_frame.to_csv(task['filename'], sep=task['sep'], index=False)
        

class JobExecutor:
    '''
    Assignee : 장우경
    Reviewer : -
    '''
    JOB_PATH = './job.json'

    # job_id 전달 받으면 해당 값 체크 후 리턴
    # 전달 받은 job_id 값 자체가 없다면 전체 리스트 리턴 
    def read_all_jobs(self, job_id=None):
        with open(self.JOB_PATH, 'r') as file:
            jobs = json.load(file)
            if job_id:
                for job in jobs:
                    if job['job_id'] == job_id:
                        return job

                return f'해당 job_id {job_id}가 존재하지 않습니다.'
            return jobs

    # 특정 job_id 데이터 리턴
    def read_job_detail(self, job_id):
        return self.read_all_jobs(job_id)

    # 전달 받은 job_list를 job.json에 입력 후 저장
    def write_job(self, job_list):
        with open(self.JOB_PATH, 'w') as file:
            json.dump(job_list, file, indent='\t', ensure_ascii=False)
            return job_list

    # job_id에 일치하는 인덱스 값 리턴
    def get_index(self, job_list, job_id):
        for idx, job in enumerate(job_list):
            if job['job_id'] == job_id:
                return idx
        return f'해당 {job_id}가 존재하지 않습니다.'

    # 새로운 job 데이터 추가 입력하여 저장
    def create(self, new_job_info):
        jobs_list = self.read_all_jobs()
        jobs_list.append(new_job_info)
        self.write_job(jobs_list) 

    # 수정하려는 job 데이터의 인덱스 통해서 해당 데이터 수정 후 저장
    def update_job(self, job_info):
        job_list = self.read_all_jobs()

        job_id = job_info['job_id']
        job_index = self.get_index(job_list, job_id)        
        job_list[job_index] = job_info

        self.write_job(job_list)
        return job_list[job_index]

    # job_id에 해당하는 job 데이터 삭제 후 저장    
    def delete(self, job_id):
        job_list = self.read_all_jobs()
        
        job_index = self.get_index(job_list, job_id)
        del job_list[job_index]
        
        self.write_job(job_list)
        
        
    def run(self, job_id):
        task_executor = TaskExecutor()
        job = self.read_job_detail(job_id)
        
        task_list = ['read']
        
        task_list.append(*job['task_list']['read'])
        
        if task := job['task_list'][task_list[-1]]:
            task_list.append(*task)
        
        for task in task_list:
            task_function = getattr(task_executor, task)
            task_function(job)
