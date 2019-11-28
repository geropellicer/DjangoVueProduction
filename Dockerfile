FROM python:3.6

RUN mkdir /site
WORKDIR /site

COPY ./htdocs/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY ./htdocs .