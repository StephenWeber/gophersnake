# GopherSnake

A (simple) gopher server written in Python.

# Installation

This requires Python 3, but no outside dependencies.

We recommend you install into a virtualenv:

    # virtualenv -p python3.6 venv
    ... ... ...
    (venv) # pip install .
    ... ... ...
    (venv) #

You should then have the command `gophersnake` installed on your (virtualenv) path:

    (venv) # gophersnake
    Process started...
    Connecting to localhost:7070

Alternatively, if you don't want to install it you can just use the `run_local` command:

    # ./run_local
    Process started...
    Connecting to localhost:7070

You may also provide a filename of a YAML file detailing the Gopher entity structure. See `example_files/basic.yaml` for the general idea:

    (venv) # ./run_local example_files/basic.yaml
    Process started...
    Connecting to localhost:7070

# Standards

The gopher protocol is described in [IETF RFC-1436](https://tools.ietf.org/html/rfc1436). Gopher snake supports elements 0 (file) and 1 (directory). All other entity types are ignored.

# Clients

It is recommended you use the Floodgate [OverbiteFF extension](http://gopher.floodgap.com/overbite/) to Mozilla Firefox,
this is what has been tested to work.

I also found [cgo](https://github.com/kieselsteini/cgo), which will list out the directory elements but segfault on accessing a file. It also, as written, does not support text elements.