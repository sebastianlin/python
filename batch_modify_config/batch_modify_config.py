#!/usr/bin/python


import os, sys, glob, subprocess, tempfile

replace_str_array = [["CONFIG_CMDLINE_BOOL", "CONFIG_CMDLINE_BOOL=y", "# CONFIG_CMDLINE_BOOL is not set" ], ["CONFIG_PARPORT" , "# CONFIG_PARPORT is not set", "CONFIG_PARPORT=y"]]

tempfile_tuple = tempfile.mkstemp(prefix="colin.")[1] 
file4 = open(tempfile_tuple,  'w')
print "The opened file is " + tempfile_tuple +"."

for file in glob.glob('/tmp/colin/test2/scpu/Linux/linux-2.6.34/config.compact.avhdd.nike.scpu.secure.nxx.nand.old'):
	file2 = open(file, "rt")
	while 1:
		line = file2.readline()
		if not line: break
#		print line,
		i = 0
		while 1:
			line=line.replace(replace_str_array[i][1], replace_str_array[i][2])
			i = i+1
			if i>=len(replace_str_array):
				break
		file4.write(line)
#		subprocess.call(["echo", file])
	file4.close()
	file2.close()






