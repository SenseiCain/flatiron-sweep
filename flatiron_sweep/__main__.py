import sys
import argparse
from .generate_file_tree import *
from .get_repos import *
from .generate_list_file import *
from .clone_repo import *

regex_exp = '081219'

parser = argparse.ArgumentParser(description='Clones & deletes Flatiron repos')

# Txt flag creates a file with a list of flagged repos
parser.add_argument('--txt', action="store_true",
	help='Generates a txt file listing flagged repos')

# Clone flag creates clones all repos that meet condition
parser.add_argument('--clone', action="store_true",
	help='Create directory in Dekstop & clones all flagged repos')

# Delete flag creates deletes all repos that meet condition
parser.add_argument('--delete', action="store_true",
	help='Deletes all flagged repos')

args = parser.parse_args()

def gather_credentials():
	github_user = input('User: ')
	github_token = input('Token: ')
	return [github_user, github_token]

def main():
	if args.txt or args.clone or args.delete:
		credentials = gather_credentials()
		github_user = credentials[0]
		github_token = credentials[1]

		list_of_repos = get_repos(regex_exp, github_user, github_token)

		if args.txt:
			generate_list_file(list_of_repos)
		if args.clone:
			desktop = os.path.expanduser('~/desktop')	
			parent_path = f'{desktop}/flatiron'

			generate_file_tree(parent_path)

			for repo in list_of_repos:
				clone_repo(repo, parent_path, github_user)
		elif args.delete:
			print('--delete flag used')


if __name__ == '__main__':
    main()