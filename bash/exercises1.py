# #lx0h

# Generate and store two passwords in Google password manager.

# 1. -> Google chrome
# 2. -> Click "..." button
# 3. -> Passwords and Autofill
# 4. -> Google password manager
# 5. -> Click " Add "

# #lx0l

# What is another way we can call a folder?
# A folder is also called a directory.

# #lx0k
# What does a folder/directory tree look like?

# Normally, a folder/directory can look like:

#  parent_folder(Root)
# ├── child_folderA
# │   ├── child_folderAA   
# │   └── child_folderAB
# ├── child_folderB

# Note*:  Its "Root" is at the top.

# #lx0e

# 1. What does pwd stand for?
# 2. Why do we use it?

# 1. pwd stands for "print working directory"
# 2. We use it to show which folder/directory we are currently in.

# Example:
#   pwd -> user/folder_name/music

# #lx0f

# Exercises: pwd

# a.
# Goal: Use pwd to identify your current directory.

# Open the terminal.

# Run: pwd

# Note the full path shown.

# b.
# Goal: Use pwd to verify directory changes.

# Run:
#  cd /
#  pwd

# Then run: 
#  cd ~
#  pwd

# c.
# Relative navigation check

# Goal: See how pwd reflects relative movement.

# Create and enter a folder:

# mkdir test_pwd
# cd test_pwd
# pwd

# Go back one level:

# cd ..
# pwd

# d.
# Deep directory awareness

# Goal: Understand full paths in nested directories.

# Create nested folders:

# mkdir -p a/b/c
# cd a/b/c
# pwd

# Write down the full path you see.

# #lx0g

# 1. What does ls stand for?
# 2. Why do we use it?

# #lx0h

# Exercises: listing

# a.
# Task:
# List all visible files and folders in your current directory.

# Command:

# ls

# Answer / What happens:
# You see all non-hidden files and directories in the current location.

# b.
# Task:
# List files with details like permissions, size, and modification date.

# Command:

# ls -l

# Answer / What happens:
# You see a long listing with:

# permissions

# owner

# size

# date

# filename

# c.
# Task:
# Show all files, including hidden ones.

# Command:

# ls -a

# Answer / What happens:
# Hidden files (starting with .), such as .git, .env, appear in the list.

# d.
# Task:
# List all files with full details.

# Command:

# ls -la

# Answer / What happens:
# You see:

# hidden + visible files

# full details for each

# This is the most commonly used ls form.

# #lx0i

# Identify folders and files in the CLI:

# cat.png
# sorry.mp3
# music/
# lesson.txt
# videos/
# videos
# closer.mp4
# music

# Folders: music/, music, videos/, videos     |     Files: cat.png, sorry.mp3, lesson.txt, closer.mp4

# #lx0j

# 1. What does "cd" command stand for?
# 2. Why do we use it?

# 1. Change directory.
# 2. We use it to move up and down the directory/folder tree.

# #lx0k

# Exercises: cd

# a.
# Task:
# From your home directory, move into a folder called Documents.

# Command:

# cd Documents

# Answer / What happens:
# You move from your home directory into the Documents folder.

# b.
# Task:
# From inside Documents, go back to your home directory.

# Command:

# cd ..

# Answer / What happens:
# You move one level up, returning to your home directory.

# c.
# Task:
# From any directory, return to your home directory.

# Command:

# cd ~

# (or simply cd)

# Answer / What happens:
# You are taken directly to your home directory.

# d.
# Task:
# From your home directory, move into:

# projects/app

# Command:

# cd projects/app

# Answer / What happens:
# You move into the app directory using a relative path.

# 1. What does mkdir stands for?
# 2. Why do we use it?

# Exercises: mkdir

# Exercise 1: Create one directory

# Task:
# Create a directory named practice in your current location.

# Answer:

# mkdir practice

# 🧪 Exercise 2: Create multiple directories

# Task:
# Create three directories named html, css, and js with one command.

# Answer:

# mkdir html css js

# 🧪 Exercise 3: Create nested directories safely

# Task:
# Create a directory structure src/components/buttons, even if src does not exist yet.

# Answer:

# mkdir -p src/components/buttons

# 🧪 Exercise 4: Create a directory using a full path

# Task:
# Create a directory called bash-practice inside your home folder.

# Answer:

# mkdir ~/bash-practice