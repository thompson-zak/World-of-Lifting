# Postgres docker image
FROM postgres

# Create db scaffold
# TODO - need to make password configurable
ENV POSTGRES_USER lifting
ENV POSTGRES_PASSWORD placeholderPassword
ENV POSTGRES_DB lifting

# Script to initialize powerlifting table
COPY createTables.sql /docker-entrypoint-initdb.d/