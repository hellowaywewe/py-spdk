import os
import subprocess
from py_spdk import pyspdk


def start_server(py, spdk_dir, server_name):
    if py.is_alive():
        py.init_hugepages(spdk_dir)
        server_dir = os.path.join(spdk_dir, 'app/')
        file_dir = py.search_file(server_dir, server_name)
        print file_dir
        os.chdir(file_dir)
        p = subprocess.Popen(
            'sudo ./%s' % server_name,
            shell=True, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out, err = p.communicate()
        return out


if __name__ == '__main__':
    py = pyspdk('nvmf_tgt')
    start_server(py, "/home/wewe/spdk/", 'nvmf_tgt')
