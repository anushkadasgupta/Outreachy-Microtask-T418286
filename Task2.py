import csv
import requests

def get_status_label(status_code):
    if status_code == 200:
        return "OK"
    elif status_code == 301:
        return "Moved Permanently"
    elif status_code == 302:
        return "Found"
    elif status_code == 303:
        return "See Other"
    elif status_code == 403:
        return "Forbidden"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Internal Server Error"
    else:
        return "Other"

with open("Task 2 - Intern.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        url = row["urls"].strip()

        if not url:
            continue

        try:
            response = requests.head(
                url,
                timeout=10,
                allow_redirects=True,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            if response.status_code >= 400:
                response = requests.get(
                    url,
                    timeout=10,
                    allow_redirects=True,
                    headers={"User-Agent": "Mozilla/5.0"}
                )

            label = get_status_label(response.status_code)
            print(f"({label}) {url}")

        except requests.exceptions.RequestException as e:
            print(f"({type(e).__name__}) {url}")
