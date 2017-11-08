# py-spdk
## Problem description

As we all know, SPDK is a high-performance kit written in c. It is hard for management applications written in python to connectted with SPDK-based app (as: nvmf_tgt, etc.) directly. For this reason, developers should be able to provide a client for callers to make convenient use of SPDK-based app. The py-spdk is such a python client that is designed for the upper-level management applications to communicate more fully and to get results returned by SPDK-based app. 

## Use case

The py-spdk is designed for all of the management-level applications to employ SPDK-based app better. For example:

* As an acceleration framework, the OpenStack Cyborg can find and report the ability of backend accelerators including hardware  (like FPGA) and software (like DPDK, SPDK) acceleration resources. It should be able to call the py-spdk through adding the driver function to complete the life cycle management of SPDK-based app as well as get some data returned. According to the configuration file of the upper-level management application, the py-spdk will to be informed whether the backend is installed with SPDK. If so, then the py-spdk will judge further if the SPDK-based app process (as: nvmf_tgt, vhost) you need is started. Suppose the nvmf_tgt server is not alive, it will provide the functions of initialization and startup for server. Once the server is successfully started, the py-spdk can obtain what it requires, and then do other operations. 


## Proposed change

In general, the goal is to develop the py-spdk that supports the management and the use of SPDK.

### Design workflow

* Modify the rpc.py provided by SPDK, and use init() to encapsulate most of its original functions, and then execute rpc.py when it’s invoked by pyspdk.py.
* When the upper management application needs to get something about SPDK, it will call pyspdk.py. And then the pyspdk.py can tell if the process of SPDK is alive in system. If not, it will initialize and start the server.
* The pyspdk.py uses the rpc.py to communicate with the SPDK server application, as: nvmf_tgt, vhost, etc, and then to get something about SPDK, as: get_luns, get_interfaces, get_vhost_blk_controller, etc.

		class pyspdk(object):
            def start_server(self, spdk_dir, server_name)
        
            def init_hugepages(self, spdk_dir)
        
            def search_file(self, spdk_dir, file_name)
        
            def get_process_id(self, pname)
        
            def is_alive(self)
        
            def exec_rpc(self, method, server='127.0.0.1', port=5260)
        
            def close_server(self, spdk_dir, server_name)
                pass

### Returned result
#### Start nvmf_tgt server example

![py-spdk](https://github.com/hellowaywewe/py-spdk/blob/master/get_bdevs.png)

#### Start vhost server example

![py-spdk](https://github.com/hellowaywewe/py-spdk/blob/master/get_luns.png)


