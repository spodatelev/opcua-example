# OPC UA Example

This repository contains a very basic example of an OPC‑UA server and client implemented in Python using the `opcua` library.

## Prerequisites

- Python 3.10+ (the environment here uses Python 3.12)
- `pip install opcua`

## Running the server

```
python server.py
```

The server exposes an endpoint at `opc.tcp://0.0.0.0:4840/freeopcua/server/` and updates a variable named `MyVariable` every second.

## Running the client

In a separate terminal, run:

```
python client.py
```

The client connects to the server and prints the current value of `MyVariable` once per second.
