from opcua import Client

# client = Client("opc.tcp://localhost:4840/freeopcua/server") # Initiate

try:
    #look for Avaliable Server 
    client = Client("opc.tcp://")
    servers = client.find_servers_on_network()
    print(servers)


    #client.connect() # Connect to the server
    #root = client.get_root_node() 

except Exception as e:
    print(f"The code has return an error : {e}")


#finally:
    
    #client.disconnect() # Disconnect from the server