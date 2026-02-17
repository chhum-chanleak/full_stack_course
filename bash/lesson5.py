# 1. Brace expansion
# i. Brace expansion is a feature in Bash (and other shells like Zsh) that allows you to generate multiple strings from a pattern quickly.

# . It happens before globbing/wildcards.
# . It’s purely a text expansion, meaning it doesn’t care whether files actually exist.

# Example 1 — Simple list of strings

# echo file{A,B,C}.txt

# Output:

# fileA.txt fileB.txt fileC.txt

# Explanation:

# {A,B,C} expands into 3 separate strings

# Resulting command: echo fileA.txt fileB.txt fileC.txt

# Example 2 — Numeric range

# echo file{1..5}.txt

# Output:

# file1.txt file2.txt file3.txt file4.txt file5.txt

# Explanation:

# {1..5} expands into all integers from 1 to 5

# Very useful for generating numbered filenames.

# Example 3 — Combining letters and numbers

# echo file{A,B}{1,2}.txt

# Output:

# fileA1.txt fileA2.txt fileB1.txt fileB2.txt

# Explanation:

# Brace expansion is cartesian — every combination of the sets is generated

# You can nest multiple braces for complex patterns.

# Example 4 — Brace expansion with wildcards

# Files in the directory:

# file1.txt  file2.txt  fileA.txt  fileB.txt  fileC.txt

# Command:

# ls file{1,A}*.txt

# Step 1 (brace expansion): file1*.txt fileA*.txt

# Step 2 (globbing): matches actual files → file1.txt fileA.txt

# Explanation:

# Combines brace expansion + wildcards

# Generates multiple file patterns quickly without typing each manually.

# 2. Wildcards
# i. Wildcards are characters that trigger globbing (matching filenames).
# ii. These wildcards are *, ?, and [].

# Wildcard	Meaning:

# *	Matches 0 or more characters

# ?	Matches exactly 1 character

# [ ]	Matches exactly 1 character from a set or range

# 1. Asterisk * — match 0 or more characters

# Example 1 — List all .txt files:

# Files:

# report1.txt  report2.txt  summary.txt  notes.doc

# Command:

# ls *.txt

# Matches: report1.txt report2.txt summary.txt

# * matches any number of characters.

# Example 2 — List all files starting with data:

# Files:

# data1.csv  data2.csv  data10.csv  data_final.doc

# Command:

# ls data*

# Matches: data1.csv data2.csv data10.csv data_final.doc

# Matches everything starting with data.

# 2. Question mark ? — match exactly one character

# Example 3 — Match single-character suffix before .csv:

# Files:

# data1.csv  data2.csv  data10.csv  dataX.csv

# Command:

# ls data?.csv

# Matches: data1.csv data2.csv dataX.csv

# Ignores data10.csv (two characters → doesn’t match ?).

# Example 4 — Match files like logA.log or logB.log:

# Files:

# log1.log  log2.log  logA.log  logB.log  logAB.log

# Command:

# ls log?.log

# Matches: log1.log log2.log logA.log logB.log

# Ignores logAB.log (too many characters).

# 3. Brackets [ ] — match one character from a set or range

# Example 5 — Match specific characters:

# Files:

# img1.png  img2.png  imgA.png  imgB.png  imgC.png

# Command:

# ls img[12AB].png

# Matches: img1.png img2.png imgA.png imgB.png

# [12AB] matches exactly one character from the set.

# Example 6 — Match a range of characters:

# Files:

# fileA.txt  fileB.txt  fileC.txt  fileD.txt

# Command:

# ls file[A-C].txt

# Matches: fileA.txt fileB.txt fileC.txt

# [A-C] matches any single character from A to C.

# 3. Quoting
# i. In Bash, quoting controls how the shell interprets text.

# Example 1: No quotes (default behavior)

# name=Hello World
# echo $name

# What happens

# ❌ Error: World: command not found

# Why

# Bash splits on spaces

# It thinks:

# name=Hello

# then tries to run World as a command

# ✅ Correct version:

# name=Hello\ World

# Rule:
# Without quotes, spaces, globbing, and expansions all happen.

# Example 2: Double quotes " " (most commonly used)

# name="Hello World"
# echo "$name"

# Output

# Hello World

# What double quotes do

# Preserve spaces

# Still allow:

# Variable expansion ($name)

# Command substitution ($(...))

# Escape sequences (\n, \")

# Example:

# echo "Today is $(date)"

# Rule:
# Use double quotes when you want variables expanded but text kept together.

# Example 3: Single quotes ' ' (literal text)

# name="Alice"
# echo '$name is here'

# Output

# $name is here

# Why

# Single quotes disable everything

# No variables

# No commands

# No escapes

# Rule:

# Single quotes mean: “Take this text exactly as-is.”

# Best for:

# Regex

# Passwords

# SQL

# JSON

# Literal strings

# Example 4: Quotes vs globbing (*)

# echo *.txt

# Output (example)

# a.txt b.txt notes.txt

# Now with quotes:

# echo "*.txt"

# Output

# *.txt

# Why

# Without quotes: * expands (globbing)

# With quotes: treated as literal text

# Rule:
# Quotes prevent wildcard expansion.

# 4. Exit codes (return value)

# i. What are exit codes?

# Every command in Bash returns a number when it finishes — this is called the exit code.

# Convention:

# 0 → success

# Non-zero → failure (different numbers can indicate different types of errors)

# $? → special variable that holds the exit code of the last command

# ii. Why exit codes matter?

# They tell Bash whether a command succeeded or failed.

# && and || rely on exit codes.

# Scripts use exit codes for conditional execution and error handling.

# Example 1: Checking success

# mkdir my_folder
# echo $?   # prints 0 if folder created, non-zero if it failed

# Example 2: Using &&

# mkdir new_dir && echo "Created successfully"

# echo runs only if mkdir succeeded (exit code 0)

# Example 3: Using ||

# mkdir existing_dir || echo "Directory already exists"

# echo runs only if mkdir failed (exit code ≠ 0)

# Example 4: In scripts with conditional checks

# grep "hello" file.txt
# if [ $? -eq 0 ]; then
#     echo "Found 'hello'"
# else
#     echo "Did not find 'hello'"
# fi

# $? captures the exit code of grep

# 0 → string found, non-zero → string not found

# 5. Logical operators (&& / ||)
# i. && runs the next command only if the previous one succeeded.
# ii. || runs the next command only if the previous one failed.

# Example 1: && (AND)

# mkdir new_folder && echo "Folder created successfully"

# If mkdir new_folder succeeds → prints message

# If folder already exists → no message

# Example 2: || (OR)

# mkdir new_folder || echo "Folder already exists"

# If mkdir fails (folder exists) → prints message

# If mkdir succeeds → does not print

# Example 3: Combining && and ||

# mkdir project && echo "Created" || echo "Failed"

# If mkdir project succeeds → prints Created

# If mkdir project fails → prints Failed

# Warning: Be careful: this behaves differently in complex cases because echo "Created" can succeed, preventing || from running. Sometimes parentheses are needed.

# Example 4: Using with commands that might fail

# grep "hello" file.txt && echo "Found" || echo "Not found"

# If file.txt exists and contains "hello" → prints Found

# If not found → prints Not found

# 6. Basic scripts

# i. A basic Bash script is:

# A file containing Bash commands

# Executed top-to-bottom

# Driven by exit codes, not magic

# Minimum structure:

# #!/bin/bash
# commands...

# ii. Why we use basic Bash scripts?

# a. Automation

# Turn repeated manual commands into a single action

# Save time and reduce effort

# b. Preventing mistakes

# Enforce correct order of operations

# Stop execution when a critical step fails

# Reduce risk of running commands in the wrong place

# c. Encoding logic

# Store decisions and conditions in code instead of memory

# Let exit codes drive behavior

# d. Reproducibility

# Same script → same behavior every time

# Acts as automation + documentation

# e. Glue between tools

# Combine small Unix tools into a workflow

# Pipe and chain commands together

# f. Scalability

# Basic scripts naturally grow into:

# build scripts

# backup scripts

# deployment scripts

# monitoring scripts

# Example 1: Minimal script (structure)

# Create hello.sh

# Add the next two lines to hello.sh

# #!/bin/bash
# echo "Hello from Bash"

# What this teaches:

# Script structure

# echo prints output

# Script exits with 0 if nothing fails

# *Now invoke hello.sh by typing ./hello.sh (we include ./ because hello.sh is in the current directory)

# You'll see "zsh: permission denied: ./hello.sh"

# Because we have not made hello.sh executable. (Learn how to identify an executable file)

# *Note: By default, new files in Linux/macOS are not executable.

# To view mode of a file type: ls -l file_name

# How to make a file executable:

# chmod +x hello.sh

# Run hello.sh

# ./hello.sh

# Example 2: Basic automation

# Create make_logs.sh

# Add the next three lines to make_logs.sh

# #!/bin/bash
# mkdir logs
# echo "logs directory ready"

# Make make_logs.sh executable

# chmod +x make_logs.sh

# Run make_backup.sh a few times. (Take time to observe each run)

# What this teaches:

# Scripts remove repeated typing

# Commands run sequentially

# Example 3: Using exit codes for logic

# Create make_backup.sh

# Add the next two lines to make_backup.sh

# #!/bin/bash
# mkdir backup && echo "backup created" || echo "backup already exists"

# Make make_backup.sh executable

# chmod +x make_backup.sh

# Run make_backup.sh a few times. (Take time to observe each run)

# What this teaches:

# Commands return exit codes

# && and || act like simple if / else

# Logic is driven by success or failure

# Example 4: Guarding against failure (very important)

# Create move_to_project.sh

# Add the next three lines to move_to_project.sh

# #!/bin/bash
# cd project || exit 1
# echo "Now inside project directory"

# Make move_to_project.sh executable

# chmod +x move_to_project.sh

# Run move_to_project.sh a few times. (Take time to observe each run)

# What this teaches:

# Guard pattern

# Script stops if a critical step fails

# Prevents dangerous mistakes

# *Note: Observe your working directory(pwd) after running the script.