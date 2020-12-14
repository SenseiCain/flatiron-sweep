from github import Github
import os

# Generates a list of repos that are to later be cloned &  deleted
def generate_repos(regex_exp, github_user, github_token, create_txt = False):
	print('Fetching list of repos...')

	# Create GitHub instance
	g = Github(github_user, github_token)
	user = g.get_user()
	user.login

	list_of_repos = []

	# Fetches repos that match regex
	for repo in g.get_user().get_repos():
		if regex_exp in repo.name:
			list_of_repos.append(repo.name)

	# Conditionally create file
	if create_txt:
		desktop = os.path.expanduser('~/desktop')
		repo_file = open(desktop + '/flation_sweep_repos.txt', 'w')
		
		for repo_name in list_of_repos:
			repo_file.write(repo_name)
			repo_file.write('\n')

	return list_of_repos