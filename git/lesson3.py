# 1. git push
# i. git push sends your local commits to a remote repository (like GitHub, GitLab, Bitbucket).

# Think:

# “I made changes locally; now I want the remote to see them.”

# Basic syntax:

# git push <remote> <branch>

# Defaults:

# <remote> → usually origin

# <branch> → usually main or master

# Example:

# git push origin main

# Pushes your current commits from local main branch to remote origin.

# Example 1: Simple push after a commit

# You’ve just made a commit locally:

# git add lesson_01.py
# git commit -m "docs: add lesson 1 instructions"
# git push

# If your local branch tracks a remote branch, just git push works.

# Remote now has your new file.

# Example 2: Push a new branch

# You created a new branch feature/exercises:

# git checkout -b feature/exercises
# git add lesson_02.py
# git commit -m "docs: add lesson 2 exercises"
# git push -u origin feature/exercises

# -u sets upstream, so future git push knows where to push automatically.

# Remote now has a new branch with your commit.

# Example 3: Force push (careful!)

# Sometimes you rewrite history (like git commit --amend) and need to overwrite remote:

# git push origin main --force

# ⚠️ This can overwrite remote changes, so only do if you know no one else relies on this branch.

# Example 4: Push tags

# Tags are used for releases:

# git tag v1.0
# git push origin v1.0

# Pushes the tag v1.0 to remote so others can reference this exact commit.