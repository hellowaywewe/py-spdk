from py_spdk import pyspdk

print "=====================get_vhost_blk_controllers=============="
def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_vhost_blk_controllers', '127.0.0.1')
        return val

cal=run_client()
print cal

print "=====================get_vhost_blk_controllers=============="

def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_vhost_blk_controllers', '127.0.0.1')
        return val

cal=run_client()
print cal

print "=====================get_vhost_scsi_controllers============="


def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_vhost_scsi_controllers', '127.0.0.1')
        return val

cal=run_client()
print cal

print "======================get_scsi_devices======================"


def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_scsi_devices', '127.0.0.1')
        return val

cal=run_client()
print cal

print "=======================get_luns=============================="

def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_luns', '127.0.0.1')
        return val

cal=run_client()
print cal

print "====================get_interfaces=========================="

def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_interfaces', '127.0.0.1')
        return val

cal=run_client()
print cal

print "===================get_trace_flags=========================="

def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_trace_flags', '127.0.0.1')
        return val

cal=run_client()
print cal

print "====================get_bdevs========================="

def run_client():
    py = pyspdk('nvme')
    if py.is_alive():
        val =  py.exec_rpc('get_bdevs', '127.0.0.1')
        return val

cal=run_client()
print cal