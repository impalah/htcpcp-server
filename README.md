# htcpcp-server

HTCPCP Protocol implementation with some juicy extra additions, based on RFC 2324: [https://www.rfc-editor.org/rfc/rfc2324]

## Technology Stack:

- FastAPI
- Uvicorn (server)
- Pytest (\*)

## Development environment

### Requirements:

- Docker CE (Linux) or Docker Desktop (MacOS, Windows).
- Python >= 3.12 (Pyenv, best option)
- Poetry as dependency manager

### Activate development environment

```bash
poetry install
```

This will create a new virtual environment (if it does not exists) and will install all the dependencies.

To activate the virtual environment use:

```bash
poetry shell
```

### Add/remove dependencies

Add dependency to the given group. If not specified will be added to the default group.

```bash
poetry add PIP_PACKAGE [-G group.name]
```

Remove dependency from the given group

```bash
poetry remove PIP_PACKAGE [-G group.name]
```


### Run project from command line


```bash
cd src/web_api_template
poetry run python -m uvicorn main:app --reload --port 8000
```

### Debug project from VS Code

First create a .env file in the root folder or copy the existing .env.example.

Then use the Launch option from Visual Studio Code

## Tests

### Debug From VS Code

Get the path of the virtual environment created by poetry:

```bash
poetry env info -p
```

Set in visual studio code the default interpreter to the virtual environment created by poetry.(SHIT+CTRL+P Select interpreter)

Launch "Pytest launch" from the run/debug tab.

You can set breakpoints and inspections

### Launch tests from command line

```bash
poetry run pytest --cov-report term-missing --cov=web_api_template ./tests
```

This will launch tests and creates a code coverage report.

### Exclude code from coverage

When you need to exclude code from the code coverage report set, in the lines or function to be excluded, the line:

```python
# pragma: no cover
```

See: https://coverage.readthedocs.io/en/6.4.4/excluding.html

## Docker build and run

### Build

From root directory execute:

```bash
docker build -f ./Dockerfile -t htcpcp-server .
```

### Run

From root directory execute:

```bash
docker run -d --name htcpcp-server -p 8000:8000 -e MY_VARIABLE='some value' htcpcp-server
```


## Development support services

### OpenTelemetry

From root directory execute:

```bash
docker-compose -f docker-compose-dev.yaml up -d
```

OR

Use -p flag to specify an alternative project name instead of the directory name. This is useful if you have multiple projects running on a single host.

```bash
docker-compose -f docker-compose-dev.yaml -p my-htcpcp up -d
```

### Stop

From root directory execute:

```bash
docker-compose -f docker-compose-dev.yaml down
```

OR

Use -p flag to specify an alternative project name instead of the directory name. This is useful if you have multiple projects running on a single host.

```bash
docker-compose -f docker-compose-dev.yaml -p my-htcpcp down
```

## Complete Development services

Start databases and API services in one go.

### Start

From root directory execute:

```bash
docker-compose -f docker-compose.yaml up -d
```

OR

Use -p flag to specify an alternative project name instead of the directory name. This is useful if you have multiple projects running on a single host.

```bash
docker-compose -f docker-compose.yaml -p my-htcpcp up -d
```

### Start rebuilding images

From root directory execute:

```bash
docker-compose -f docker-compose.yaml up -d --build
```

### Stop

From root directory execute:

```bash
docker-compose -f docker-compose.yaml down
```

OR

Use -p flag to specify an alternative project name instead of the directory name. This is useful if you have multiple projects running on a single host.

```bash
docker-compose -f docker-compose.yaml -p my-htcpcp down
```


## Additional help

### Opentelemetry install

```bash
poetry add opentelemetry-api
poetry add opentelemetry-sdk
poetry add opentelemetry-instrumentation
poetry add opentelemetry-exporter-otlp
poetry add opentelemetry-instrumentation-fastapi
```

