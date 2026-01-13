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
# ii. We use it to:.
#   1. View content of files. (cat filename.txt)
#   2. Create files with content 
#       or overwrite content of an existing file with new content. (> (overwrite))
#   3. Append/Add content to existing files. (>> (append))

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

# Example 1: Create a file with overwrite

# Task: Create file1.txt and write “Hello World”.

# cat > file1.txt

# Hello World

# Ctrl + D

# Result:

# file1.txt contains only:

# Hello World

# If file1.txt already existed, its old content is gone.

# Example 2: Overwrite an existing file

# Task: Replace content of file1.txt with “New Content”.

# cat > file1.txt

# New Content

# Ctrl + D

# Result:

# New Content

# Old content (“Hello World”) is deleted.

# Example 3: Append to an existing file

# Task: Add “Second Line” to file1.txt without removing existing content.

# cat >> file1.txt

# Second Line

# Ctrl + D

# Result:

# New Content

# Second Line

# Original content remains; new content added at the bottom.

# Example 4: Combine multiple files with append

# Task: Append contents of part2.txt to main.txt.

# cat part2.txt >> main.txt

# Result:

# main.txt now contains its original content plus everything from part2.txt at the end.

# Important: Using > here instead would replace main.txt completely with part2.txt.

# Quick Mental Shortcut

# > → “wipe and write”

# >> → “keep what’s there, add this at the end”

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