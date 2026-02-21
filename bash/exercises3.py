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

# 2. cat
# i. What does "cat" stand for?
# ii. Why do we use it?

# a.
# Do these first:
#   1. Create colors.txt
#   2. Write "red, green, blue" in colors.txt

# Task: View colors.txt

# b.
# Do these first:
#     1. Create fruits.txt
#     2. Write "apple, banana, cherry" in fruits.txt

# Task: View colors.txt and fruits.txt files together

# c.
# Do these first:
#     1. Create days.txt
#     2. Write "Monday"
#              "Tuesday"
#              "Wednesday" in days.txt (3 lines in total).

# Task: Display content of days.txt with line numbers

# d.
# Task: Create file.md using "cat >"" then write "Hello, world!" in it (Press Ctrl + D two times to save) and view file.md.

# e. 
# Task: Append "Hello, again" to file.md using "cat >>" and view file.md.

# 3. > (overwrite) vs >> (append)
# i. What does ">" do?
# ii. What does ">>" do?

# a.
# What happens if notes.txt already exists and you run:

# echo "Hello" > notes.txt

# A) “Hello” is added to the end
# B) The old content is deleted and replaced
# C) Command fails

# b.
# What happens if log.txt does NOT exist and you run:

# date >> log.txt

# A) Error
# B) File is created and date is written
# C) Nothing happens

# c.
# You want to keep a running history of timestamps. Which operator should you use?

# d.
# You want to reset a file and start fresh. Which operator?

# e.
# Assume file.txt initially contains:

# Apple
# Banana

# echo "Cherry" > file.txt

# What does file.txt contain now?

# f.
# Reset the file back to:

# Apple
# Banana

# Then run:

# echo "Cherry" >> file.txt

# What does file.txt contain now?

# g.
# Assume combined.txt does NOT exist.

# cat file.txt > combined.txt
# cat file.txt >> combined.txt

# What does combined.txt contain?

# h.
# You are building a simple bash logger:

# echo "Server started" ___ server.log

# You want to preserve previous logs.

# Which operator goes in the blank?

# i.
# You accidentally run:

# ls > important.txt

# But important.txt had critical data.

# What just happened?

# 4. less
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
# You want to read documentation for the "ls" command.

# Question:
# What command do you run, and what tool is used to display it?

# 5. echo
# i. Why do we use "echo"?

# a.
# Print the text Hello, World! to the terminal.

# b.
# Print Loading... without moving to the next line.

# c.
# Assign your name to a variable NAME and then print Hello, <NAME>! using echo.

# d.
# Print the following exactly as shown (including quotes):

# He said, "Bash is fun!"