FROM python:3.10

WORKDIR /project_drf

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver"]
