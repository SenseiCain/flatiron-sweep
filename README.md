A CLI for cloning & optionally deleting repos associated with the Flatiron curriculum.

# Dislcaimer

This has the potential to automatically delete mass amounts of repos. I'd advise running this with only the --txt flag at first to verify which repos are flagged.

Also, if using --clone, ensure that a directory named 'flatiron_repos' does not already exist in Desktop.

# Getting Started

`$ pip install flatiron_sweep`

Generate a GitHub token, and enable the delete option if you wish to delete repos as well.

After calling `flatiron_sweep` with the appropriate flags, you will be prompted to input your: GitHub username, GitHub token, and the 6 digit date of your cohort.

# Flagged Repos

`$ flatiron_sweep --txt`

This generates a .txt file in the Desktop directory with a list of repos that this CLI flags. Be sure to run this prior to deleting to verify that only desired repos will be deleted.

# Cloning

`$ flation_sweep --clone`

This creates a directory called 'flatiron_sweep' in Dekstop, and clones all repos that contain the 6 digit cohort substring. Includes basic filtering.

# Deleting

`$ flatiron_sweep --delete`

This deletes all repos that contain the 6 digit cohort substring. Ensure to clone prior, or additionally append the clone flag.