FROM python:latest
WORKDIR /mongo-seed

# install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get -y install python3.7


RUN pip3 install pymongo
RUN pip3 install json-lines

COPY garment_items.jl garment_items.jl
COPY create_fixtures.py create_fixtures.py


CMD ["python3", "create_fixtures.py"]