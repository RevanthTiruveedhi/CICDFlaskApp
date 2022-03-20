from mysql:5.6

ARG DEBIAN_FRONTEND=noninteractive

ENV MYSQL_DATABASE employeeusers

COPY ./sql-scripts/ /docker-entrypoint-initdb.d/