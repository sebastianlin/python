#!/bin/python


#!/usr/bin/python
import cextension

print cextension.noargfunc()
cextension.argument_test(1, 2.0, "three")
print cextension.foo_add(1, 3)
print cextension.list_test()
print cextension.varlist_test()
print cextension.varcomplex_test()



