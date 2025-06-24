from opcua import Client
import time


def main():
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    client = Client(url)

    print("Connecting to server...")
    client.connect()

    try:
        root = client.get_root_node()
        uri = "http://examples.freeopcua.github.io"
        idx = client.get_namespace_index(uri)
        myvar = root.get_child(["0:Objects", f"{idx}:MyObject", f"{idx}:MyVariable"])

        while True:
            value = myvar.get_value()
            print("Current value:", value)
            time.sleep(1)
    finally:
        client.disconnect()
        print("Client disconnected")


if __name__ == "__main__":
    main()
