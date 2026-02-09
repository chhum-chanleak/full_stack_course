# *Setting up Git

# 1. Git
# i. Git is a Version Control System(VCS).
# ii. Git is a tool that tracks changes of the project over time. It allows multiple users to collaborate, view history of changes and go back to any certain point in that history

# Example 1

# Git is like a “time machine” for your project

# Every time you commit, Git takes a snapshot of your project.

# You can go back in time, compare moments, or undo mistakes.

# If something breaks today, you can return to a version from yesterday.

# Key idea: history + recovery

# Example 2

# Git is like a “save system in a video game”

# Manual saves = commits

# Different save paths = branches

# Trying risky moves without ruining progress = branches

# Reloading an old save = checkout / reset

# Key idea: safe experimentation

# Example 3

# Git is like a “collaborative Google Docs with checkpoints”

# Many people work on the same files.

# Git tracks who changed what and when.

# If two people edit the same part, Git asks you to resolve it (merge conflicts).

# Key idea: teamwork + accountability

# Example 4

# Git is like a “lab notebook for code”

# Every experiment (change) is recorded.

# You can explain why you made a change (commit message).

# You can branch off to test an idea without polluting the main experiment.

# Key idea: structured progress tracking

# 2. The basic Git workflow goes something like this:
# i. You modify files in your working tree.
# ii. You selectively stage just those changes you want to be part of your next commit, which adds
# only those changes to the staging area.
# iii. You do a commit, which takes the files as they are in the staging area and stores that snapshot
# permanently to your Git directory.

# 3. git config
# i. "git config" = Git’s settings system
# ii. It defines (who you are, how Git behaves, and what tools it uses)

# Example 1 — Set your identity (who you are)

# Git needs to know who made a commit.

# git config --global user.name "Your Name"

# git config --global user.email "you@example.com"

# --global → applies to all repositories

# Stored in: ~/.gitconfig

# Used every time you run:

# git commit

# Example 2 — View your settings

# Check your configuration settings

# git config --list

# output:

# user.name=John Doe
# user.email=johndoe@example.com
# color.status=auto
# color.branch=auto
# color.interactive=auto
# color.diff=auto

# Example 3 — Change default branch name (behavior tweak)

# Modern Git uses main instead of master.

# git config --global init.defaultBranch main

# Affects:

# git init

# New repos will start with:

# main

# Example 4 — Create a shortcut (alias)

# Save typing, reduce friction.

# git config --global alias.st status

# Now this works:

# git st

# 4. Scopes of "git config"
#   3.1. System (--system) – applies to all users on the machine
#   3.2. Global (--global) – applies to the current user across all repos
#   3.3. Local (default) – applies only to the current repo. Local overrides global, global overrides system

# *Creating or cloning a repository

# 5. git init
# i. Initializing a Repository in an Existing Directory
# ii. This creates a new subdirectory named .git that contains all of your necessary repository files

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

# 6. git clone
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