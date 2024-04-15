FROM pinning-service-base AS base

WORKDIR /app

# Creating folders, and files for a project:
COPY ./indexer /app/indexer

CMD python -m indexer.main