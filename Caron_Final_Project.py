'''
Please see 'README.md' file!
About this script:
- Return helpful message upon running FINAL_PROJECT.py file in command line
- Take file from command line, merge to merge_file.csv
- Remove headers from document that aren't in row 0
- Remove lines that start with 'Mean' or 'SD' to clean up the document
'''

import csv
import sys
import argparse
import os.path

parser = argparse.ArgumentParser()

def parse_args():
	'''this function adds a helpful input comment at start of program'''
	parser = argparse.ArgumentParser(
		description = 'Merge flow cytometry CSV files and clean up unnecessary lines.'
	)
	parser.add_argument('path', help = '<input> For usage: <python3> <Caron_Final_Project.py> <filename.csv>')
	return parser.parse_args()


def file_choices(choices,fname): 
	'''this function will prompt you if the file name does not have .csv extension, and will not run other file extensions'''
	ext = os.path.splitext(fname)[1][1:]
	if ext not in choices:
		parser.error('File does not end with extension {}'.format(choices)) # choices are in main body of code
	return fname


def strip_header(infile_header, outfile_header):
	'''this function strips any additional headers except header in row 0'''
	for i, line in enumerate(infile_header):
		if i == 0: # write first line (row 0) to new file
			outfile_header.write(line)
		else:
			if not line.startswith(',Count,Live'): # write every line that is not an additional header to new file
				outfile_header.write(line)
	
	
def delete_line():
	'''this function removes lines that start with 'Mean' and 'SD' '''
	for line in infile_lines:
		if 'Mean' in line:
			pass
		elif 'SD' in line:
			pass
		elif 'Compensation' in line:
			pass
		else:
			outfile_lines.write(line) # essentially write all lines that do NOT include 'Mean' or 'SD' to new file
			

if len(sys.argv) != 2:
# if not enough/too many arguments entered into command line, print helpful message to command line, includes usage prompt
	print('Incorrect number of arguments, enter -h for help')


parse_args()
parser.add_argument('fn', type = lambda s:file_choices(('csv'),s)) # file extensions that will allow code to run, see file_choices function
parser.parse_args()

source_file = open(sys.argv[1], 'r') # input first file from command line
merged_file = open('merged_file.csv', 'a') # open a file in append mode that we will merge all of our files to
data = source_file.read() 
merged_file.write(data) # merge the .csv file to the new merged file

source_file.close() # close the original file and the merge file since
merged_file.close()

infile_header = open('merged_file.csv', 'r') # reopen merge file stream in read mode
outfile_header_filename = 'merged_file.csv'.replace('.csv', '_noheader.csv') # append the file name to indicate changes
outfile_header = open(outfile_header_filename, 'w') # open new filestream in write mode

strip_header(infile_header, outfile_header) # call function to remove any added headers except row 0 header

infile_header.close() # close the header file streams
outfile_header.close()

infile_lines = open('merged_file_noheader.csv', 'r') # open the file stream that has no headers in read mode
outfile_lines_filename = 'merged_file_noheader.csv'.replace('_noheader.csv', '_FINAL.csv') # adjust file name to reflect changes
outfile_lines = open(outfile_lines_filename, 'w') # open file stream in write mode

delete_line() # call function to remove any 'compensation', 'mean', or 'SD' rows

infile_lines.close() # close up the file streams
outfile_lines.close()
