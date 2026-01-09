# 1. Variables
# i. Variables in Bash store data (strings, numbers, paths, etc.) that you can use later in scripts or commands.

# Key points:

# No spaces around = when assigning:

# NAME=Alice  # ✅ correct
# NAME = Alice  # ❌ wrong

# Reference variables with $:

# echo $NAME

# By default, all variables are strings.

# Use export to make a variable available to child processes.

# Example 1: Basic variable

# NAME="Alice"
# echo "Hello, $NAME!"

# Output:

# Hello, Alice!

# Explanation:

# Assign a string to NAME

# Use $NAME to print its value

# Example 2: Numeric variable

# AGE=25

# echo "I am $AGE years old."

# Output:

# I am 25 years old.

# Explanation:

# Numbers are treated as strings unless used in arithmetic

# Bash doesn’t require explicit typing

# Example 3: Variables with command output

# DATE=$(date)

# echo "Today is $DATE"

# Output: (example)

# Today is Sat Jan 3 12:34:56 UTC 2026

# Explanation:

# $(command) captures the output of a command

# Assign it to a variable for later use

# Example 4: Add two variables

# A=5
# B=3

# SUM=$((A + B))
# echo $SUM

# Output: 8

# Key point:

# $(( ... )) tells Bash: this is arithmetic

# 2. set
#. We use "set" to view default and declared variables.

# Declare a variable
# my_name="Alice"

# Check all declared variables

# set

# output:

# BASH=/bin/bash
# HOME=/home/alice
# my_name=Alice
# ...

# 3. wc
# i. "wc" stands for "word count".
# ii. We use "wc" to count lines, words, and characters of files.

# Example 1 - Count lines, words, characters and show file name.

# echo "Hello, world\!" > greeting.txt

# wc greeting.txt

# Example 2 — Count lines in a file

# echo -e "apple\nbanana\ncherry" > fruits.txt

# wc -l fruits.txt

# Step by step:

# wc -l → counts lines

# fruits.txt has 3 lines → output: 3 fruits.txt

# Example 3 — Count words

# echo "apple banana cherry" > fruits.txt

# wc -w fruits.txt

# Step by step:

# wc -w → counts words

# 3 words → output: 3 fruits.txt

# Example 4 — Count characters

# echo "apple" | wc -c

# Step by step:

# echo "apple" → outputs apple plus a newline character

# wc -c → counts characters including newline

# Output: 6

# (5 letters + 1 newline)

# 4. pipe "|"
# i. We use pipe "|" to send the output of one command as input to another

# Symbol: |

# Think of it as a conveyor belt for data

# Syntax:

# command1 | command2

# command1 produces output

# command2 processes that output

# Example 1 — List files and count them

# ls | wc -l

# ls → lists files in current directory

# wc -l → counts lines

# Pipe passes the file list from ls to wc -l

# Output = number of files

# Example 2 — Filter files with grep

# ls -l | grep ".sh"

# ls -l → lists files with details

# grep ".sh" → shows only files ending with .sh

# Pipe passes the full file list to grep

# Example 3 — Filter words containing “a”

# echo -e "cat\ndog\napple\nbanana" | grep "a"

# Step by step:

# echo -e "cat\ndog\napple\nbanana" → prints 4 words, each on a new line

# | grep a → keeps only lines containing "a"

# Output:

# cat
# apple
# banana

# Example 4 — Filter lines from a file using cat

# cat fruits.txt | grep "apple"

# Step by step:

# cat fruits.txt → prints all lines in the file

# | grep "apple" → only shows lines containing “apple”

# Output: whatever lines in fruits.txt have “apple”

# Note: cat is optional here — you can also do grep apple fruits.txt — but this shows how pipes work.

# 5. grep
# i. "grep" stands for "Global Regular Expression Print"
# ii. "grep" searches for lines that match a pattern.

# Syntax:

# grep [options] PATTERN file

# It prints entire lines that contain the pattern.

# Example 1 — Search for a word in a file

# printf "apple\nbanana\ncherry\n" > fruits.txt

# grep "banana" fruits.txt

# Output

# banana

# Why

# grep scans each line

# Prints the line containing "banana"

# Example 2 — Case-insensitive search (-i)

# printf "Hello\nhello\nHELLO\n" > hello.txt

# grep -i "hello" hello.txt

# Output: 

# Hello
# hello
# HELLO

# Why

# -i ignores letter case

# All variations match

# Example 3 — Search from command output (pipe)

# ls | grep ".py"

# Output

# lesson1.py
# lesson2.py
# exercises1.py

# Why

# ls → list files

# grep ".py" → keep only lines containing .py

# Example 4 — Exclude matching lines (-v)

# printf "pass\nfail\npass\nfail\n" > results.txt

# grep -v "fail" results.txt

# Output
# pass
# pass

# Why

# grep normally keeps matching lines

# -v inverts the match

# Lines containing "fail" are excluded

# Only lines not matching "fail" are printed