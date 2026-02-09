# 1. Quoting
# i. Please explain what "Quoting" is in bash.

# a. Double quotes

# Suppose you have:

# greeting=Hello
# name=World

# Write a command using double quotes to output:

# Hello World

# b. Single quotes

# What will this output? Explain why:

# fruit=apple
# echo 'I have an $fruit'

# c. Prevent globbing

# You are in a folder with files:

# file1.txt  file2.txt  script.sh

# Write a command that literally prints:

# *.txt

# d. Combining quotes

# You want to assign this string to a variable exactly as shown, including quotes and $ signs:

# The price is $5

# Write a Bash assignment using quotes so that:

# echo price

# outputs exactly:
# The price is $5

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