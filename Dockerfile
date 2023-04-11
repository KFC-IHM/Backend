FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py migrate
RUN python manage.py init-admin
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]