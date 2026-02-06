# *Instruction:

# This project1 is ready for those who have learned git lesson1.py, lesson2.py, exercises1.py and exercises2.py.

# *Git Workplace Simulation Project

# Scenario

# You are a junior developer joining a project.

# Tasks include:

# Initializing a repo

# Adding files

# Making changes

# Staging and committing logically

# Checking history and differences

# Simulating collaboration with a cloned repo

# Project Goal

# Create a simple website project with multiple files, make changes, track them in Git, and inspect history.

# my-website/
# ├── index.html
# ├── styles.css
# └── app.js

# Step 1: Initialize or Clone a Repository

# Option A: Start from scratch

# mkdir my-website
# cd my-website
# git init

# Option B: Clone an existing repository

# git clone https://github.com/user/sample-website.git
# cd sample-website

# Step 2: Check Status

# git status

# Observe untracked files if you started from scratch

# Observe clean state if cloned

# Step 3: Add Initial Files

# touch index.html styles.css app.js
# git status      # check new files
# git add .       # stage all files
# git status      # confirm staging
# git commit -m "Initial commit: add basic project files"

# Step 4: Make Changes and Track Them

# Modify files
# echo "<h1>Welcome</h1>" >> index.html
# echo "body { margin: 0; }" >> styles.css

# Check differences

# git diff        # see unstaged changes

# Stage selectively

# git add index.html
# git status      # see staged vs unstaged
# git commit -m "Add welcome heading to homepage"

# Step 5: Make a Multi-File Logical Change

# echo "console.log('App started');" >> app.js
# echo "h1 { color: blue; }" >> styles.css

# git add app.js styles.css
# git commit -m "Update app behavior and style heading color"

# Step 6: Inspect History

# git log             # full commit history
# git log --oneline   # concise view
# git log -2          # last 2 commits
# git log index.html  # history of a single file

# Step 7: Simulate Collaboration

# Clone the repo into another folder:

# cd ..
# git clone ./my-website my-website-copy
# cd my-website-copy

# Make a change in the cloned copy:

# echo "<p>About section</p>" >> index.html
# git add index.html
# git commit -m "Add About section in clone"

# Compare changes in original repo:

# cd ../my-website
# git fetch ../my-website-copy
# git log --oneline --graph --all

# This simulates working on the same project from two copies (like two teammates).

# Step 8: Optional Inspection

# git diff between commits:

# git diff HEAD~1 HEAD

# Review staged vs unstaged changes:

# git diff
# git diff --staged

# What This Project Simulates

# Real-life project setup

# File tracking and staging

# Logical commits for single and multiple files

# Inspecting diffs before committing

# Viewing commit history

# Collaboration via cloned repositories