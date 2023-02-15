from opcua import Client

client = Client("opc.tcp://localhost:4840/freeopcua/server") # Initiate

try :
    # Connect to Server
    client.connect()

    # Optional if you already knew node's id
    root = client.get_root_node() 
    print(f'Root node is {root}')

    # Read node
    var = client.get_node("ns=2;i=2") 
    print(f'Read node is {var}')
    

    # Print Value
    print(f'Node : {var}')
    print(f'Value of node :{var.get_value()}') # Get and print only value of thge node
    print(f'Full value of node : {var.get_data_value()}') # Get and print full value of the node 

    # Write Value
    var.set_value(1.3) # Set value into 1.3
    print(f'New value is : {var.get_value()}') # Get and print full value of the node 

finally :
    # Disconnect when finish
    client.disconnect()