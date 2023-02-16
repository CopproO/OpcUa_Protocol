from opcua import Client, ua

class OPCUAClient:
    
    def __init__(self, server_url, node_id):
        self.server_url = server_url
        self.node_id = node_id
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


opc_url = "opc.tcp://172.16.200.141:4840"
opc_node = 'ns=3;s="Blocco_dati_1"."call_me_from_Server"' 

#ns=3;s="Blocco_dati_1"."reponce_from_serevr"
client = OPCUAClient(opc_url, opc_node)

try:
    client.connect()
    client.read_input_value()
    
except Exception as e:
    print(e)

finally:
    client.disconnect()




