# py-spdk
## Problem description

As we all know, SPDK is a high-performance kit written in c. It is hard for python applications to communicate with SPDK directly. For this reason, developers should be able to provide a client for callers to use SPDK better. The py-spdk is such a python client that is designed for the upper-level management applications to get result returned by server process in SPDK, and further to accelerate the backend. 

## Use case

The py-spdk is designed for all of the management-level applications. For example:

* As an acceleration framework, the Cyborg should be able to call the py-spdk through adding the driver function to complete the life cycle management of SPDK as well as get something returned by the backend SPDK. According to the configuration file of the upper-level management application, the py-spdk will to be known whether the backend is installed with SPDK. If so, it will provide the related functions of initialization and startup for server. Once the server is successfully started, the py-spdk can obtain what it requires. 
* In the virtualization scenario, when users want to get information about the VM virtio device easily, the py-spdk can accomplish the same operations for SPDK as mentioned above. Once the vhost server is successfully started, the py-spdk can report result to the management-level applications, and help SPDK to manage virtio storage controllers,etc.


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
#### Start nvmf_tgt example

![py-spdk](https://github.com/hellowaywewe/py-spdk/blob/master/get_bdevs.png)

#### Start vhost example

![py-spdk](https://github.com/hellowaywewe/py-spdk/blob/master/get_luns.png)


### REST API impact
None

### Security impact
None

### Other end user impact
None

### Performance impact
None

