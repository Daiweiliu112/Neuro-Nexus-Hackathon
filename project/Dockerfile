# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 and Pillow dependencies
#RUN apk update \
#    && apk add --virtual build-deps gcc python3-dev musl-dev \
#    && apk add postgresql \
#    && apk add postgresql-dev \
#    && pip install psycopg2 \
#    && apk del build-deps
#    && apk add jpeg-dev \ zlib-dev \libjpeg \
#    && pip install Pillow

RUN apk update
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
RUN apk add --no-cache --virtual gdal-bin 
# RUN apk add --no-cache --virtual libpq-dev python-dev
# RUN apk add --no-cache --virtual postgresql postgresql-contrib
RUN apk add postgresql-dev gcc python3-dev musl-dev
#gdal-bin python-gdal python3-gdal
# python3-gdal
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
# RUN gdal --version 
 # to see what version of GDAL you have
# RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
# RUN export C_INCLUDE_PATH=/usr/include/gdal

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

EXPOSE 8000

EXPOSE 5432

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "t4tt.wsgi:application"]
