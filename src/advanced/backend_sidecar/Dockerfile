FROM python:3

RUN pip install Flask && mkdir /work

ADD src/backend_sidecar.py /work

CMD ["python", "/work/backend_sidecar.py"]
