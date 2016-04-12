# python version of grep -- for use outside of Linux / OSX;

# how to == py pygrep.py <file> <string to grep>


"""
ABOUT:

A Python grep tool for use in Windows env (since win doesn't support grep (! not mentioning the win-10 Linux support... :P ) natively).

Currently this script will print whole lines (in-context) of the search string.
"""






import sys, os, re, argparse

VER_NO = "v1.2";

h_info = \
r'''- Make sure the file being grepped is saved in ANSI
		format; this program has trouble with UNICODE
- Full file paths, unless the file is within the same
		directory;
'''

e_snip = \
r'''
## basic grep:

>>>		pygrep.py <file_name.file_ext> <string_to_search_for>

e.g.	pygrep.py example.txt "hello"

## output to file:

>>>		pygrep.py <file> <string> -f <output_file_path>

		
e.g.	pygrep.py example.txt "hello" -f "example_res.txt"


** other notes


#
#	be aware that this program does not (currently)
#	parse text (in non .txt documents).
#
#	this means, if reading from a(n) .rtf file (Rich Text File)
#	any text used to render the font within the application
#	to edit the file will remain, such as [\f1] or [\b], etc.
#
#	the same would apply to .html files, where the HTML tags
#	will be present in the returned text.
#
#	<title>Website Title</title> <- for example;
#
'''


# CLI PARSER -- set-up;
par = argparse.ArgumentParser(prog = 'pygrep', prefix_chars = '-',
	description = 'ASCII grep tool (CLI) only -- type [-h/--help] for assistance.');
par.add_argument('file', nargs = '?', type = argparse.FileType('r'),
	default = None, help = 'file to grep');
par.add_argument('string', nargs = '?', action = 'store',
	help = 'string to search for within file');
par.add_argument('-f', '--fout', action = 'store', help = 'output info to file FOUT');
par.add_argument('-i', '--info', action = 'store_true', help = 'other help information');
par.add_argument('-e', '--example', action = 'store_true', help = 'display example(s) for using pygrep');
par.add_argument('-v', '--version', action = 'version', version = '%(prog)s {}'.format(VER_NO),
	help = 'displays tool version');
par.add_argument('-a', '--author', action = 'store_true', help = 'display program author');





def grep_file(search_string):
	print('\n/**\n')
	for line in args.file:
		if re.search(search_string, line):
			print(line)
		else:
			pass;
	print('\n**/\n')

def grep_output_to_file(search_string):
	output_file_name = args.fout;
	
	# original standard output;
	temp = sys.stdout;

	# output to file;
	sys.stdout = open(output_file_name, "w+");

	

	for line in args.file:
		if re.search(search_string, line):
			print(line + '\n');
		else:
			pass;
	
	sys.stdout.close();
	sys.stdout = temp;
	print('Finished');


args = par.parse_args();

if (args.fout):
	try:
		grep_output_to_file(args.string);
	except Exception, e:
		print(e);
else:
	if not args.author and not args.info and not args.example:
		# if [-a/--author] or [-i/--info] is included, then grep_file() won't run;
		try:
			grep_file(args.string);
		except TypeError:
			print("No path was provided; type `pygrep -h` for help")
	elif (args.author):
		print('pygrep -- arkat-one <arcius0@gmail.com>');
	elif (args.info):
		print(h_info);
	elif (args.example):
		print(e_snip);

