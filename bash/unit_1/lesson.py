# 1. Generate and store two passwords in Google password manager.

# 1. -> Google chrome
# 2. -> Click "..." button
# 3. -> Passwords and Autofill
# 4. -> Google password manager
# 5. -> Click " Add "

# 2. A folder is also called a directory.

# 3. Normally, a folder/directory can look like:
                                  
# Example

#  parent_folder(Root)
# ├── child_folderA
# │   ├── child_folderAA   
# │   └── child_folderAB
# ├── child_folderB

# Note*:  Its "Root" is at the top.

# 4. 
# a. pwd stands for "print working directory"
# b. We use it to show which folder/directory we are currently in.

# Examples:

# a. Check current directory

# pwd -> /home/user

# b. After changing directories

# cd Documents
# pwd -> /home/user/Documents

# c. Using pwd with parent directories

# cd ..
# pwd -> /home

# d. Deep directory path

# cd ~/projects/my-app/src
# pwd -> /home/user/projects/my-app/src

# 5.
# a. ls stands for "list".
# b. The ls command shows files and folders in the current directory.

# Example 1: Basic listing
# ls

# What it does:

# Lists visible files and folders in the current directory

# Use when:

# You want to see “what’s here?”

# Example 2: Long format (details)
# ls -l

# What it shows:

# File permissions

# Owner

# Size

# Last modified date

# Use when:

# You want more information about files

# Example 3: Show hidden files
# ls -a

# What it does:

# Shows all files, including hidden ones (. files)

# Use when:

# You’re checking config files like .gitignore

# Example 4: Combine options
# ls -la

# What it does:

# Long format + hidden files

# Most commonly used form in real work.

# 6. cd

# a. cd stands for "change directory"

# b. We use it to move up and down the directory/folder tree.

# Example 1: Move into a directory
# cd Documents

# What it does:
# Moves you from the current directory into the Documents folder.

# Example 2: Go to the parent directory

# cd ..

# What it does:

# Moves you one level up in the directory hierarchy.

# Example 3: Go to the home directory

# cd ~

# or simply:

# cd

# What it does:
# Takes you directly to your home directory, no matter where you are.

# Example 4: Use an absolute path

# cd /usr/local/bin

# What it does:

# Moves you to a directory using its full (absolute) path, starting from /.

# 7. mkdir

# a. mkdir stands for "make directory"

# b. We use it to create directory/folders.

# Example 1: Create a single directory

# mkdir projects

# Result:

# A folder named projects is created in the current directory

# When to use:

# Starting a new workspace

# Organizing files

# Example 2: Create multiple directories at once
# mkdir frontend backend docs

# Result:

# Three folders created:

# frontend

# backend

# docs

# Why this is useful:

# Faster setup

# Common in project initialization

# Example 3: Create nested directories (parent + child)
# mkdir -p src/components


# What -p means:

# p = parents

# Creates missing parent directories automatically

# Result:

# src/ is created (if it doesn’t exist)

# components/ is created inside src/

# ❌ Without -p, this would fail if src didn’t exist.

# Example 4: Create directories using a path

# mkdir ~/projects/web-design

# Result:

# Creates:

# projects/

# web-design/ inside it

# Location: home directory (~)

# Common real-world use:

# Organizing work by domain or client
