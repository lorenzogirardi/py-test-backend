FROM python:3.9-alpine
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install -r requirements.txt
RUN opentelemetry-bootstrap -a install
#ENTRYPOINT ["python"]
#CMD ["app.py"]
CMD ["opentelemetry-instrument", "--traces_exporter", "console", "--metrics_exporter", "console", "flask", "run"]
