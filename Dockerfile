FROM frolvlad/alpine-miniconda3:latest

COPY . /home
WORKDIR /home

RUN pip install --no-cache dash\
    pip install --no-cache sklearn\
    pip install --no-cache plotly\
    pip install --no-cache pandas\
    pip install --no-cache numpy\
    pip install --no-cache xlrd

CMD python app.py -h 0.0.0.0 -p $PORT