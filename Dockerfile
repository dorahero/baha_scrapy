FROM python:3.6
COPY . /baha
WORKDIR /baha
RUN pip install -r requirements.txt
ENTRYPOINT [ "scrapy" ]
CMD []