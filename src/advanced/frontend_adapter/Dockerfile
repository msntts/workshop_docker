FROM python:3

RUN pip install Flask && mkdir /work

ADD src/frontend_adapter.py /work

CMD ["python", "/work/frontend_adapter.py"]
