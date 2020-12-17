A CLI for cloning & optionally deleting repos associated with the Flatiron curriculum.

Step by step - https://christian24cain.medium.com/how-to-clone-optionally-delete-flatiron-curriculum-repos-b11521477ecb

**Disclaimer** - If you're looking to delete, ensure that you use the --txt flag only first to scan through repos that get flagged. Deleting repos will also erase contributions, though pull requests for curriculum repos will still be visible.

If you do not wish to delete, then do not select the delete option when creating your GitHub Token.

[Future Update] - provide the option to mark repos as private, so contributions are preserved.

# Getting Started

`$ pip install flatiron_sweep`

Generate a GitHub token, and enable the delete option only if you wish to delete repos as well.

After calling `flatiron_sweep` with the appropriate flags, you will be prompted to input your: 
- GitHub username
- GitHub token
- 6 digit date of your cohort.

# Flagged Repos

`$ flatiron_sweep --txt`

This generates a .txt file in the Desktop directory with a list of repos that this CLI flags. Be sure to run this prior to deleting to verify that only desired repos will be deleted.

# Cloning

`$ flation_sweep --clone`

This creates a directory called 'flatiron_repos' in Dekstop, and clones all repos that contain the 6 digit cohort substring. Includes basic filtering.

# Deleting

`$ flatiron_sweep --delete`

This deletes all repos that contain the 6 digit cohort substring. Ensure to clone prior, or additionally append the clone flag.