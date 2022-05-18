import json


class JobInfo:
    JOB_PATH = './job.json'
    print('start')

    # job_id 전달 받으면 해당 값 체크 후 리턴
    # 전달 받은 job_id 값 자체가 없다면 전체 리스트 리턴 
    def read_all_jobs(self, job_id=None):
        with open(self.JOB_PATH, 'r') as file:
            jobs = json.load(file)
            if job_id:
                for job in jobs:
                    if job['job_id'] == job_id:
                        print(job)
                        return job
                print(f'There is no job_id({job_id}) in job list.')
                return f'There is no {job_id} in job list.'
            print(jobs)
            return jobs

    # 특정 job_id 데이터 리턴
    def read_job_info(self, job_id):
        self.read_all_jobs(job_id)

    # 전달 받은 job_list를 job.json에 입력 후 저장
    def write_job(self, job_list):
        with open(self.JOB_PATH, 'w') as file:
            json.dump(job_list, file, indent='\t')
    
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

    # job_id에 해당하는 job 데이터 삭제 후 저장    
    def delete(self, job_id):
        job_list = self.read_all_jobs()
        
        job_index = self.get_index(job_list, job_id)
        del job_list[job_index]
        
        self.write_job(job_list)

    
            
job = JobInfo()
job_info = {'job_id': 3, 'job_name': 'Job3', 'task_list': {'read': ['drop'], 'drop': ['write'], 'write': []}, 'property': {'read': {'task_name': 'read', 'filename': 'a.csv', 'sep': ','}, 'drop': {'task_name': 'drop', 'column_name': 'date'}, 'write': {'task_name': 'write', 'filename': 'b.csv', 'sep': ','}}}
job_id = 2

# job.read_all_jobs()
# job.read_job_info(job_id)
# job.create(job_info)
# job.update_job(job_info)
# job.delete(job_id)
