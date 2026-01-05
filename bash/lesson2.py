# 1. We use "touch" command to create files or update the timestamp of existing files.

# Example 1: Create a new empty file
# touch notes.txt

# What happens

# If notes.txt does not exist → it gets created as an empty file

# If it already exists → only its timestamp is updated

# Example 2: Create multiple files at once
# touch file1.txt file2.txt file3.txt

# Why this is useful

# Quickly scaffold files for a project

# Common in programming setups

# Example 3: Create a file inside a directory
# touch docs/readme.md

# Important

# The directory (docs/) must already exist

# Otherwise you’ll get an error

# Example 4: Update timestamp without changing content

# touch existing.log

# Use case

# Force a file to look “recently modified”

# Useful in build systems, scripts, or testing

# You can verify with:

# ls -l existing.log

# 2. rm
# i. "rm" stands for remove.
# ii. We use it to remove non-empty folders/directories.

# Example 1: Delete a single file
# rm notes.txt

# What happens

# notes.txt is permanently deleted

# Example 2: Delete multiple files at once

# rm file1.txt file2.txt file3.txt

# Use case

# Clean up several files quickly

# Example 3: Ask before deleting (safer)
# rm -i important.txt

# What -i does

# Prompts you: remove important.txt?

# Prevents accidental deletion

# Example 4: Delete a directory and everything inside it

# rm -r old_project

# What -r means

# Recursive deletion (directory + all contents)

# *Be very careful with this one.

# Common safety combo (recommended)
# rm -ri folder_name

# Recursive

# Interactive (asks before each deletion)

# 3. rmdir
# i. "rmdir" stands for "remove directory".
# ii. We use it to remove empty directories/folders.

# rmdir is used to delete empty directories only.

# If the directory is not empty, rmdir will fail.

# Syntax
# rmdir directory_name

# Example 1: Remove an empty directory
# rmdir logs

# What happens

# logs is deleted only if it’s empty

# Example 2: Remove multiple empty directories
# rmdir day1 day2 day3

# Use case

# Clean up several empty folders at once

# Example 3: Remove nested empty directories
# rmdir -p projects/app/src

# What -p does

# Removes src

# Then removes app if it becomes empty

# Then removes projects if it becomes empty

# Example 4: See an error when directory is not empty
# rmdir downloads

# Result

# Fails if downloads contains files or folders

# This is a safety feature, not a bug

# 4. cp
# i. "cp" stands for "copy".
# ii. We use it to copy files and directories.

# Example 1: Copy a file to another file
# cp notes.txt backup.txt

# What happens

# Creates backup.txt as a copy of notes.txt

# If backup.txt exists, it gets overwritten

# Example 2: Copy a file into a directory

# cp report.pdf documents/

# What happens

# A copy of report.pdf is placed inside documents/

# The directory must already exist

# Example 3: Copy multiple files into a directory

# cp a.txt b.txt c.txt archive/

# Use case

# Move several files into one folder (by copying)

# Example 4: Copy a directory and everything inside it
# cp -r project backup_project

# What -r means

# Recursive copy (directory + all subfiles/subfolders)
