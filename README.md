# Outreachy-Microtask-T418286

## Overview

This repository contains the solution for **Outreachy Microtask T418286** as a part of the project "Addressing the lusophone technological wishlist proposals"

The objective of this task is to create a Python script that:
- Reads a list of URLs from a CSV file
- Sends an HTTP request to each URL
- Prints the status code of the response in the format:

(STATUS CODE) URL

Example:

(200) https://example.com  
(404) https://example.com/page  
(ERROR) https://broken-link.com  

---

## Python Implementation

### Step 1: Import Libraries
The script uses:
- `csv` to read the CSV file  
- `requests` to send HTTP requests  

### Step 2: Open CSV File
The file `Task 2 - Intern.csv` is opened using Python.

### Step 3: Read Data
- `csv.DictReader()` is used  
- Each row is treated as a dictionary  
- URLs are accessed using the column name  

### Step 4: Loop Through URLs
A `for` loop processes each URL one by one.

### Step 5: Send Request
- `requests.get(url)` is used  
- A timeout is added to avoid delays  

### Step 6: Print Output
The output is printed in this format:

(STATUS CODE) URL

### Step 7: Handle Errors
If any request fails:

(ERROR) URL

---

## Technologies Used

- Python  
- CSV module  
- Requests library  
- Git  
- GitHub  

---

## How to Run the Project

1. Install Python  
2. Install dependencies:

pip install requests  

3. Ensure both files are in the same folder:
- Task2.py  
- Task 2 - Intern.csv  

4. Run the script:

python Task2.py  

or

py Task2.py  

---

## Git Workflow

git init  
git add .  
git commit -m "Completed Microtask T418286"  
git branch -M main  
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git  
git push -u origin main  

---

## Status

- Task completed successfully  
- URLs read from CSV file  
- HTTP status codes printed correctly  
- Errors handled properly  
- Code pushed to GitHub  

---
