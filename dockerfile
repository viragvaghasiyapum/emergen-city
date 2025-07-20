FROM apache/spark:3.5.0

USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-pip python3-dev gcc g++ curl netcat

RUN pip3 install --upgrade pip
RUN pip3 install \
    pyspark==3.5.0 \
    pandas \
    geopandas \
    shapely \
    psycopg2-binary \
    elasticsearch \
    requests

# Set working directory
WORKDIR /app
COPY . /app

# Default: run main ETL script
CMD ["python3", "main.py"]
