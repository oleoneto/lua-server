FROM postgres:10.5-alpine
COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
