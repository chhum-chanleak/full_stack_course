# 1. Git
# i. Git is a Version Control System(VCS).
# ii. Git is a tool that records snapshots of your project over time, so you can go back, compare, and collaborate safely.

# Example 1

# Git is like a “time machine” for your project

# Every time you commit, Git takes a snapshot of your project.

# You can go back in time, compare moments, or undo mistakes.

# If something breaks today, you can return to a version from yesterday.

# Key idea: history + recovery

# Example 2

# Git is like a “save system in a video game”

# Manual saves = commits

# Different save paths = branches

# Trying risky moves without ruining progress = branches

# Reloading an old save = checkout / reset

# Key idea: safe experimentation

# Example 3

# Git is like a “collaborative Google Docs with checkpoints”

# Many people work on the same files.

# Git tracks who changed what and when.

# If two people edit the same part, Git asks you to resolve it (merge conflicts).

# Key idea: teamwork + accountability

# Example 4

# Git is like a “lab notebook for code”

# Every experiment (change) is recorded.

# You can explain why you made a change (commit message).

# You can branch off to test an idea without polluting the main experiment.

# Key idea: structured progress tracking

# 3. git config
# i. "git config" = Git’s settings system
# ii. It defines (who you are, how Git behaves, and what tools it uses)

# Example 1 — Set your identity (who you are)

# Git needs to know who made a commit.

# git config --global user.name "Your Name"
# git config --global user.email "you@example.com"

# --global → applies to all repositories

# Stored in: ~/.gitconfig

# Used every time you run:

# git commit

# Example 2 — View your settings

# Check your configuration settings

# git config --list

# output:

# user.name=John Doe
# user.email=johndoe@example.com
# color.status=auto
# color.branch=auto
# color.interactive=auto
# color.diff=auto

# Example 3 — Change default branch name (behavior tweak)

# Modern Git uses main instead of master.

# git config --global init.defaultBranch main

# Affects:

# git init

# New repos will start with:

# main

# Example 4 — Create a shortcut (alias)

# Save typing, reduce friction.

# git config --global alias.st status

# Now this works:

# git st

# 3. Scopes of "git config"
#   3.1. System (--system) – applies to all users on the machine
#   3.2. Global (--global) – applies to the current user across all repos
#   3.3. Local (default) – applies only to the current repo. Local overrides global, global overrides system
