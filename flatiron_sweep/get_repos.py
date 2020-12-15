from github import Github

# Generates a list of repos that are to later be cloned &  deleted
def get_repos(github_instance, regex_exp, github_user, github_token):
	print('Fetching list of repos...')

	list_of_repos = []

	# Fetches repos that match regex
	for repo in github_instance.get_user().get_repos():
		if regex_exp in repo.name:
			list_of_repos.append(repo.name)

	return list_of_repos