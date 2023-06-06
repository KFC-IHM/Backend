FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

EXPOSE 8000
CMD ["./entrypoint.sh"]