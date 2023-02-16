This class has a constructor method that takes in two arguments, server_url and node_id, which initialize the server_url and node_id attributes of the class instance.

The connect method initializes a connection to the OPC UA server using the server_url attribute. The disconnect method disconnects from the server if the client is connected.

The read_input_value, write_value_int, and write_value_bool methods are similar to the functions we defined earlier, except that they now use the client object that is initialized by the connect method.

Finally, the read_and_print_value method uses the read_input_value method to read the value of the node specified by node_id and prints the result to the console.