from opcua import Client
import asyncio
import time

from opcua import Client, ua

class OPCUAClient:
    
    def __init__(self, server_url, node_id):
        self.server_url = server_url
        self.node_id = node_id
        self.client = None

    async def connect(self):
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
        return client_node_value



async def main():
        
    # Define the url of the server and the node id to look for
    url_OpcUa_Server = 'opc.tcp://172.16.200.141:4840'
    search_for_NodeId = 'ns=3;s="Blocco_dati_1"."call_me_from_Server"'

    new_client = OPCUAClient(url_OpcUa_Server, search_for_NodeId)

    try:
        await asyncio.gather(new_client.connect())
        value = new_client.read_and_print_value()
        #new_client.write_value_bool(True)
        new_client.write_value_bool(False)
            
    except Exception as e:
        print(f'Exception during client session : {e}')

    finally :
        # Disconnect when finish
        new_client.disconnect()
        print(f'Client session successfully closed')



if __name__ == '__main__':

    import time

    #Start Counting execution time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
