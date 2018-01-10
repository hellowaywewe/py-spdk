from py_spdk import pyspdk
from vhost_client import VhostTgt


py = pyspdk('vhost')
if py.is_alive():
    vhost_tgt = VhostTgt(py)

    my_obj = vhost_tgt.get_rpc_methods()
    for index in range(len(my_obj)):
        print my_obj[index]

    my_bdevs = vhost_tgt.get_bdevs()
    for index in range(len(my_bdevs)):
        my_bdev = my_bdevs[index]
        if(index == 0):
            print my_bdev.supported_io_types.nvme_admin

    my_interfaces = vhost_tgt.get_interfaces()
    for index in range(len(my_interfaces)):
        my_interface = my_interfaces[index]
        print my_interface

    dele = vhost_tgt.delete_bdev('Malloc2')
else:
    raise Exception('vhost_tgt server is unalive.')


