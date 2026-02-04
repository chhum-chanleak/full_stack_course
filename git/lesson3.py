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

# 4. git pull
# i. "git pull" brings changes from a remote repository into your local branch.

# Under the hood, it does two steps:

# git fetch  +  git merge

# So mentally:

# “Get remote changes, then integrate them into my current branch.”

# Basic form:

# git pull <remote> <branch>

# Most of the time:

# git pull

# Example 1: Simple pull (most common)

# You’re on main, and someone pushed new commits to origin/main.

# git pull

# What happens:

# Fetches latest commits from the remote

# Merges them into your local main

# Use this before you start working.

# Example 2: Pull from a specific branch

# You want to pull changes from origin/main while on another branch.

# git pull origin main

# What happens:

# Downloads changes from origin/main

# Merges them into your current branch

# Useful when syncing a feature branch with main.

# Example 3: Pull with rebase (clean history)

# You want to avoid merge commits.

# git pull --rebase

# What happens:

# Fetches remote changes

# Replays your local commits on top of them

# Result:

# Linear, cleaner commit history

# Common in professional workflows

# Example 4: Pull after a conflict exists

# You try:

# git pull

# Git responds with a merge conflict.

# What you do:

# Open conflicted files

# Resolve conflicts manually

# Stage fixes:

# git add .

# Complete the merge:

# git commit

# This finalizes the pull.