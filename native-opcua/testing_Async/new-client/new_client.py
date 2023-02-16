# Import necessary libraries
from opcua import Client, ua
import time

# Define a function to read an input value from an OPC UA server node
def read_input_value(node_id):
    # Get the node from the client
    client_node = client.get_node(node_id)
    # Read the value of the node
    client_node_value = client_node.get_value()
    # Print the value of the node
    print("Value of : " + str(client_node) + ' : ' + str(client_node_value))

# Define a function to write an integer value to an OPC UA server node
def write_value_int(node_id, value):
    # Get the node from the client
    client_node = client.get_node(node_id)
    # Set the value of the node to the input value as an integer
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)
    # Print the new value of the node
    print("Value of : " + str(client_node) + ' : ' + str(client_node_value))

# Define a function to write a boolean value to an OPC UA server node
def write_value_bool(node_id, value):
    # Get the node from the client
    client_node = client.get_node(node_id)
    # Set the value of the node to the input value as a boolean
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)
    # Print the new value of the node
    print("Value of : " + str(client_node) + ' : ' + str(client_node_value))

# The main function of the code
if __name__ == "__main__":

    # Start a timer to measure the execution time of the code
    s = time.perf_counter()
    elapsed = time.perf_counter() - s

    # Create a client object to connect to the OPC UA server
    client = Client("opc.tcp://172.16.200.141:4840")

    try:
        # Connect to the OPC UA server
        client.connect()

        # Get the root node of the server
        root = client.get_root_node()
        print("Objects root node is: ", root)

        # Read the value of a node on the server
        read_input_value('ns=3;s="Blocco_dati_1"."call_me_from_Server"')

        # Write a boolean value to a node on the server
        write_value_bool('ns=3;s="Blocco_dati_1"."call_me_from_Server"', True)

    finally:
        # Disconnect from the OPC UA server
        client.disconnect()

        # Print the execution time of the code
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")
