import argparse
import os

# program takes in a directory of image files and renames them to a standardized format
# and numbers them sequentially. Directory is passed in through command line argument,
# and so is desired prefix.
parser = argparse.ArgumentParser(description='standardizes photo filenames')
parser.add_argument('indir', type=str, help='Input dir for files')
parser.add_argument('new_prefix', type=str, help='syntax of filename after rename')
args = parser.parse_args()

# Function to rename multiple files 
i = 0

# for every file found in directory name passed in through command line arg, rename
for filename in os.listdir(args.indir): 
	dst = args.new_prefix + str(i) + ".jpg"
	src = args.indir + filename 
	dst = args.indir + dst 

	# rename() function will 
	# rename all the files 
	os.rename(src, dst) 
	i += 1
