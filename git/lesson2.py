# *Checking repository status

# 1. git status
# i. We use "git status" to see which files are staged, modified, or untracked

# Example 1 — Clean working directory
# git status

# Output:

# On branch main
# nothing to commit, working tree clean

# Meaning:

# Your working directory matches the last commit

# No staged changes, no untracked files

# Equivalent to “clean working directory”

# Example 2 — Modified but not staged

# You edit file1.txt but don’t stage it

# git status

# Output:

# On branch main
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
#         modified:   file1.txt

# Meaning:

# file1.txt has been edited

# Changes not staged, so won’t be included in the next commit yet

# Example 3 — Staged changes
# git add file1.txt
# git status

# Output:

# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
#         modified:   file1.txt

# Meaning:

# file1.txt is now staged

# Will be included in the next commit

# You can unstage it with git restore --staged file1.txt

# Example 4 — Untracked files
# # You create a new file newfile.txt
# git status

# Output:

# On branch main
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         newfile.txt

# Meaning:

# newfile.txt exists in your working directory

# Git does not know about it yet

# Use git add newfile.txt to start tracking it

# 2. git log
# i. We use "git log" to view the commit history of the current branch (newest first).

# Example 1 — Basic git log
# git log

# Output (simplified):

# commit a3f5c1e2
# Author: Alex
# Date:   Mon Jan 15

#     Fix login bug

# commit 9b2d4c8a
# Author: Alex
# Date:   Sun Jan 14

#     Initial commit


# Meaning:

# Shows commits in reverse chronological order

# Each commit includes hash, author, date, and message

# Example 2 — One-line log
# git log --oneline


# Output:

# a3f5c1e Fix login bug
# 9b2d4c8 Initial commit


# Meaning:

# Compact view

# Useful for quickly scanning history

# Example 3 — Limit number of commits
# git log -2


# Output:

# commit a3f5c1e2
#     Fix login bug

# commit 9b2d4c8a
#     Initial commit


# Meaning:

# Shows only the last 2 commits

# Example 4 — File-specific history
# git log README.md

# Meaning:

# Shows only commits that modified README.md

# Useful for tracking when and why a file changed

# *Tracking and staging files

# 3. git add
# i. git add moves changes from the working directory to the staging area.

# Example 1 — Add a single file

# git add file1.txt

# Meaning:

# Stages file1.txt

# Only this file will be included in the next commit

# Example 2 — Add multiple specific files

# git add file1.txt file2.txt

# Meaning:

# Stages both files

# Other modified files remain unstaged

# Example 3 — Add all changes

# git add .

# Meaning:

# Stages all changes in the current directory and subdirectories

# Includes modified and untracked files

# Use carefully — it stages everything.

# Example 4 — Add parts of a file (interactive)

# git add -p

# Meaning:

# Lets you stage changes chunk by chunk

# Useful when one file contains unrelated changes