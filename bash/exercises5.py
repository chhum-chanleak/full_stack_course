# 1. Quoting
# i. Please explain what "Quoting" is in bash.

# a.
# You run the following in Bash:

# name=Hello World
# echo $name

# Questions:

# 1. What happens?

# 2. Why does it happen?

# 3. How do you fix it correctly?

# 4. What rule of Bash explains this behavior?

# b. Double quotes

# Suppose you have:

# greeting=Hello
# name=World

# Write a command using double quotes to output:

# Hello World

# c. Single quotes

# What will this output? Explain why:

# fruit=apple
# echo 'I have an $fruit'

# d. Prevent globbing

# You are in a folder with files:

# file1.txt  file2.txt  script.sh

# Write a command that literally prints:

# *.txt

# 2. Logical operators (&& / ||)
# i. && runs the next command only if the previous one succeeded.
# ii. || runs the next command only if the previous one failed.

# a.
# Create a directory called test_dir. If it succeeds, print:

# Directory created!

# Which operator should you use?

# b.
# Try to create a directory called existing_dir (assume it already exists). If creation fails, print:

# Directory already exists!

# Which operator should you use?

# c.
# Combine both operators in one line:

# Create project_dir

# If creation succeeds, print Created!

# If creation fails, print Failed!

# Write the one-line command.

# d.
# You have a file data.txt.

# If it exists, print File found!

# If it does not exist, print File missing!

# Hint: Use ls data.txt to check.

# 3. Exit code or return value

# i. What are exit codes?
# ii. Why exit codes matter?

# a.
# You run this command:

# mkdir my_folder

# How can you check whether it succeeded or failed immediately after running it?

# b.
# Predict the exit code:

# ls existing_file.txt
# echo $?

# What will $? print if the file exists?

# What if the file does not exist?

# c.
# You want to run a command only if the previous command succeeded. Which operator would you use?

# command1 ??? command2

# Fill in ??? to achieve this behavior.

# d.
# You run a script that returns a non-zero exit code. You want to print:

# Script failed!

# only if it failed. Write the Bash command using ||.

# 4. Basic scripts

# i. What is a basic script?
# ii. Why do we use basic Bash scripts?

# a. Script structure

# Create a Bash script that prints:

# Learning Bash

# Requirements:

# Include the correct shebang

# Use echo

# b. Simple automation

# Write a script that:

# Creates a directory called data

# Prints Data directory ready

# (No conditionals yet.)

# c. Exit-code based logic

# Write a script that:

# Tries to create a directory called backup

# Prints Backup created if successful

# Prints Backup already exists if it fails

# d. Guard pattern

# Write a script that:

# Changes into a directory called project

# If that fails, stop the script immediately

# If successful, print Inside project