FROM python:3

RUN pip install Flask && mkdir /work

ADD src/frontend_sidecar.py /work

CMD ["python", "/work/frontend_sidecar.py"]
