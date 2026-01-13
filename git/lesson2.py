# 1. You typically obtain a Git repository in one of two ways:
# i. You can take a local directory that is currently not under version control, and turn it into a Git
# repository, or
# ii. You can clone an existing Git repository from elsewhere.
# In either case, you end up with a Git repository on your local machine, ready for work.

# 2. git init
# i. Initializing a Repository in an Existing Directory
# ii. This creates a new subdirectory named .git that contains all of your necessary repository files — a
# Git repository skeleton.

# Initializing a repository means:

# Taking a normal folder and telling Git:
# “Start tracking changes here.”

# syntax: git init

# Example 1 — Empty directory
# mkdir my-project
# cd my-project
# git init

# Result:

# my-project/ is now a Git repository

# No files are tracked yet

# Check:

# git status

# You’ll see:

# No commits yet
# nothing to commit

# Example 2 — Directory with files already in it
# cd website
# ls

# Output:

# index.html style.css script.js

# Now initialize:

# git init

# Result:

# Files still exist

# All files are untracked

# Check:

# git status

# Example 3 — Start tracking after init
# git init
# git add .
# git commit -m "Initial commit"

# Result:

# Repository now has a first snapshot

# All existing files are tracked

# This is the most common real-world flow.

# Example 4 — Verify it’s a Git repository
# ls -a

# Output includes:

# .git

# That hidden folder is the entire Git brain.

# If .git exists → it’s a Git repo.

# 3. git clone
# i. We use "git clone" to copy an existing Git repository to a certain local directory.
# ii. syntax: git clone <repository-url>

# Example: git clone https://github.com/libgit2/libgit2

# Making a full local copy of an existing Git repository.

# When you clone:

# You get all files

# You get entire history

# Git is already enabled (no git init needed)

# The command

# git clone <repository-url>

# This:

# Creates a new directory

# Downloads the repository into it

# Automatically sets up origin (the remote)

# Example 1 — Basic clone
# git clone https://github.com/user/project.git

# Result:

# A folder named project/ is created

# You can immediately run:

# cd project
# git status

# Example 2 — Clone into a custom directory name

# git clone https://github.com/user/project.git my-project

# Result:

# Folder created: my-project/

# Repo contents live there instead of project/

# Example 3 — Clone via SSH

# git clone git@github.com:user/project.git

# Result:

# Same as HTTPS clone

# Uses SSH keys (no password every time)

# Example 4 — Clone a specific branch

# git clone -b dev https://github.com/user/project.git

# Result:

# Repository is cloned

# dev branch is checked out instead of main
