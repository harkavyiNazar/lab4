FROM python:3.12-slim
WORKDIR /harkavyi
COPY . /harkavyi/
RUN pip install googletrans==3.1.0a0
CMD ["/bin/bash"]