#lx0b

# 1.
# What is another way we can call a folder?

# 2.
# What does a folder tree look like?

#lx0e

# Identify folders and files in the CLI:

# cat.png
# sorry.mp3
# music/
# lesson.txt
# videos/
# videos
# closer.mp4
# music

#lx0f

# 1. cd
# i. What does "cd" command stand for?
# ii. Why do we use it?

# a.
# Task:
# From your home directory, move into a folder called Documents.

# b.
# Task:
# From inside Documents, go back to your home directory.

# c.
# Task:
# From any directory, return to your home directory.

# d.
# Task:
# From your home directory, move into:
# projects/app

#lx0a

# Generate and store two passwords in Google password manager.

#lx0d

# 1.
# i. What does "ls" stand for?
# ii. Why do we use it?

# a.
# Task:
# List all visible files and folders in your current directory.

# b.
# Task:
# List files with details like permissions, size, and modification date.

# c.
# Task:
# Show all files, including hidden ones.

# d.
# Task:
# List all files with full details.

#lx0k

# 1. rmdir
# i. What does "rmdir" stand for?
# ii. Why do we use it?

# a.
# Task:
# Remove an empty directory named temp.

# b.
# Task:
# Remove three empty directories named jan, feb, and mar in one command.

# c.
# Task:
# Remove a nested directory projects/app/src, and also remove parent directories if they become empty.

# d.
# Task:
# You try to remove a directory named downloads, but it contains files.
# What command will fail, and why?

#lx0c

# 1.
# i. What does "pwd" stand for?
# ii. Why do we use it?

# a.
# Goal: Use pwd to identify your current directory.

# b.
# Move down one level from your current working directory.
# Goal: Use pwd to verify directory changes.

# c.
# Create and enter a folder:
# Goal: See how pwd reflects relative movement.

# d.
# Create nested folders a/b/c
# Move, then print when inside each directory.
# Goal: Understand full paths in nested directories.

#lx0h

# *For Windows OS only
# Practice on spot: Cursor movement (no selection)

# Move left (character) ←
# Move right (character) →
# Move up (line) ↑
# Move down (line) ↓
# Move one word left Ctrl + ←
# Move one word right Ctrl + →
# Move to line start Home
# Move to line end End
# Move to document start Ctrl + Home
# Move to document end Ctrl + End

#lx0g

# 1. mkdir
# i. What does "mkdir" stand for?
# ii. Why do we use it?

# a.
# Task:
# Create a directory named practice in your current location.

# b.
# Task:
# Create three directories named html, css, and js with one command.

# c.
# Task:
# Create a directory structure src/components/buttons, even if src does not exist yet.

# d.
# Task:
# Create a directory called bash-practice inside your home folder.

#lx0i

# 1. touch
# i. What does "touch" command do?

# a.
# Task:
# Create an empty file named todo.txt.

# b.
# Task:
# Create three files named index.html, style.css, and script.js in one command.

# c.
# Task:
# Update the timestamp of an existing file called server.log without modifying its content.

# d.
# Task:
# Create a file named notes.md inside a directory called projects.
# (Assume the directory already exists.)

#lx0j

# 1. rm
# i. What does "rm" command stands for?
# ii. Why do we use it?

# a.
# Task:
# Delete a file named old_notes.txt.

# b.
# Task:
# Delete three files named a.txt, b.txt, and c.txt using one command.

# c.
# Task:
# Delete a file named config.json, but make sure Bash asks for confirmation first.

# d.
# Task:
# Delete a directory named temp, including all files inside it, with confirmation prompts.

#lx0l

# 1. cp
# i. What does "cp" stands for?
# ii. Why do we use it?

# a.
# Task:
# Copy a file named data.txt to a new file called data_backup.txt.

# b.
# Task: Copy a file named photo.jpg into a directory called images.
# (Assume the directory already exists.)

# c.
# Task: Copy three files — a.js, b.js, and c.js — into a directory named scripts.

# d.
# Task: Copy a directory named project and all of its contents into a new directory called project_backup.

#lx0n

# 1. cat
# i. What does "cat" stand for?
# ii. Why do we use it?

# a.
# Task: Show the contents of notes.txt on the terminal.

# b.
# Task: Display a.txt and b.txt one after another.

# c.
# Task: Create a file called todo.txt and type content into it (Press Ctrl D to save).

# d.
# Task: Append the contents of part2.txt to the end of main.txt.

#lx0o

# 1. > (overwrite) vs >> (append)
# i. What does ">" do?
# ii. What does ">>" do?

# a.
# Task: Create a file called greetings.txt and write the text:
# Hello, world!

# b.
# Task: greetings.txt already exists. Replace its content with:
# Good morning!

# c.
# Task: Add a second line to greetings.txt that says:
# How are you today?

# d.
# Task: You have part1.txt and part2.txt. Append part2.txt to part1.txt.

#lx0q

# 1. echo
# i. Why do we use "echo"?

# a.
# Print the text "Hello, World!"" to the terminal.

# b.
# Print Loading... without moving to the next line.

# c.
# Assign your name to a variable NAME and then print "Hello, <NAME>! using echo.

# d.
# Print the following exactly as shown (including quotes):

# He said, "Bash is fun!"

#lx0v

# 1. grep
# i. What does "grep" stand for?
# ii. Why do we use it?

# a.
# Do these first:
# printf "cat\ndog\nfish\n" > animals1.txt
# printf "lion\ndog\ntiger\n" > animals2.txt

# Task: Search for "dog" in animals1.txt, and animals2.txt.

# b.
# Do this first:
# printf "error\nwarning\ninfo\nerror\n" > logs.txt

# Task: Invert search "error" in logs.txt.

# c.
# Task: Use "grep" with pipe "|" to search for ".txt" files only.

# d.
# Do this first
# printf "yes\nno\nYes\nyes\n" > answers.txt

# Task: Case-insensitively search for lines that contain "yes" inside answers.txt

#lx0p

# 1. less
# i. Why do we use "less"?

# a.
# You have a very large file called server.log.
# You want to read it safely and scroll up and down.

# Question:
# Which command should you use?

# b.
# A teammate says:

# “The issue is around line 120 in config.txt.”

# Question:
# Which command opens the file directly at that line?

# c.
# You opened app.log using less.
# You want to find the word error.

# Question:
# What exact keys do you press inside less?

# d.
# You want to read documentation for the ls command.

# Question:
# What command do you run, and what tool is used to display it?

#lx0u

# 1. Pipe "|"
# i. Why do we use pipe "|"?

# a.
# Do these first:
# 1. Create files a.txt, b.md, and c.pdf
# 2. Create directories named house, and room

# Task: Count how many files/directories are in your current directory using ls and a pipe.

# b.
# Task: List files/directories with details and show only the ones ending with ".md".

# c.
# Task: Print these words "apple\nbanana\ncherry" and only show the ones that contain the letter "a".

# d.
# Do these first:
# 1. printf "red apple\ngreen banana\nblue cherry" > fruits.txt

# Task: Show only lines containing “apple” from fruits.txt.

#lx0s

# 1. What does "set" do?

# a.
# Task: Use "set" alone and the see result.

# b.
# Task: Use "set" with "|" and "grep" to find a declared variable name "MY_VAR".

#lx0m

# 1. mv
# i. What does "mv" stand for?
# ii. Why do we use it?

# a.
# Task: You have a file named draft.txt. Rename it to final.txt.

# b.
# Task: Move report.pdf into the existing directory docs/.

# c.
# Task: Rename the directory images to assets.

# d.
# Task: Move a.txt, b.txt, and c.txt into the directory archive/.

#lx0r

# 1. variables
# i. Why do we use variables?

# a.
# Assign your favorite color to a variable named COLOR and print it.

# b.
# Create a variable NAME with your name and print:

# Hello, <NAME>! Welcome to Bash.

# c.
# Assign the number 5 to a variable X and 10 to a variable Y.
# Print their sum.

# d.
# Store the current date and time in a variable NOW and print it.

#lx0t

# 1. wc
# i. What does "wc" stand for?
# ii. Why do we use "wc"?

# Do this first:
# printf "red apple\ngreen banana\nblue cherry\nyellow pear" > book.txt

# a.
# Task: Default wc output of book.txt

# b.
# Task: Count lines in book.txt 
# *Note: "wc -l" counts "\n" not actual the number of lines in the file.

# c.
# Task: Count words in book.txt

# d.
# Task: Count characters (newline matters) in book.txt