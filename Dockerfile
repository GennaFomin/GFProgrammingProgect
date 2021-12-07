FROM python:3.9

WORKDIR /project1
COPY . .

RUN pip install -r requierments.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
