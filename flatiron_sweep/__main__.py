import sys
import argparse
from github import Github

from .generate_file_tree import *
from .get_repos import *
from .generate_list_file import *
from .clone_repo import *
from .delete_repo import *

parser = argparse.ArgumentParser(description='Clones & deletes Flatiron repos. Recommended to run with --txt flag prior to cloning or deleting in order to verify flagged repos!')

# Txt flag creates a file with a list of flagged repos
parser.add_argument('--txt', action="store_true",
	help='Generates a txt file listing flagged repos')

# Clone flag clones all repos that meet condition
parser.add_argument('--clone', action="store_true",
	help='Creates a directory in Dekstop & clones all flagged repos')

# Delete flag deletes all repos that meet condition
parser.add_argument('--delete', action="store_true",
	help='Deletes all flagged repos')

args = parser.parse_args()

def gather_credentials():
	github_user = input('User: ')
	github_token = input('Token: ')
	regex_exp = input('6 digit cohort date: ')
	return [github_user, github_token, regex_exp]

def main():
	if args.txt or args.clone or args.delete:
		# Gather credentials
		credentials = gather_credentials()
		github_user = credentials[0]
		github_token = credentials[1]
		regex_exp = credentials[2]

		# Create GitHub instance
		g = Github(github_user, github_token)
		user = g.get_user()
		user.login

		list_of_repos = get_repos(g, regex_exp, github_user, github_token)

		if args.txt:
			generate_list_file(list_of_repos)

		if args.clone:
			desktop = os.path.expanduser('~/desktop')	
			parent_path = f'{desktop}/flatiron_repos'

			generate_file_tree(parent_path)

			for repo in list_of_repos:
				clone_repo(repo, parent_path, github_user)
				if args.delete:
					delete_repo(g, repo)

		elif args.delete:
			for repo in list_of_repos:
				delete_repo(g, repo)

if __name__ == '__main__':
    main()