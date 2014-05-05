#!/usr/bin/python


import os, sys, glob, subprocess, tempfile

replace_str_array = [["CONFIG_CMDLINE_BOOL", "CONFIG_CMDLINE_BOOL=y", "# CONFIG_CMDLINE_BOOL is not set" ]]

file4 = open(tempfile.mkstemp()[1], "rw")


for file in glob.glob('/home/mark/RTK_workshop/nike/svn/DTH_permission/nike_scpu/linux-2.6.34/config.develop.avhdd.nike.scpu.secure.nxx.nand.old'):
	file2 = open(file)
	while 1:
		line = file2.readline()
		if not line: break
#		print line,
		line.replace(replace_str_array[0][1], replace_str_array[0][2])
		file4.write(line)
#		subprocess.call(["echo", file])
	tmp_file.close()
	file4.close()
	file2.close()






