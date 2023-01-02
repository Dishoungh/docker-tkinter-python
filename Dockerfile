FROM ubuntu:20.04
RUN apt update
RUN echo "37" | apt install firefox python python3 python3-tk -y

WORKDIR /home/

COPY script.py ./

CMD ["python3", "./script.py"]



