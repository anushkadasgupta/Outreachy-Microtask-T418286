import csv
import requests

with open("Task 2 - Intern.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        url = row["urls"]

        try:
            response = requests.get(url, timeout=10)
            print(f"({response.status_code}) {url}")
        except requests.RequestException:
            print(f"(ERROR) {url}")