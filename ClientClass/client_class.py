from opcua import Client, ua
import asyncio
import time

# write_NodeId = 'ns=3;s="Data_Exange"."Call_Me_From_Server"'

class OPCUAClient:
    
    def __init__(self, server_url):
        self.server_url = server_url
        self.node_id = None 
        self.client = None

    def connect(self):
        self.client = Client(self.server_url)
        print("Connected to OPC UA server in Url: {self.server_url}".format(self=self))
        self.client.connect()

    def disconnect(self):

        if self.client is not None:
            self.client.disconnect()

    def read_input_value(self):

        if self.client is None:
            raise ValueError("Client is not connected.")
        client_node = self.client.get_node(self.node_id)
        client_node_value = client_node.get_value()
        return client_node_value

    def write_value_int(self, value):

        if self.client is None:
            raise ValueError("Client is not connected.")
        client_node = self.client.get_node(self.node_id)
        client_node_value = value
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Int16))
        client_node.set_value(client_node_dv)

    def write_value_bool(self, value):

        if self.client is None:
            raise ValueError("Client is not connected.")
        client_node = self.client.get_node(self.node_id)
        client_node_value = value
        client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Boolean))
        client_node.set_value(client_node_dv)

    def read_and_print_value(self):
        
        if self.client is None:
            raise ValueError("Client is not connected.")
        client_node_value = self.read_input_value()
        print(f"Value of : {str(self.node_id)}' : ' {str(client_node_value)}")


async def main():
    # Define the url of the server and the node id to look for

    # This Variables can be Input by the User 

    url_OpcUa_Server = 'opc.tcp://172.16.200.141:4840'
    read_NodeId = 'ns=3;s="Data_Exange"."Count_Status"'

    new_client = OPCUAClient(url_OpcUa_Server)

    try:
        await asyncio.gather(new_client.connect())
        
    except Exception as e:
        print(f'Exception during client session : {e}')

    finally :
        # Disconnect when finish
        new_client.disconnect()
        print(f'Client session successfully closed')

if __name__ == '__main__':

    #Start Counting execution time
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

