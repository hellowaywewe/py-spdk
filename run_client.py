from py_spdk import pyspdk


def get_rpc_methods():
    py = pyspdk('nvme')
    if py.is_alive():
        res = py.exec_rpc('get_rpc_methods', '10.0.2.15')
        return res


get_rpc_methods()
