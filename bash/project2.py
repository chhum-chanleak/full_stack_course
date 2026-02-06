# This project2 is ready for those who have learned lesson3.py, lesson4.py, exercises3.py and exercises4.py.

# Workplace Bash Project: Dev Workspace + Logs
# Scenario

# You join a team maintaining a small internal tool.
# Your task is to inspect logs, configure files, reorganize resources, and produce simple reports.

# 🎯 Final Goals

# Create and modify config files

# Generate and append logs

# Move files into correct locations

# Inspect large files safely

# Search logs for issues

# Count lines/words/errors

# 📁 Starting Structure (assume it exists)
# project/
# ├── app.log
# ├── config.txt
# ├── temp.log
# └── notes.txt

# If it doesn’t exist, your instructor/team lead already created it for you.

# cd into project before starting.

# 🧩 Task 1: Initialize configuration (variables + echo)
# Step 1: Define environment variables
# APP_NAME="inventory-service"
# ENV="development"
# PORT=8080

# Step 2: Write config file (overwrite)
# echo "APP_NAME=$APP_NAME" > config.txt
# echo "ENV=$ENV" >> config.txt
# echo "PORT=$PORT" >> config.txt

# Step 3: Verify
# cat config.txt

# 🧩 Task 2: Simulate application logs (append safely)
# Step 1: Add startup logs
# echo "INFO: App starting..." >> app.log
# echo "INFO: Listening on port $PORT" >> app.log

# Step 2: Add runtime logs
# echo "WARN: Cache miss" >> app.log
# echo "ERROR: Database connection failed" >> app.log
# echo "INFO: Retrying connection" >> app.log

# 🧩 Task 3: Inspect logs like a professional
# View entire file (small logs)
# cat app.log

# View safely (realistic logs)
# less app.log

# (use q to quit)

# 🧩 Task 4: Search for issues (grep)
# Find errors
# grep "ERROR" app.log

# Find warnings + errors
# grep -E "WARN|ERROR" app.log

# 🧩 Task 5: Generate a simple report (pipe + wc)
# Count total log lines
# cat app.log | wc -l

# Count error lines only
# grep "ERROR" app.log | wc -l

# Count warning + error lines
# grep -E "WARN|ERROR" app.log | wc -l

# 🧩 Task 6: Reorganize files (mv)
# Move temp log out of the way
# mv temp.log temp.log.bak

# Rename notes
# mv notes.txt developer_notes.txt

# (Real teams rename files constantly.)

# 🧩 Task 7: Append audit info (printf)
# printf "Audit: Checked logs on %s\n" "$(date)" >> app.log

# (If date is unavailable, just write text.)

# 🧠 What This Project Simulates (Very Real)

# Config initialization

# Log generation & inspection

# Safe file viewing (less)

# Searching production logs

# Producing quick metrics

# Renaming and organizing files

# Using variables instead of hardcoding

# 🧪 Optional Challenge (No new commands)

# Create a file called error_report.txt

# Store only ERROR lines inside it

# Count how many lines it has

# (Hint: grep, >, wc)
