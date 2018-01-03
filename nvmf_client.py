import json
import spdk_pb2
import pbjson
from py_spdk import pyspdk


def get_rpc_methods():
    py = pyspdk('nvme')
    if py.is_alive():
        res =  py.exec_rpc('get_rpc_methods', '10.0.2.15')
        json_obj = json.loads(res)
        proto_obj = spdk_pb2.RpcMethods().name
        for name_i in range(len(json_obj)):
	    proto_obj.append(json_obj[name_i])
        return proto_obj


def get_bdevs():
    py = pyspdk('nvme')
    if py.is_alive():
        block_devices = spdk_pb2.BlockDevices().blockDevice
	block_device = spdk_pb2.BlockDevice()
	block_devices= get_proto_objs(py, 'get_bdevs', '127.0.0.1', block_devices, block_device)
        print type(block_devices)
	return block_devices


def get_nvmf_subsystems():
    py = pyspdk('vhost')
    if py.is_alive():
        subsystems = spdk_pb2.NVMFSubsystems().subsystem
	subsystem = spdk_pb2.NVMFSubsystem()


def get_proto_objs(py, method, server_ip, proto_objs, proto_obj): 
    res = py.exec_rpc(method, server_ip)
    json_obj = json.loads(res)
    for list_i in range(len(json_obj)):
        proto_obj = pbjson.dict2pb(proto_obj, json_obj[list_i])
        proto_objs.extend([proto_obj])
    return proto_objs
    

my_obj = get_rpc_methods()
for index in range(len(my_obj)):
    print my_obj[index]

"""
my_obj = get_bdevs()
for index in range(len(my_obj)):
    obj = my_obj[index]
    if(index == 0):
        print obj.supported_io_types.nvme_admin
"""
"""
my_obj = get_nvmf_subsystems()
for index in range(len(my_obj)):
    obj = my_obj[index]
    print obj
"""
