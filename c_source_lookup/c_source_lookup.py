#!/usr/bin/python                                                                                                               
# If we have map files and .i (gcc with -save-temps option) files, we can use this tool to find out all used .a, .c, .S, and .h files.
# Usage:

import sys, os

# Header files containing these strings won't be displayed
header_exclude_files=["u-boot64/arch/", "u-boot64/include/", "scx35l64_ss_sharklt8", "gcc/linux-x86"]

START_GROUP_STR='START GROUP'
END_GROUP_STR='END GROUP'
LOAD_STR='LOAD '

# Translate a relative-path file list to an absolute-patch file list
def file_path_list_to_absolute(file_list):
	for i in range(len(file_list)):
		file_list[i] = os.path.abspath(file_list[i])

# Traverse a directory
def traverse_dir(dirname_str):
	sub_i_files=[]
	sub_s_files=[]
	sub_a_files=[]
	for dirName, subdirList, fileList in os.walk(dirname_str):							# traverse the dir
#		print('Found directory: %s' % dirName)
		for fname in fileList:															# all files
			if fname.endswith('.map'):													# files end with .map
				with open(dirName+'/'+fname, 'r') as f:
					start = 0
					for line in f:
						if line.startswith(START_GROUP_STR):								# lines between "START GROUP" and "END GROUP"
							start=1
						else:
							if line.startswith(END_GROUP_STR):
								start=0
							elif start==1:
#								print(line)
								if line.startswith(LOAD_STR):								# Start with "LOAD "
									if line.endswith(".o\n"):								# Handle .o files
										fileName2=line[len(LOAD_STR):-len(".o\n")]
										dirName2 = dirName[:-len("out")]
										newFile = dirName2+fileName2+".i"
										newFile=os.path.abspath(newFile)
										if os.path.isfile(newFile):							# If .o has a related .i file
											if newFile not in sub_i_files:
												sub_i_files.append(newFile)
										else:
											newFile = dirName+"/"+line[len("LOAD "):-1]
											newFile=os.path.abspath(newFile)
											if newFile not in sub_s_files:
												sub_s_files.append(newFile)
									elif line.endswith(".a\n"):								# Handle .a files
										fileName2=line[len(LOAD_STR):-1]
										if fileName2.startswith('/'):
											newFile = fileName2
										else:
											newFile = dirName+"/"+fileName2
										newFile=os.path.abspath(newFile)
										if newFile not in sub_a_files:
#											if os.path.isfile(newFile):
											sub_a_files.append(newFile)
	sub_i_files.sort()
	sub_s_files.sort()
	sub_s_files.sort()
	return sub_i_files, sub_s_files, sub_a_files

# Parse ".i" file. A ".c" file and many ".h" files will be found.
def parse_i_file(dir, file):
	c_file_name=""
	header_list=[]
	with open(file, 'r') as f:
		for line in f:
			if line.startswith('# '):
				local_file = line[line.index('"')+1:line.rfind('"')]
				if not local_file.startswith("/"):
					local_file = dir+local_file
				if local_file.endswith('.h'):
					local_file=os.path.abspath(local_file)
					if local_file not in header_list:
						header_list.append(local_file)
				elif local_file.endswith('.c'):
					if c_file_name == "" :
						c_file_name = local_file
	header_list.sort()
	return c_file_name, header_list


for i in range(1, len(sys.argv)):										# Parse all parameters
	if os.path.isdir(sys.argv[i]):										# If it is a dir
		print("Lookup directory, " + sys.argv[i] + ".")
		sub_i_files, sub_s_files, sub_a_files = traverse_dir(sys.argv[i])
		if sub_i_files != []:
			print("Result in " + sys.argv[i] + ":")
			print("\tLibraries:")
			for file in sub_a_files:
				print("\t\t"+ file)
			print("\tAssembly source:")
			for file in sub_s_files:
				print("\t\t"+ file)
			print("\tObject files:")
			for file in sub_i_files:
				c_file, h_files = parse_i_file(sys.argv[i], file)
				print("\t\t"+ os.path.abspath(c_file) + ":")
				for file2 in h_files:
					is_exclude=False
					for excl_file in header_exclude_files:
						if file2.__contains__(excl_file):
							is_exclude = True
					if is_exclude == False:
						print("\t\t\t"+ file2)













