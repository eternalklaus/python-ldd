#!/usr/bin/python
#-*- coding: utf-8 -*-
from elftools.elf.elffile import ELFFile
from elftools.elf.dynamic import DynamicSection
import sys



def ldd(filename):
	bin = ELFFile(open(filename, 'rb'))
	DynamicSections = [s for s in bin.iter_sections() if isinstance(s, DynamicSection)]
	for section in DynamicSections:
		for tag in enumerate(section.iter_tags()):
			if tag[1].entry.d_tag == 'DT_NEEDED':
				print tag[1].needed

def call_loader(soname):
	'''
	SONAME으로부터 library full path를 얻기 위해서는 아래 디렉토리를 순회하며 SONAME과 비교해보아야 한다. 
	(ldd 에서는 단순히 ld.so를 특별 플래그(LD_TRACE_LOADED_OBJECTS)로 로딩하여 한방에 full path를 얻어올 수 있지만...)

	DT_RPATH: Using the DT_RPATH dynamic section attribute of the binary if present and DT_RUNPATH attribute does not exist. Use of DT_RPATH is deprecated. (Ie: this is a value that can be included in an executable’s ELF header.  There’s apparently some controversy over whether DT_RPATH really overrides LD_LIBRARY_PATH — GW).
	LD_LIBRARY_PATH: Using the environment variable LD_LIBRARY_PATH. Except if the executable is a set-user-ID/set-group-ID binary, in which case it is ignored. 
	DT_RUNPATH: Using the DT_RUNPATH dynamic section attribute of the binary if present. (Ie: the executable can provide a list of paths t search for objects to load. However, DT_RUNPATH is not applied at the point those objects load other objects. — GW)
	/etc/ld.so.cache : From the cache file /etc/ld.so.cache which contains a compiled list of candidate libraries previously found in the augmented library path. If, however, the binary was linked with -z nodeflib linker option, libraries in the default library paths are skipped.
	Default paths: In the default path /lib, and then /usr/lib. If the binary was linked with -z nodeflib linker option, this step is skipped.
	'''

if __name__=="__main__":
	if len(sys.argv)!=2:
		print "usage : ldd.py <binary name>"
		sys.exit(1)
	else:
		ldd(sys.argv[1])