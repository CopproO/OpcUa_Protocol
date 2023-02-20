import asyncio
import logging
import random

from asyncua import Server, ua
from asyncua.common.methods import uamethod


@uamethod
def func(parent, value):
    return value * 2

async def main():
    _logger = logging.getLogger(__name__)
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # set up our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    main = await server.nodes.objects.add_object(idx, "Mainect")
    const_variable = await main.add_variable(idx, "Const_Value", 6.7)

    int_value_1 = await main.add_variable(idx, "Integer_1_Value", random.randint(0,200))

    int_value_2 = await main.add_variable(idx, "Integer_2_Value", random.randint(100,200))


    
    # Set const_variableiable to be writable by clients
    await const_variable.set_writable()
    await int_value_1.set_writable()
    await int_value_2.set_writable()



    await server.nodes.objects.add_method(
        ua.NodeId("ServerMethod", idx),
        ua.QualifiedName("ServerMethod", idx),
        func,
        [ua.VariantType.Int64],
        [ua.VariantType.Int64],
    )

    _logger.info("Starting server!")
    async with server:
        while True:
            await asyncio.sleep(1)
            new_val = await const_variable.get_value() + 0.1
            _logger.info("Set value of %s to %.1f", const_variable, new_val)
            await const_variable.write_value(new_val)
            await int_value_1.write_value(int(100*(random.randint(100,  200))))
            await int_value_2.write_value(int(100*(random.randint(200, 300))))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)
   