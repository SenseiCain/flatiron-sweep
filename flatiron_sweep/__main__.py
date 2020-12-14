import sys
from .generate_repos import *

def main():
	args = sys.argv[1:]
	regex_exp = '081219'
	create_text = False

	# Credentials
	with open('credentials.txt', 'r') as f:
		token_array = f.read().split('\n')
		github_user = token_array[0]
		github_token = token_array[1]

	if '--txt' in args:
		# Create repo.txt if --txt flag present
		create_text = True

	generate_repos(regex_exp, github_user, github_token, create_text)

if __name__ == '__main__':
    main()