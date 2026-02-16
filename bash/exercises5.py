# 1. Brace expansion
# i. What is brace expansion?

# a. Simple list of strings

# Create the following files:

# fileA.txt fileB.txt fileC.txt

# Task:
# Write a command using brace expansion to echo filenames above.

# b. Numeric range

# Create the following files:

# file1.txt file2.txt file3.txt file4.txt file5.txt

# Task:
# Write a command using brace expansion to echo filenames above.

# c. Combining letters and numbers

# Create the following files:

# fileA1.txt fileA2.txt fileB1.txt fileB2.txt

# Task:
# Write a command using nested braces to echo files above.

# d. Brace expansion with wildcards

# Create the following files:

# file1.txt file2.txt fileA.txt fileB.txt fileC.txt

# Task:
# Write a command using brace expansion combined with a wildcard to list files starting with file1 or fileA ending in .txt.

#lx0aa

# 2. Wildcards
# i. Why do we use them?
# ii. Name them.

# a. Asterisk *

# Create these files in your directory:

# report1.txt report2.txt summary.txt notes.doc

# Task:
# Write a command using * to list all .txt files.

# b. Asterisk *

# Create these files in your directory:

# data1.csv data2.csv data10.csv data_final.doc

# Task:
# Write a command using * to list all files starting with data.

# c. Question mark ?

# Create these files in your directory:

# data1.csv data2.csv data10.csv dataX.csv

# Task:
# Write a command using ? to list files with exactly one character after data and before .csv.

# d. Question mark ?

# Create these files in your directory:

# log1.log log2.log logA.log logB.log logAB.log

# Task:
# Write a command using ? to list files like logA.log or logB.log, but not logAB.log

# e. Brackets [ ]

# Create these files in your directory:

# img1.png img2.png imgA.png imgB.png imgC.png

# Task:
# Write a command using [ ] to list files above which contain 1, 2, A, or B.

# f. Brackets [ ] (range)

# Create these files in your directory:

# fileA.txt fileB.txt fileC.txt filed.txt

# Task:
# Write a command using [ ] to list files ending with A to C.

# 3. Quoting
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

# 4. Exit code (return value)

# i. What are exit codes?
# ii. Why exit codes matter?

# a.
# You run this command:

# mkdir my_folder

# How can you check whether it succeeded or failed immediately after running it?

# b.

# Run this command:

# touch existing_file.txt

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

# Assume you run a script that returns a non-zero exit code. You want to print:

# "Script failed!"

# Which logical operator would you use?

# 5. Logical operators (&& / ||)
# i. When does && run the next command in Bash?
# ii. When does || run the next command in Bash?

# a.

# *Do the following but do not press Enter or run.

# Create a directory called test_dir. If it succeeds, print:

# Directory created!

# Which operator should you use?

# b.

# Create a directory call existing_dir

# Try to create it again (do not press Enter or run). If creation fails, print:

# Directory already exists!

# Which operator should you use?

# c.
# Combine both operators in one line:

# *Do the following but do not press Enter or run.

# Create project_dir

# If creation succeeds, print Created!

# If creation fails, print Failed!

# Write the one-line command.

# d.

# Create a file data.txt.

# *Do the following but do not press Enter or run.

# Use ls to search for data.txt

# If it exists, print "File found!"

# If it does not exist, print "File missing!"

# 6. Basic scripts

# i. What is a script?
# ii. Why do we use Bash scripts?

# a. Script structure

# Create a Bash script file named say_learning_bash.sh that prints:

# "Learning Bash"

# Requirements:

# Include the correct shebang

# Use echo

# b. Simple automation

# Create a script file named mkdir_data.sh that:

# Creates a directory called data

# Prints "data directory ready"

# (No conditionals yet.)

# c. Exit-code based logic

# Create a script file named mkdir_backup.sh that:

# Tries to create a directory called backup

# Prints "backup created" if successful

# Prints "backup already exists" if it fails

# d. 

# Create a script file named cd_project.sh that:

# Changes into a directory called project

# If that fails, stop the script immediately

# If successful, print "Inside project"

# 7. Make scripts inside each of these directories executable everywhere:

# . Go to your home directory(~)
# . Create one script file for each of following directories and make each script executable everywhere.

# a. app

# b. ban

# c. che

# d. dat

# . It should be like this:

# app/app.sh
# ban/ban.sh
# che/che.sh
# dta/data.sh

# . When run each script, it should look like this:

# app.sh -> "Hello, app"
# ban.sh -> "Hello, ban"
# che.sh -> "Hello, che"
# data.sh -> "Hello, data"