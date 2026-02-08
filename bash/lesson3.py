# 1. mv
# i. "mv" stands for "move".
# ii. We use "mv" to :
#   1. "move" files or directories to a different location/directory.
#   2. "rename" files or directories.

# Example 1: Rename a file

# Task: Rename old.txt to new.txt.

# mv old.txt new.txt

# Same directory → treated as a rename

# Example 2: Move a file to another directory

# Task: Move file.txt into the docs/ directory.

# mv file.txt docs/

# File keeps the same name

# docs/ must already exist

# Example 3: Rename a directory

# Task: Rename directory project to project_backup.

# mv project project_backup

# Works for directories too

# Directory contents move automatically

# Example 4: Move multiple files into one directory

# Task: Move a.txt, b.txt, and c.txt into archive/.

# mv a.txt b.txt c.txt archive/

# Last argument must be a directory

# Common real-world use

# 2. cat
# i. "cat" stands for "concatenate".
# ii. We use it to view content of files. (cat filename.txt)

# What cat does

# cat = concatenate and display files

# In practice, it’s mostly used to:

# View file contents

# Combine files

# Create small files

# Basic Syntax

# cat [options] file1 file2 ...

# Example 1: View a file

# Task: Display the contents of notes.txt.

# cat notes.txt

# Prints the file to the terminal

# Example 2: View multiple files together

# Task: Display a.txt and b.txt in order.

# cat a.txt b.txt

# Contents are shown one after another

# Example 3: Create a file using cat

# Task: Create a file called todo.txt.

# cat > todo.txt

# Type your text, then press:

# Ctrl + D

# Saves the file

# *Overwrites existing file

# Example 4: Append one file to another

# Task: Append part2.txt to the end of main.txt.

# cat part2.txt >> main.txt

# Combines files

# Keeps existing content in main.txt

# *Important Tips

# For large files, use less instead of cat

# Use cat -n file.txt to show line numbers

# Be careful with > (overwrite) vs >> (append)

# 3. > (overwrite) vs >> (append)

# Core Concept

# Operator Meaning	Behavior
# >	Overwrite:	Creates a new file or replaces existing content
# >>	Append: Adds content to the end of an existing file; creates it if it doesn’t exist

# Think:

# > = replace everything

# >> = add to the end

# Example 1) pwd → current directory

# Overwrite
# pwd > dir.txt
# dir.txt now contains the path of the current directory, e.g.:
# /home/user/projects

# Append
# pwd >> dir.txt
# dir.txt now contains:
# /home/user/projects
# /home/user/projects

# Example 2) date → timestamp logging

# Overwrite
# date > timestamp.txt
# timestamp.txt contains only the current date/time

# Append
# date >> timestamp.txt
# timestamp.txt now has the old timestamp + new one

# Example 3) ls → directory listing

# Overwrite
# ls > dirlist.txt
# dirlist.txt has current directory contents only

# Append
# ls >> dirlist.txt
# dirlist.txt now has old list + new listing

# Example 4) cat → combine files

# Overwrite
# cat file1.txt > combined.txt
# combined.txt contains only file1.txt content

# Append
# cat file2.txt >> combined.txt
# combined.txt now has file1.txt + file2.txt

# 4. less
# i. less lets you read text one screen at a time and move around easily.

# Example 1: View a large file

# less file.txt

# Why this is useful:

# Safe (read-only)

# Handles very large files

# Scroll up and down freely

# Example 2: Open a file at a specific line

# less +50 file.txt

# What this does:

# Opens file.txt

# Jumps directly to line 50

# Very useful when:

# Someone says “check line 200”

# Debugging long files

# Example 3: Search inside a file

# less file.txt

# Inside less:

# Press /

# Type a word (e.g. error)

# Press Enter

# Navigation:

# n → next match

# N → previous match

# Example 4: Reading help pages

# man ls

# Important:

# Help pages open inside less

# Same keys work (Space, /, q)

# Knowing less means you know how to read Linux documentation.

# 5. echo/printf
# i. echo/printf prints text (or variables) to the terminal.

# Basic syntax:

# echo [options] [text]

# Example 1: Print plain text

# echo Hello, world!

# Output:

# Hello, world!

# This is the simplest use: printing a message.

# Example 2: Print multiple words

# echo This is Bash echo command

# Output:

# This is Bash echo command

# Everything after echo is printed as-is, separated by spaces.

# Example 3: Print a variable

# name="Alex"

# echo $name

# Output:

# Alex

# echo is commonly used to display variable values.

# $name means “replace this with the value of name”.

# Example 4: Print without a newline (-n option)

# echo -n "Loading..."

# Output:

# Loading...

# Normally echo adds a newline at the end.

# -n tells Bash not to move to the next line.

# Quick mental model

# Think of echo as:

# “Say this out loud in the terminal.”