FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8080

COPY main.py main.py

CMD ["python3", "main.py"]