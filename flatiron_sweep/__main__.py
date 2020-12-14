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