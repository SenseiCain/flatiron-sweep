import sys
from .generate_repos import *
from .generate_file_tree import *
from .clone_repo import *

def main():
	args = sys.argv[1:]
	regex_exp = '081219'
	create_text = False

	# Credentials
	with open('credentials.txt', 'r') as f:
		token_array = f.read().split('\n')
		github_user = token_array[0]
		github_token = token_array[1]

	# Displays instruction
	if '--help' in args:
		print('CLI for cloning & deleting Flatiron repos')
		print('Requires 3 args: GitHub Username, GitHub access key, and cohort date')
		print('Caution! Run with --txt flag to see all flagged repos prior to deleting!')
		print('\n')
		print('[--txt]      generates a txt file listing all flagged repos')
		print('[--clone]    generates a folder in desktop & clones all repos')
		print('[--delete]   deletes all repos that match')
	else:
		# Create repo.txt if --txt flag present
		if '--txt' in args:
			create_text = True

		list_of_repos = generate_repos(regex_exp, github_user, github_token, create_text)

		if '--clone' in args:
			# Create directory in Desktop
			desktop = os.path.expanduser('~/desktop')
			parent_path = f'{desktop}/flatiron'
			generate_file_tree(parent_path)

			# Clones repos that match regex
			# Cloned to file tree created above w/ basic filtering
			for repo in list_of_repos[:5]:
				clone_repo(repo, parent_path, github_user)


if __name__ == '__main__':
    main()