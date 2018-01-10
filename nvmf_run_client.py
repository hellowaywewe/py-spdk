from nvmf_client import NvmfTgt
from py_spdk import pyspdk


py = pyspdk('nvme')
if py.is_alive():
    nvmf_tgt = NvmfTgt(py)

    my_obj = nvmf_tgt.get_rpc_methods()
    for index in range(len(my_obj)):
        print my_obj[index]

    my_bdevs = nvmf_tgt.get_bdevs()
    for index in range(len(my_bdevs)):
        my_bdev = my_bdevs[index]
        if(index == 0):
            print my_bdev.supported_io_types.nvme_admin

    my_nvmfs = nvmf_tgt.get_nvmf_subsystems()
    for index in range(len(my_nvmfs)):
        my_nvmf = my_nvmfs[index]
        print my_nvmf

    dele = nvmf_tgt.delete_bdev('Malloc7')
else:
    raise Exception('nvmf_tgt server is unalive.')

