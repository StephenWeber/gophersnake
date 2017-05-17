# GopherSnake

A gopher client written in Python.

# Standards

The gopher protocol is described in [IETF RFC-1436](https://tools.ietf.org/html/rfc1436). Gopher snake supports elements 0 (file) and 1 (directory).

# Clients

It is recommended you use the Floodgate [OverbiteFF extension](http://gopher.floodgap.com/overbite/) to Mozilla Firefox,
this is what has been tested to work.

I also found [cgo](https://github.com/kieselsteini/cgo), which will list out the directory elements but segfault on accessing a file. It also, as written, does not support text elements.