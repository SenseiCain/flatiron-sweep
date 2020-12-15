from github import Github

# Deletes repo that matches expression
def delete_repo(g, repo_name):
	print(f'Deleting {repo_name}')
	g.get_user().get_repo(repo_name).delete()