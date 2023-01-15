FROM python:3.10.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV CONTRACT=""
ENV DAY="0"
ENV MONTH="0"
ENV YEAR="0"
ENV RANGE="0"
ENV PG_HOST=""
ENV PG_PORT="0"
ENV PG_USER=""
ENV PG_PASSWORD=""
ENV PG_DB=""

ENTRYPOINT python main.py --contract=${CONTRACT:-""} --day=${DAY:-"0"} --month=${MONTH:-"0"} \
--year=${YEAR:-"0"} --range=${RANGE:-"0"} --pg_host=${PG_HOST:-""} \
--pg_port=${PG_PORT:-"0"} --pg_user=${PG_USER:-""} --pg_password=${PG_PASSWORD:-""} --pg_db=${PG_DB:-""}