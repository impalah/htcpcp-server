"""

Convert poetry show --tree output to a .dot file.

Example:

fastapi 0.105.0 FastAPI framework, high performance, easy to learn, fast to code, ready for production
|-- anyio >=3.7.1,<4.0.0
|   |-- idna >=2.8 
|   `-- sniffio >=1.1 
|-- pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<2.1.0 || >2.1.0,<3.0.0
|   |-- annotated-types >=0.6.0 
|   |-- pydantic-core 2.23.4 
|   |   `-- typing-extensions >=4.6.0,<4.7.0 || >4.7.0 
|   |-- typing-extensions >=4.12.2 (circular dependency aborted here)
|   `-- typing-extensions >=4.6.1 (circular dependency aborted here)
|-- starlette >=0.27.0,<0.28.0
|   `-- anyio >=3.4.0,<5 
|       |-- idna >=2.8 
|       `-- sniffio >=1.1 
`-- typing-extensions >=4.8.0
graphviz 0.20.3 Simple Python interface for Graphviz
httpx 0.27.2 The next generation HTTP client.
|-- anyio *
|   |-- idna >=2.8 
|   `-- sniffio >=1.1 
|-- certifi *
|-- httpcore ==1.*
|   |-- certifi * 
|   `-- h11 >=0.13,<0.15 
|-- idna *
`-- sniffio *
loguru 0.7.2 Python logging made (stupidly) simple
|-- colorama >=0.3.4
`-- win32-setctime >=1.0.0
mangum 0.19.0 AWS Lambda support for ASGI applications
`-- typing-extensions *
mock 5.1.0 Rolling backport of unittest.mock for all Pythons
opentelemetry-api 1.27.0 OpenTelemetry Python API
|-- deprecated >=1.2.6
|   `-- wrapt >=1.10,<2 
`-- importlib-metadata >=6.0,<=8.4.0
    `-- zipp >=0.5 
opentelemetry-exporter-otlp 1.27.0 OpenTelemetry Collector Exporters
|-- opentelemetry-exporter-otlp-proto-grpc 1.27.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   |-- googleapis-common-protos >=1.52,<2.0 
|   |   `-- protobuf >=3.20.2,<4.21.1 || >4.21.1,<4.21.2 || >4.21.2,<4.21.3 || >4.21.3,<4.21.4 || >4.21.4,<4.21.5 || >4.21.5,<6.0.0.dev0 
|   |-- grpcio >=1.0.0,<2.0.0 
|   |-- opentelemetry-api >=1.15,<2.0 
|   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- opentelemetry-exporter-otlp-proto-common 1.27.0 
|   |   `-- opentelemetry-proto 1.27.0 
|   |       `-- protobuf >=3.19,<5.0 (circular dependency aborted here)
|   |-- opentelemetry-proto 1.27.0 (circular dependency aborted here)
|   `-- opentelemetry-sdk >=1.27.0,<1.28.0 
|       |-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|       |-- opentelemetry-semantic-conventions 0.48b0 
|       |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|       |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|       `-- typing-extensions >=3.7.4 
`-- opentelemetry-exporter-otlp-proto-http 1.27.0
    |-- deprecated >=1.2.6 
    |   `-- wrapt >=1.10,<2 
    |-- googleapis-common-protos >=1.52,<2.0 
    |   `-- protobuf >=3.20.2,<4.21.1 || >4.21.1,<4.21.2 || >4.21.2,<4.21.3 || >4.21.3,<4.21.4 || >4.21.4,<4.21.5 || >4.21.5,<6.0.0.dev0 
    |-- opentelemetry-api >=1.15,<2.0 
    |   |-- deprecated >=1.2.6 (circular dependency aborted here)
    |   `-- importlib-metadata >=6.0,<=8.4.0 
    |       `-- zipp >=0.5 
    |-- opentelemetry-exporter-otlp-proto-common 1.27.0 
    |   `-- opentelemetry-proto 1.27.0 
    |       `-- protobuf >=3.19,<5.0 (circular dependency aborted here)
    |-- opentelemetry-proto 1.27.0 (circular dependency aborted here)
    |-- opentelemetry-sdk >=1.27.0,<1.28.0 
    |   |-- opentelemetry-api 1.27.0 (circular dependency aborted here)
    |   |-- opentelemetry-semantic-conventions 0.48b0 
    |   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
    |   |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
    |   `-- typing-extensions >=3.7.4 
    `-- requests >=2.7,<3.0 
        |-- certifi >=2017.4.17 
        |-- charset-normalizer >=2,<4 
        |-- idna >=2.5,<4 
        `-- urllib3 >=1.21.1,<3 
opentelemetry-instrumentation 0.48b0 Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
|-- opentelemetry-api >=1.4,<2.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- setuptools >=16.0
`-- wrapt >=1.0.0,<2.0.0
opentelemetry-instrumentation-fastapi 0.48b0 OpenTelemetry FastAPI Instrumentation
|-- opentelemetry-api >=1.12,<2.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- opentelemetry-instrumentation 0.48b0
|   |-- opentelemetry-api >=1.4,<2.0 
|   |   |-- deprecated >=1.2.6 
|   |   |   `-- wrapt >=1.10,<2 
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- setuptools >=16.0 
|   `-- wrapt >=1.0.0,<2.0.0 (circular dependency aborted here)
|-- opentelemetry-instrumentation-asgi 0.48b0
|   |-- asgiref >=3.0,<4.0 
|   |-- opentelemetry-api >=1.12,<2.0 
|   |   |-- deprecated >=1.2.6 
|   |   |   `-- wrapt >=1.10,<2 
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- opentelemetry-instrumentation 0.48b0 
|   |   |-- opentelemetry-api >=1.4,<2.0 (circular dependency aborted here)
|   |   |-- setuptools >=16.0 
|   |   `-- wrapt >=1.0.0,<2.0.0 (circular dependency aborted here)
|   |-- opentelemetry-semantic-conventions 0.48b0 
|   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|   |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|   `-- opentelemetry-util-http 0.48b0 
|-- opentelemetry-semantic-conventions 0.48b0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- opentelemetry-api 1.27.0 
|       |-- deprecated >=1.2.6 (circular dependency aborted here)
|       `-- importlib-metadata >=6.0,<=8.4.0 
|           `-- zipp >=0.5 
`-- opentelemetry-util-http 0.48b0
opentelemetry-sdk 1.27.0 OpenTelemetry Python SDK
|-- opentelemetry-api 1.27.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- opentelemetry-semantic-conventions 0.48b0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- opentelemetry-api 1.27.0 
|       |-- deprecated >=1.2.6 (circular dependency aborted here)
|       `-- importlib-metadata >=6.0,<=8.4.0 
|           `-- zipp >=0.5 
`-- typing-extensions >=3.7.4
pydantic 2.9.2 Data validation using Python type hints
|-- annotated-types >=0.6.0
|-- pydantic-core 2.23.4
|   `-- typing-extensions >=4.6.0,<4.7.0 || >4.7.0 
|-- typing-extensions >=4.12.2
`-- typing-extensions >=4.6.1
pytest 7.4.4 pytest: simple powerful testing with Python
|-- colorama *
|-- iniconfig *
|-- packaging *
`-- pluggy >=0.12,<2.0
pytest-asyncio 0.23.8 Pytest support for asyncio
`-- pytest >=7.0.0,<9
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
pytest-cov 4.1.0 Pytest plugin for measuring coverage.
|-- coverage >=5.2.1
`-- pytest >=4.6
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
pytest-mock 3.14.0 Thin-wrapper around the mock package for easier use with pytest
`-- pytest >=6.2.5
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
svix-ksuid 0.6.2 A pure-Python KSUID implementation
`-- python-baseconv *
uvicorn 0.32.0 The lightning-fast ASGI server.
|-- click >=7.0
|   `-- colorama * 
`-- h11 >=0.8

"""

import re
import string
from typing import Dict, Generator, List, Optional, Tuple

the_data: str = """
fastapi 0.105.0 FastAPI framework, high performance, easy to learn, fast to code, ready for production
|-- anyio >=3.7.1,<4.0.0
|   |-- idna >=2.8 
|   `-- sniffio >=1.1 
|-- pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<2.1.0 || >2.1.0,<3.0.0
|   |-- annotated-types >=0.6.0 
|   |-- pydantic-core 2.23.4 
|   |   `-- typing-extensions >=4.6.0,<4.7.0 || >4.7.0 
|   |-- typing-extensions >=4.12.2 (circular dependency aborted here)
|   `-- typing-extensions >=4.6.1 (circular dependency aborted here)
|-- starlette >=0.27.0,<0.28.0
|   `-- anyio >=3.4.0,<5 
|       |-- idna >=2.8 
|       `-- sniffio >=1.1 
`-- typing-extensions >=4.8.0
graphviz 0.20.3 Simple Python interface for Graphviz
httpx 0.27.2 The next generation HTTP client.
|-- anyio *
|   |-- idna >=2.8 
|   `-- sniffio >=1.1 
|-- certifi *
|-- httpcore ==1.*
|   |-- certifi * 
|   `-- h11 >=0.13,<0.15 
|-- idna *
`-- sniffio *
loguru 0.7.2 Python logging made (stupidly) simple
|-- colorama >=0.3.4
`-- win32-setctime >=1.0.0
mangum 0.19.0 AWS Lambda support for ASGI applications
`-- typing-extensions *
mock 5.1.0 Rolling backport of unittest.mock for all Pythons
opentelemetry-api 1.27.0 OpenTelemetry Python API
|-- deprecated >=1.2.6
|   `-- wrapt >=1.10,<2 
`-- importlib-metadata >=6.0,<=8.4.0
    `-- zipp >=0.5 
opentelemetry-exporter-otlp 1.27.0 OpenTelemetry Collector Exporters
|-- opentelemetry-exporter-otlp-proto-grpc 1.27.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   |-- googleapis-common-protos >=1.52,<2.0 
|   |   `-- protobuf >=3.20.2,<4.21.1 || >4.21.1,<4.21.2 || >4.21.2,<4.21.3 || >4.21.3,<4.21.4 || >4.21.4,<4.21.5 || >4.21.5,<6.0.0.dev0 
|   |-- grpcio >=1.0.0,<2.0.0 
|   |-- opentelemetry-api >=1.15,<2.0 
|   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- opentelemetry-exporter-otlp-proto-common 1.27.0 
|   |   `-- opentelemetry-proto 1.27.0 
|   |       `-- protobuf >=3.19,<5.0 (circular dependency aborted here)
|   |-- opentelemetry-proto 1.27.0 (circular dependency aborted here)
|   `-- opentelemetry-sdk >=1.27.0,<1.28.0 
|       |-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|       |-- opentelemetry-semantic-conventions 0.48b0 
|       |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|       |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|       `-- typing-extensions >=3.7.4 
`-- opentelemetry-exporter-otlp-proto-http 1.27.0
    |-- deprecated >=1.2.6 
    |   `-- wrapt >=1.10,<2 
    |-- googleapis-common-protos >=1.52,<2.0 
    |   `-- protobuf >=3.20.2,<4.21.1 || >4.21.1,<4.21.2 || >4.21.2,<4.21.3 || >4.21.3,<4.21.4 || >4.21.4,<4.21.5 || >4.21.5,<6.0.0.dev0 
    |-- opentelemetry-api >=1.15,<2.0 
    |   |-- deprecated >=1.2.6 (circular dependency aborted here)
    |   `-- importlib-metadata >=6.0,<=8.4.0 
    |       `-- zipp >=0.5 
    |-- opentelemetry-exporter-otlp-proto-common 1.27.0 
    |   `-- opentelemetry-proto 1.27.0 
    |       `-- protobuf >=3.19,<5.0 (circular dependency aborted here)
    |-- opentelemetry-proto 1.27.0 (circular dependency aborted here)
    |-- opentelemetry-sdk >=1.27.0,<1.28.0 
    |   |-- opentelemetry-api 1.27.0 (circular dependency aborted here)
    |   |-- opentelemetry-semantic-conventions 0.48b0 
    |   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
    |   |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
    |   `-- typing-extensions >=3.7.4 
    `-- requests >=2.7,<3.0 
        |-- certifi >=2017.4.17 
        |-- charset-normalizer >=2,<4 
        |-- idna >=2.5,<4 
        `-- urllib3 >=1.21.1,<3 
opentelemetry-instrumentation 0.48b0 Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
|-- opentelemetry-api >=1.4,<2.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- setuptools >=16.0
`-- wrapt >=1.0.0,<2.0.0
opentelemetry-instrumentation-fastapi 0.48b0 OpenTelemetry FastAPI Instrumentation
|-- opentelemetry-api >=1.12,<2.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- opentelemetry-instrumentation 0.48b0
|   |-- opentelemetry-api >=1.4,<2.0 
|   |   |-- deprecated >=1.2.6 
|   |   |   `-- wrapt >=1.10,<2 
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- setuptools >=16.0 
|   `-- wrapt >=1.0.0,<2.0.0 (circular dependency aborted here)
|-- opentelemetry-instrumentation-asgi 0.48b0
|   |-- asgiref >=3.0,<4.0 
|   |-- opentelemetry-api >=1.12,<2.0 
|   |   |-- deprecated >=1.2.6 
|   |   |   `-- wrapt >=1.10,<2 
|   |   `-- importlib-metadata >=6.0,<=8.4.0 
|   |       `-- zipp >=0.5 
|   |-- opentelemetry-instrumentation 0.48b0 
|   |   |-- opentelemetry-api >=1.4,<2.0 (circular dependency aborted here)
|   |   |-- setuptools >=16.0 
|   |   `-- wrapt >=1.0.0,<2.0.0 (circular dependency aborted here)
|   |-- opentelemetry-semantic-conventions 0.48b0 
|   |   |-- deprecated >=1.2.6 (circular dependency aborted here)
|   |   `-- opentelemetry-api 1.27.0 (circular dependency aborted here)
|   `-- opentelemetry-util-http 0.48b0 
|-- opentelemetry-semantic-conventions 0.48b0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- opentelemetry-api 1.27.0 
|       |-- deprecated >=1.2.6 (circular dependency aborted here)
|       `-- importlib-metadata >=6.0,<=8.4.0 
|           `-- zipp >=0.5 
`-- opentelemetry-util-http 0.48b0
opentelemetry-sdk 1.27.0 OpenTelemetry Python SDK
|-- opentelemetry-api 1.27.0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- importlib-metadata >=6.0,<=8.4.0 
|       `-- zipp >=0.5 
|-- opentelemetry-semantic-conventions 0.48b0
|   |-- deprecated >=1.2.6 
|   |   `-- wrapt >=1.10,<2 
|   `-- opentelemetry-api 1.27.0 
|       |-- deprecated >=1.2.6 (circular dependency aborted here)
|       `-- importlib-metadata >=6.0,<=8.4.0 
|           `-- zipp >=0.5 
`-- typing-extensions >=3.7.4
pydantic 2.9.2 Data validation using Python type hints
|-- annotated-types >=0.6.0
|-- pydantic-core 2.23.4
|   `-- typing-extensions >=4.6.0,<4.7.0 || >4.7.0 
|-- typing-extensions >=4.12.2
`-- typing-extensions >=4.6.1
pytest 7.4.4 pytest: simple powerful testing with Python
|-- colorama *
|-- iniconfig *
|-- packaging *
`-- pluggy >=0.12,<2.0
pytest-asyncio 0.23.8 Pytest support for asyncio
`-- pytest >=7.0.0,<9
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
pytest-cov 4.1.0 Pytest plugin for measuring coverage.
|-- coverage >=5.2.1
`-- pytest >=4.6
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
pytest-mock 3.14.0 Thin-wrapper around the mock package for easier use with pytest
`-- pytest >=6.2.5
    |-- colorama * 
    |-- iniconfig * 
    |-- packaging * 
    `-- pluggy >=0.12,<2.0 
svix-ksuid 0.6.2 A pure-Python KSUID implementation
`-- python-baseconv *
uvicorn 0.32.0 The lightning-fast ASGI server.
|-- click >=7.0
|   `-- colorama * 
`-- h11 >=0.8
"""


def find_first_alnum_position(input_string: str) -> int:
    """Find the position os the first numeric or alphabetic character in a string.

    Args:
        input_string (str): _description_

    Returns:
        int: _description_
    """
    for index, char in enumerate(input_string):
        if char.isalnum():
            return index
    return -1


def find_first_alnum_position_regex(input_string: str) -> int:
    """Find the position os the first numeric or alphabetic character in a string usign regex (slower)

    Args:
        input_string (str): _description_

    Returns:
        int: _description_
    """
    match = re.search(r"\w", input_string)
    if match:
        return match.start()
    return -1


def extract_elements(line: str) -> Tuple[str, str, Optional[str]]:
    # Expresión regular para coincidir con el formato NOMBRE - espacio - VERSION - espacio - DESCRIPCIÓN
    match: re.Match[str] | None = re.match(r"(\S+)\s+([^\s]+)(?:\s+(.*))?", line)
    if match:
        name: str = match.group(1)
        version: str = match.group(2)
        description: str | None = match.group(3) if match.group(3) else None

        # TODO: Replace special chars

        return name, version, description
    return "", "", None


def parse_dependencies(input_string: str) -> List[str]:

    lines = input_string.splitlines()

    graph_lines = ["digraph G {"]

    # Almacenar los niveles y los nombres de los paquetes para definir relaciones
    stack = []

    for line in lines:
        # Detect if the first character is a numeric o alfabetic one
        position: int = find_first_alnum_position(line)

        if position == -1:
            # Ignore the line
            continue

        # Extract the package line and its properties
        package_line: str = line[position:]
        # print(f"Package line: {package_line}")

        name, version, description = extract_elements(package_line)
        # print(f"Name: {name}, Version: {version}, Description: {description}")

        # Determinar el nivel de indentación
        # (son 4 espacios por nivel de indentación)
        indent_level = (position + 1) / 4 if position > 0 else 0

        # Ajustar la pila de niveles
        while len(stack) > indent_level:
            stack.pop()

        # Añadir la dependencia actual y generar la relación
        if stack:
            parent_name = stack[-1]
            graph_lines.append(f'  "{parent_name}" -> "{name} {version}";')

        # Añadir el paquete actual a la pila
        stack.append(f"{name} {version}")

    graph_lines.append("}")

    return graph_lines


def parse_dependencies_v1(input_file, output_file):

    with open(input_file, "r") as infile:
        lines = infile.readlines()

    graph_lines = ["digraph G {"]

    # Almacenar los niveles y los nombres de los paquetes para definir relaciones
    stack = []

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        # Determinar el nivel de indentación usando los caracteres |-- o `--
        if stripped_line.startswith("|--") or stripped_line.startswith("`--"):
            indent_level = line.count("|   ") + line.count("`--")
            package_name = re.split(r"\s+", stripped_line[3:].strip())[0]
        else:
            indent_level = 0
            package_name = re.split(r"\s+", stripped_line)[0]

        # Ajustar la pila de niveles
        while len(stack) > indent_level:
            stack.pop()

        # Añadir la dependencia actual y generar la relación
        if stack:
            parent_name = stack[-1]
            graph_lines.append(f'  "{parent_name}" -> "{package_name}";')

        # Añadir el paquete actual a la pila
        stack.append(package_name)

    graph_lines.append("}")

    # Guardar el archivo en formato .dot
    with open(output_file, "w") as outfile:
        outfile.write("\n".join(graph_lines))


# # Ejecutar la conversión
# parse_dependencies_v1("dependencies_raw.txt", "dependencies.dot")


def letter_generator() -> Generator[str, None, None]:
    letters: str = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index: int = 0
    number: int = 0

    while True:
        if index < len(letters):
            yield letters[index] + (str(number) if number > 0 else "")
            index += 1
        else:
            index = 0
            number += 1
            yield letters[index] + str(number)
            index += 1


def export_to_mermaid(input_string: str) -> List[str]:

    lines = input_string.splitlines()

    id_dictionary: Dict[str, str] = {}

    gen: Generator[str, None, None] = letter_generator()

    # Procesar la salida para convertirla a formato Mermaid

    mermaid_lines = ["graph TD"]
    stack = []
    for line in lines:

        # Detect if the first character is a numeric o alfabetic one
        position: int = find_first_alnum_position(line)

        if position == -1:
            # Ignore the line
            continue

        # Extract the package line and its properties
        package_line: str = line[position:]
        # print(f"Package line: {package_line}")

        name, version, description = extract_elements(package_line)
        # Replace special characters on every variable
        # TODO: send to extract_elements
        name = name.replace("||", "or").replace("(", "").replace(")", "")
        version = version.replace("||", "or").replace("(", "").replace(")", "")
        description = (
            description.replace("||", "or").replace("(", "").replace(")", "")
            if description
            else None
        )

        key: str = f"{name} {version}"

        if not key in id_dictionary:
            id_dictionary[key] = (
                f"{next(gen)}[{name} {version} {description if description else ''}]"
            )

        # Determinar el nivel de indentación
        # (son 4 espacios por nivel de indentación)
        indent_level = (position + 1) / 4 if position > 0 else 0

        # Ajustar la pila de niveles
        while len(stack) > indent_level:
            stack.pop()

        # Añadir la dependencia actual y generar la relación
        if stack:
            parent_name = stack[-1]
            mermaid_lines.append(
                f"    {id_dictionary[parent_name]} --> {id_dictionary[key]}"
            )

        # Añadir el paquete actual a la pila
        stack.append(f"{name} {version}")

    return mermaid_lines


if __name__ == "__main__":

    # print("\n".join(parse_dependencies(the_data)))

    print("\n".join(export_to_mermaid(the_data)))
