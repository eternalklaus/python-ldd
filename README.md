# python-ldd
Python ldd script, simple and lightweight.  
List `SONAME`s of dynamically linked libraries of input binary.


# Usage example
    $ python ldd.py /bin/ls
    libselinux.so.1
    libc.so.6

# Todo
Resolve library full path from `SONAME`
