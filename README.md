# py-spdk
## Problem description

As we all know, SPDK is a high-performance kit written in c, It is hard for python applications to communicate with SPDK directly. Developers should be able to provide a client for callers to use SPDK better. The py-spdk is such a python client designed for the upper-level management applications to get what they want about SPDK, and further to accelerate the backend. 

### Use Case

The py-spdk is designed for all of the management-level applications. For example:

* vhost
* When Cinder directly uses SPDK as its backend, the Cyborg should be able to call the py-spdk through adding the driver function to complete the life cycle management of SPDK as well as get something returned by the backend SPDK. According to the configuration file of the upper-level management application, the py-spdk will to be known whether the backend is installed with SPDK. If so, it will provide the related functions of initialization and startup for server. Once the server is successfully started, the py-spdk can obtain what it requires. 


## Proposed change

In general, the goal is to develop the py-spdk that supports the management and the use of SPDK.

### Design Workflow

* Modify the rpc.py provided by SPDK, and use init() to encapsulate most of its original functions,  and then execute rpc.py when called by pyspdk.py.
* When the upper management application needs to get something about SPDK, it will call pyspdk. py. And then the pyspdk.py can tell if the process of SPDK is alive in system. If not, it will initialize and start the server.
* The pyspdk.py uses the rpc.py to communicate with the SPDK server application, as: nvmf_tgt, vhost, etc, and then to get something about SPDK, as: get_luns, get_interfaces, get_vhost_blk_controller, etc.

### Something Returned
#### Start nvmf_tgt

![py-spdk](https://github.com/hellowaywewe/py-spdk/get_bdevs.png

#### Start vhost

![py-spdk](https://github.com/hellowaywewe/py-spdk/get_luns.png

