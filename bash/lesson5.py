# Quoting

# && / ||

# Exit codes (conceptual)

# Tiny scripts

# 1. Quoting
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

# 2. Logical operators (&& / ||)

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