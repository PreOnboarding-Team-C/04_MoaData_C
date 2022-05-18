import json
import pandas as pd


class JobExecutor:
    FILE_PATH = './job.json'

    def _read_all_job(self, id=None):
        with open(self.FILE_PATH, 'r') as file:
            job_list = json.load(file)

            if id:
                for job in job_list:
                    if int(job['job_id']) == int(id):
                        return job
            else:
                return job_list

        if id:
            raise Exception(f'404 : There is no Job id [{id}]')

    def _read_job(self, job_id):
        return self._read_all_job(job_id)

    def _write_to_csv(self, job):
        with open(self.FILE_PATH, 'w') as file:
            json.dump(job, file, indent=4)

    def _get_index(self, job_list, id):
        for idx, job in enumerate(job_list):
            if int(job['job_id']) == int(id):
                return idx

        raise Exception(f'404 : There is no Job id [{id}]')

    # 현재 존재하는 job_id 인지 판별
    def _exist_or_not(self, job_list, id):
        for job in job_list:
            if int(job['job_id']) == int(id):
                return False
        return True

    def read(self, id=None):
        return self._read_job(id)

    def create(self, input_job):
        job_list = self._read_all_job()
        if self._exist_or_not(job_list, input_job['job_id']):
            job_list.append(input_job)
            self._write_json(job_list)
        else:
            return "이미 존재하는 job_id 입니다."

    def edit(self, job_id, input_job):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, job_id)

        job_list.insert(job_index, input_job)

        self._write_to_csv(job_list)

    def delete(self, job_id):
        job_list = self._read_all_job()
        job_index = self._get_index(job_list, job_id)

        job_list.pop(job_index)

        self._write_to_csv(job_list)

    # Job Task excute functions

    def run(self, task, id=None, job=False, task_excutor=None):
        print('Run Task: ', task)
        if not job:
            job = self._read_job(id)

        if not task_excutor:
            task_excutor = TaskExecutor()

        # Case 1
        if task.lower() == 'read':
            task_excutor.read(job)
        elif task.lower() == 'drop':
            task_excutor.drop(job)
        elif task.lower() == 'write':
            task_excutor.write(job)

        # # Case 2
        # task_fucntion = getattr(task_excutor, task.lower())
        # task_fucntion(job)

        next_tasks = job['task_list'].get(task, [])
        next_tasks = ["drop"]
        for task in next_tasks:
            self.run(task, id=None, job=job, task_excutor=task_excutor)



class TaskExecutor:
    DF = None

    def read(self, job):
        task = job['property']['read']
        self.DF = pd.read_csv(task['filename'], delimiter=task['sep'])
        return self.DF

    def read2(self, job):
        self.read(22)

    def drop(self, job):
        task = job['property']['drop']
        self.DF = self.DF.drop(task['column_name'], axis=1)
        return self.DF

    def write(self, job):
        task = job['property']['write']
        self.DF.to_csv(task['filename'], sep=task['sep'], index=False)