import argparse
import os

# program takes in a directory of  files and renames them to a standardized format
# and numbers them sequentially. Directory is passed in through command line argument,
# file extension to match, and so is desired prefix. Optionally, the user may specify
# a start index for the numbering.
parser = argparse.ArgumentParser(description='Standardizes filenames')
parser.add_argument('input_dir', type=str, help='Input dir for files')
parser.add_argument('extension_to_match', type=str, help='Filename extension to match')
parser.add_argument('new_prefix', type=str, help='Syntax of filename after rename')
parser.add_argument('--start_index', type=int, default=0, help='Optional starting index. Default is 0')
args = parser.parse_args()

# for every file found in directory name passed in through command line arg, rename
for filename in os.listdir(args.input_dir):
	try:
		if filename.endswith(args.extension_to_match):
			dst = args.new_prefix + str(args.start_index) + args.extension_to_match
			src = args.input_dir + filename 
			dst = args.input_dir + dst 

# rename() function will rename all the files starting with the passed index and moving
# forwards.
			os.rename(src, dst) 
			args.start_index += 1
# Permission error will catch errors related to access rights and Windows error will
# catch errors related to duplicate file names being found.
	except(PermissionError):
		print(filename + " may not be accessed")
	except(WindowsError):
		print(filename + " already exists.")

