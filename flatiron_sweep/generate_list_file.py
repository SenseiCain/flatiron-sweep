import os

# Creates a txt file in Desktop listing flagged repos
def generate_list_file(list_of_repos):

	desktop = os.path.expanduser('~/desktop')
	repo_file = open(desktop + '/flatiron_sweep_repos.txt', 'w')
	
	for repo_name in list_of_repos:
		repo_file.write(repo_name)
		repo_file.write('\n')

	print ("Successfully created flatiron_sweep_repos.txt!")