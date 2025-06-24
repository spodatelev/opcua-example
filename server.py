from opcua import ua, Server
from random import random
import time


def main():
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    objects = server.get_objects_node()
    myobj = objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 0.0)
    myvar.set_writable()

    print("Starting OPC UA server...")
    server.start()
    try:
        while True:
            value = random()
            myvar.set_value(value)
            print("Updated variable to", value)
            time.sleep(1)
    finally:
        server.stop()
        print("Server stopped")


if __name__ == "__main__":
    main()
