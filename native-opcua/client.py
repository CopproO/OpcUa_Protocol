from opcua import Client
import asyncio
import time

async def runClient(url: str, NodeId: str, **kwargs): 
    
    client = Client(url) # Initiate
    try :
        # Connect to Server
        client.connect()

        root = client.get_root_node()
        #print("Objects node is: ", root)
    except Exception as e:
        print(f'Exception during client session : {e}')

    finally :
        # Disconnect when finish
        client.disconnect()
        print(f'Client session successfully closed')


async def main():
        
    # Define the url of the server and the node id to look for
    url_OpcUa_Server = 'opc.tcp://172.16.200.141:4840'
    serach_for_NodeId = "ns=3;s='Blocco_dati_1'.'call_me_from_Server'"

    await asyncio.gather(runClient(url_OpcUa_Server, serach_for_NodeId))


if __name__ == '__main__':

    import time

    #Start Counting execution time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
