from opcua import Client, ua
import time

# write_NodeId = 'ns=3;s="Data_Exange"."Call_Me_From_Server"'

class OPCUAClient:
    
    def __init__(self, server_url:str, read_node:str = None, write_node:str = None):
        self.server_url = server_url
        self.read_node = read_node
        self.write_node = write_node
        self.client = None

    def get_read_node(self, id):
        self.read_node = id 


    def connect(self):
        self.client = Client(self.server_url)
        self.client.connect()
        print(f"Connected to OPC UA server in Url: {self.server_url}")
        
    
    def disconnect(self):

        if self.client is not None:
            self.client.disconnect()

    def read_input_value(self):

        if self.client is None:
            raise ValueError("Client is not connected.")

        client_node = self.client.get_node(self.read_node)
        client_node_value = client_node.get_value()
        return client_node_value

    def write_value_int(self):

        if self.client is None:
            raise ValueError("Client is not connected.")

        client_node = self.client.get_node(self.read_node)
        client_node_value = self.write_node
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
        client_node.set_value(client_node_dv)

    def write_value_bool(self):

        if self.client is None:
            raise ValueError("Client is not connected.")

        client_node = self.client.get_node(self.read_node)
        client_node_value = self.write_node
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
        client_node.set_value(client_node_dv)

    def read_and_print_value(self):
        
        if self.client is None:
            raise ValueError("Client is not connected.")

        client_node_value = self.read_input_value()
        print(f"Value of : {str(self.read_node)}' : ' {str(client_node_value)}")


def main():
    # Define the url of the server and the node id to look for

    # This Variables can be Input by the User 

    url_OpcUa_Server = 'opc.tcp://localhost:4840/freeopcua/server/'
    read_NodeId_1 = 'ns=2;i=3'
    read_NodeId_2 = 'ns=2;i=4'

    new_client = OPCUAClient(url_OpcUa_Server)

    new_client.connect()
    elapsed = time.perf_counter() - s
    
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    while True:
        time.sleep(1)
        new_client.read_node = read_NodeId_1
        new_client.read_and_print_value()
        new_client.read_node = read_NodeId_2
        new_client.read_and_print_value()


if __name__ == '__main__':

    #Start Counting execution time
    s = time.perf_counter()
    main()