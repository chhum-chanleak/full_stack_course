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

# 2. What does "set" do?

# a.
# Task: Use "set" alone and the see result.

# b.

# Do this first:
# Create a variable named AGE which has a value of 12.

# Task: Use "set" with "|" and "grep" to find a declared variable name AGE.

# 3. wc
# i. What does "wc" stand for?
# ii. Why do we use "wc"?

# Do this first:
# printf "red apple\ngreen banana\nblue cherry\nyellow pear" > book.txt

# a.
# Task: Default wc output of book.txt

# b.
# Task: Count lines in book.txt 
# *Note: "wc -l" counts "\n" not the actual number of lines in the file.

# c.
# Task: Count words in book.txt

# d.
# Task: Count characters (newline matters) in book.txt

# 4. Pipe "|"
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
# Do this first:
# printf "red apple\ngreen banana\nblue cherry" > fruits.txt

# Task: Show only lines containing “apple” from fruits.txt.

# 5. grep
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
# Do this first:
# Create file1.txt, file2.md, a.txt, and b.md.

# Task: Use "grep" with pipe "|" to search for ".txt" files only.

# d.
# Do this first
# printf "yes\nno\nYes\nyes\n" > answers.txt

# Task: Case-insensitively search for lines that contain "yes" inside answers.txt

# e.
# Create files that have content like the following:

# a.txt

# dog
# cat
# bird

# b.txt

# fish
# horse

# c.txt

# doghouse

# Question:

# If you run:

# grep -l "dog" *.txt

# What will be printed?

# Take 20 seconds. Think carefully.