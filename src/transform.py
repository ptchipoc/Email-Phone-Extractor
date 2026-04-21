import csv

def transform(emails: list[str], phones: list[str]):
    file_name = "results.csv"
    with open(file_name, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Type", "Value"])
        for email in emails:
            writer.writerow(["Email", email])
        for phone in phones:
            writer.writerow(["Phone", phone])