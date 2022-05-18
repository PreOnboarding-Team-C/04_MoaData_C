import json
from typing import Optional

import pandas as pd
from pandas.core.frame import DataFrame


class JobExecutor:
    """
    Assignee : 김수빈
    Reviewer : -
    """
    FILE_PATH = './job.json'

    def __init__(self, requested_job: Optional[dict]=None):
        self._jdf = self._get_json()
        if requested_job:
            # sample job 참고
            self._requested_job = requested_job
            self._ids = list(map(lambda x: int(x['job_id']), self._requested_job))

    def _get_json(self):
        with open(self.FILE_PATH, 'r') as f:
            jdf = json.load(f)
        return jdf

    def save_json(self):
        pass

    def delete_json(self):
        pass
    
    def update_json(self):
        pass

    def excute_job(self):
        # 상속과 인자로 설정하는 부분에서 고민 중
        jobflow = CSVExecutor(self.job, self.job['task_list'].keys()[0])
        
        # read > drop > write의 flow만 존재한다고 가정
        jobflow.task_step = self.job['task_list'].items()[0]
        jobflow.task = jobflow.task_step

        jobflow.DF = jobflow.drop()
        
        jobflow.task_step = self.job['task_list'].items()[1]
        jobflow.task = jobflow.task_step

        jobflow.write()


class CSVExecutor:
    """
    Assignee : 김수빈
    Reviewer : -
    """
    def __init__(self, job, start_task):
        # node :: start_task: read > update next step using property > end_task: write
        self.job = job
        self._task_step = start_task    # 'read'
        self._task = self.job['property'][self._task_step]
        # init dataframe :: read
        self.DF = eval(f"self.{self._task_step}")

    @property
    def task_step(self):
        return self.task_step

    @task_step.setter
    def task_step(self, next_step):
        self._task_step = next_step

    @property
    def task(self):
        return self.task

    @task.setter
    def task(self, task_step):
        self._task = self.job['property'][task_step]
    
    def read(self):
        DF = pd.read_csv(self._task['filename'], sep=self._task['sep'])
        return DF

    def drop(self):
        # should be func(read)'s next step
        self.DF = self.DF.drop(columns=self._task)
        return self.DF

    def write(self):
        # always allowed as end step
        self.DF.to_csv(self._task['filename'], sep=self._task['sep'], encoding='utf-8', index=False)
