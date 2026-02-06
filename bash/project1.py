# This project1 is ready for those who have learned lesson1.py, lesson2.py, exercises1.py and exercises2.py.

# Mini Project: Workplace Dev Environment Setup
# Scenario

# You just joined a company as a junior developer.
# Your task is to set up a local project workspace, organize files, and clean up mistakes—exactly what happens on day one at work.

# You are not writing code yet. You’re organizing the environment.

# 🎯 Project Goal

# Create a clean directory structure for a software project, add placeholder files, simulate mistakes, and fix them.

# 📁 Final Directory Structure (Target)
# company/
# ├── frontend/
# │   ├── index.html
# │   └── styles.css
# ├── backend/
# │   ├── app.js
# │   └── database.js
# ├── docs/
# │   └── README.md
# └── scripts/

# 🧠 Rules

# Use only: pwd, ls, cd, mkdir, touch, rm, rmdir, cp

# No shortcuts

# Check your location often (pwd, ls) like professionals do

# 🧩 Step-by-Step Tasks
# 🔹 Task 1: Confirm your location
# pwd
# ls


# Make sure you’re in your home directory.

# 🔹 Task 2: Create the company workspace
# mkdir company
# cd company
# ls

# 🔹 Task 3: Create department folders
# mkdir frontend backend docs scripts
# ls

# 🔹 Task 4: Create frontend files
# cd frontend
# touch index.html styles.css
# ls
# cd ..

# 🔹 Task 5: Create backend files
# cd backend
# touch app.js database.js
# ls
# cd ..

# 🔹 Task 6: Create documentation
# cd docs
# touch README.md
# ls
# cd ..

# ⚠️ Simulated Workplace Mistakes (Very Real)
# ❌ Mistake 1: Wrong file created

# You accidentally create a file in the wrong place:

# touch backend/README.md


# 👉 Fix it:

# rm backend/README.md

# ❌ Mistake 2: Duplicate file needed

# The frontend team wants a copy of index.html for testing.

# cp frontend/index.html frontend/index_test.html
# ls frontend

# ❌ Mistake 3: Unused folder

# The scripts folder is not needed anymore.

# rmdir scripts


# (Works because it’s empty—just like real cleanup rules.)

# ✅ Final Verification

# From inside company:

# ls
# ls frontend
# ls backend
# ls docs


# Make sure it matches the target structure above.

# 🧠 What This Project Taught You (Workplace Skills)

# Navigating confidently (pwd, cd)

# Creating clean project structure

# Managing files safely

# Fixing mistakes without panic

# Thinking like a developer, not just typing commands

# 🔍 Optional Challenge (No new commands)

# Create a backup copy of the entire docs folder inside company

# Name it docs_backup

# (Hint: cp can copy files one by one.)