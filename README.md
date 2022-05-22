# MoaData

## 1. 가상환경 설치 및 실행
```shell
# virtualvenv 설치
> sudo pip install virtualenv

# 가상환경을 위한 디렉토리
> python3 -m virtualenv [디렉토리명]

# 또는
> virtualenv -p python3 [디렉토리명]

# 가상환경 활성화
> source [디렉토리명]/bin/activate

# django 프레임워크 설치
> pip3 install django

# 가상환경 비활성화
> deactivate

# 패키지 목록 출력
> pip freeze

# 패키지 목록을 requirements.txt에 저장
> pip freeze > requirements.txt
```

## 2. Task 및 작업 분담
```py
1. read - path/to/a.csv를 읽어서 pandas data frame으로 리턴하는 동작을 수행
2. drop - “column_name”: “date” / a.csv 안의 컬럼네임 date가 있다는 가정하에 이것을 drop시킨다. 
   drop시킨 후 data frame을 리턴하는게 drop의 역할
3. write - (read-drop한 결과를) path/to/b.csv로 저장한다.
-------------------------------------------------------------------------------------------
# 어려운 점
1. db에서 하던 작업을 csv파일하고 json 파일로만 해야됨 
2. pandas를 이용해서 리턴해야 됨
3. 결과물 DFD, Sequence Diagram
-------------------------------------------------------------------------------------------
# 작업
1. DFD (우경)
2. Sequence Diagram (은비)
3. json 파일 저장, 수정, 삭제 (병수)
4. json 파일 실행
```

## 3. Sequence diagram
![img](./src/images/moadata_sequence_diagram.png "Sequence Diagram")

## 4. API 명세서
| 기능 | method | url | 비고 |
|------|---|---| --- |
| 전체 job_id 읽기 | GET | http://127.0.0.1:8000/api/v1/jobs | - |
| 특정 job_id 생성  | POST | http://127.0.0.1:8000/api/v1/jobs | - |
| 특정 job_id 읽기  | GET | http://127.0.0.1:8000/api/v1/jobs/<int:job_id> | - |
| 특정 job_id 수정  | PATCH | http://127.0.0.1:8000/api/v1/jobs/<int:job_id> | - |
| 특정 job_id 삭제  | DELETE | http://127.0.0.1:8000/api/v1/jobs/<int:job_id> | - |
| 특정 job_id 수행  | GET | http://127.0.0.1:8000/api/v1/jobs/<int:job_id>/run | - |
