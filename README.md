# Outreachy-Microtask-T418286

## Overview

This repository contains the solution for **Outreachy Microtask T418286** as part of the project **"Addressing the Lusophone Technological Wishlist Proposals"**.

The objective of this task is to build a Python script that:

* Reads a list of URLs from a CSV file
* Sends an HTTP request to each URL
* Prints the response in a structured and human-readable format

### Output Format

```
(STATUS / MESSAGE) URL
```

### Example

```
(OK)  
(Not Found) 
(ConnectionError) 
```

---

## Python Implementation

### Step 1: Import Libraries

The script uses:

* `csv` for reading the CSV file
* `requests` for making HTTP requests

### Step 2: Read CSV File

* The file `Task 2 - Intern.csv` is opened using `utf-8-sig` encoding
* `csv.DictReader()` is used to parse rows as dictionaries

### Step 3: Extract URLs

* Each row contains a URL under the column `urls`
* Empty values are skipped

### Step 4: Send HTTP Requests

* A `HEAD` request is used to efficiently fetch response headers
* Redirects are followed automatically
* A fallback `GET` request is used when required

### Step 5: Interpret Responses

* HTTP status codes are mapped to meaningful labels such as:

  * `200 → OK`
  * `301 → Moved Permanently`
  * `302 → Found`
  * `303 → See Other`
  * `403 → Forbidden`
  * `404 → Not Found`
  * `500 → Internal Server Error`
* Unknown status codes are labeled as `Other`

### Step 6: Handle Exceptions

* Exceptions are caught using `requests.exceptions.RequestException`
* The exact exception type is printed (e.g., `Timeout`, `ConnectionError`)

### Step 7: Print Output

Each result is printed in the format:

```
(STATUS / MESSAGE) URL
```

---

## Technologies Used

* Python
* CSV module
* Requests library
* Git
* GitHub

---

## How to Run the Project

1. Install Python

2. Install dependencies:

```
pip install requests
```

3. Ensure both files are in the same directory:

* `Task2.py`
* `Task 2 - Intern.csv`

4. Run the script:

```
python Task2.py
```

or

```
py Task2.py
```

---

## Git Workflow

```
git init  
git add .  
git commit -m "Completed Microtask T418286"  
git branch -M main  
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git  
git push -u origin main  
```

---

## ✅ Status

✔️ Task completed successfully
✔️ URLs read from CSV file
✔️ Efficient HTTP requests implemented
✔️ Meaningful status messages displayed
✔️ Exceptions handled with detailed output
✔️ Code pushed to GitHub
