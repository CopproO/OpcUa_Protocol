from opcua import Client, ua
import time

#write_NodeId = 'ns=3;s="Data_Exange"."Call_Me_From_Server"'

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
        return self.client
        
    
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
        return client_node_value


def main():
    # Define the url of the server and the node id to look for

    # This Variables can be Input by the User 

    url_OpcUa_Server = 'opc.tcp://192.168.16.200:4840'

    new_client = OPCUAClient(url_OpcUa_Server)

    new_client.connect()
    elapsed = time.perf_counter() - s
    
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    increment = 0

    while True:
        read_NodeId_2 = f'ns=3;s="Data"."Random_Number_Db"' #[{increment}]
        time.sleep(1)
        new_client.read_node = read_NodeId_2
        this_data = new_client.read_and_print_value()
        print(type(this_data))
        increment +=1
        if increment > 1:
            new_client.disconnect()
            break

    print(this_data)
if __name__ == '__main__':

    #Start Counting execution time
    s = time.perf_counter()
    main()