from git import Repo
import os

def clone_repo(repo, base_directory, github_user):
	print(f'Cloning {repo}')
	directory = f'{base_directory}/misc'

	# Filter to correct sub directory
	if 'ruby' in repo:
		directory = f'{base_directory}/ruby'
	if  'activerecord' in repo:
		directory = f'{base_directory}/ruby'
	if 'sinatra' in repo:
		directory = f'{base_directory}/sinatra'
	if 'rails' in repo:
		directory = f'{base_directory}/rails'
	if 'fewpjs' in repo:
		directory = f'{base_directory}/javascript'
	if 'js' in repo:
		directory = f'{base_directory}/javascript'
	if 'javascript' in repo:
		directory = f'{base_directory}/javascript'
	if 'react' in repo:
		directory = f'{base_directory}/react'
	if 'redux' in repo:
		directory = f'{base_directory}/react'

	# Clone repo
	repo = Repo.clone_from(
    	f'http://github.com/{github_user}/{repo}.git',
    	f'{directory}/{repo}',
    	branch='master'
	)