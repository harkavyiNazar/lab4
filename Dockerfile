FROM python:3.12-slim
WORKDIR /app
COPY . /app/
RUN pip install googletrans==3.1.0a0
ENV PYTHONPATH=/app
CMD ["/bin/bash"]