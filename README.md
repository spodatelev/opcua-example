# OPC UA Example

This repository contains a very basic example of an OPC‑UA server and client implemented in Python using the `opcua` library.

## Prerequisites

- Python 3.10+ (the environment here uses Python 3.12)
- `pip install uv` (for the fast `uv` package manager)

## Setup

Install the dependencies using [uv](https://github.com/astral-sh/uv):

```bash
uv pip install -r requirements.txt
```

## Running the server

```
uv run python server.py
```

The server exposes an endpoint at `opc.tcp://0.0.0.0:4840/freeopcua/server/` and updates a variable named `MyVariable` every second.

## Running the client

In a separate terminal, run:

```
uv run python client.py
```

The client connects to the server and prints the current value of `MyVariable` once per second.
