FROM python:3.12 AS requirements-stage

ARG package_name=htcpcp
ARG module_name=htcpcp

# Create structure and install poetry
WORKDIR /tmp
RUN mkdir projects
RUN pip install poetry

# Build requirements
COPY ./pyproject.toml ./poetry.lock* ./projects/${package_name}/
RUN cd projects/${package_name} && poetry export -f requirements.txt --output requirements.txt --without-hashes

# ---------------------------------

# Build execution container
FROM python:3.12-alpine

# ARGs are needed in all the stages
ARG package_name=htcpcp
ARG module_name=htcpcp

# Install additional libraries
RUN apk add --no-cache gcc musl-dev curl-dev

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup


ENV PORT=8000

EXPOSE 8000/tcp
EXPOSE 80/tcp

WORKDIR /app

# Install requirements
COPY --from=requirements-stage /tmp/projects/${package_name}/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app

# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser


CMD ["sh", "-c", "uvicorn htcpcp.main:app --host 0.0.0.0 --port $PORT"]
