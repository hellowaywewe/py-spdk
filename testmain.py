import share_val
import os
from test1 import test1
from test2 import test2
from test3 import test3

c = test2()
c.add()

s = test1()
s.showchange()

c1 = test2()
c1.add()

s1 = test1()
s1.showchange()

t = test3()
t.testchange()

server_dir = os.path.join('/home/wewe/spdk/', 'app/')

a = 'fi'
b = 'fi'
print server_dir == b
print server_dir

spdk_dir = '/Users/wewe/share'


def search_file(string):
    for dirpath, dirnames, filenames in os.walk(spdk_dir):
        for filename in filenames:
            if filename == string:
                print 'File', filename
                print dirpath

search_file('test_plan.md')
