# 1. git push
# i. Why do we use "git push"?

# a. Basic push

# Scenario: You created lesson_03.py, added it, and committed locally. Your branch is main.

# Question: What command pushes your changes to the remote repository?

# b. Pushing a new branch

# Scenario: You created a branch feature/loops to add exercises. You committed loops_exercises.py.

# Question: What command pushes this branch and sets it to track the remote?

# c. Force push

# Scenario: You amended a commit on main (changed the message) and need to update the remote.

# Question: What command will safely overwrite the remote branch?

# d. Pushing a tag

# Scenario: You tagged a release v1.0 after finishing the exercises.

# Question: How do you push this tag to the remote repository?

# 2. git fetch
# i. Why do we use "git fetch"?

# a. Safe update check

# Scenario:
# You’re on main. You want to see if the remote repository has new commits without changing your code.

# Question:
# What command do you run?

# b. Inspect fetched changes

# Scenario:
# You already ran git fetch. You want to see commits that exist on the remote but not locally.

# Question:
# What command shows those commits?

# c. Fetch from a specific remote

# Scenario:
# Your repo has two remotes: origin and upstream. You want to update your knowledge of upstream.

# Question:
# What command do you run?

# d. Fetch, then integrate explicitly

# Scenario:
# You want full control: first see changes, then integrate them into main.

# Question:
# What is the correct command sequence?

# 3. git merge
# i. Why do we use "git merch"?

# a. Basic branch merge

# Scenario:
# You are on the main branch. A feature branch feature/arrays has been completed and needs to be integrated.

# Question:
# What command merges the feature branch into main?

# b. Merge remote changes after fetch

# Scenario:
# You ran git fetch and now want to integrate the latest remote changes from origin/main into your local branch.

# Question:
# What command do you run?

# c. Resolving merge conflicts

# Scenario:
# You merge a branch and Git reports conflicts in several files.

# Question:
# What is the correct sequence to finish the merge?

# d. Aborting a bad merge

# Scenario:
# You start a merge, conflicts appear, and you realize this merge should not happen yet.

# Question:
# What command safely cancels the merge and restores the previous state?

# 4. "merge conflict"

a. Same line edited differently

Scenario:
You are on main. A teammate changed line 10 in lesson.py while you also edited the same line. You attempt:

git merge feature/lesson


Git reports a conflict.

Question:
How do you resolve it?

b. File deleted on one branch, edited on another

Scenario:

On feature/cleanup, old_lesson.py was deleted.

On main, you edited old_lesson.py.

You run:

git merge feature/cleanup

Question:
What options does Git give, and how do you resolve?

c. Conflict during git pull

Scenario:
You run:

git pull

and Git reports a conflict in lesson_exercises.py.

Question:
What is the correct sequence to handle it?

d. Adjacent lines conflict

Scenario:
Two branches modified adjacent lines in loops.py. Git reports a conflict.

Question:
How do you resolve adjacent line conflicts safely?