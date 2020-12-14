# Generates file tree in Desktop directory
# Note - Designed for Mac!

# - Flatiron
# 	- ruby
# 	- sinatra
# 	- rails
# 	- javascript
# 	- react
# 	- misc

import os

def generate_file_tree(parent_path):
	print('Creating file tree...')

	try:
	    os.mkdir(parent_path)
	    os.mkdir(f'{parent_path}/ruby')
	    os.mkdir(f'{parent_path}/sinatra')
	    os.mkdir(f'{parent_path}/rails')
	    os.mkdir(f'{parent_path}/javascript')
	    os.mkdir(f'{parent_path}/react')
	    os.mkdir(f'{parent_path}/misc')
	except OSError:
	    print ("Creation of the directory %s failed" % parent_path)
	else:
	    print ("Successfully created the directory %s " % parent_path)