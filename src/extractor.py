from re import findall



def extract_email_phone(text: str) -> dict[list[str]]:
    email_regex = r'[\w\.-]+@[\w\.-]+\.\w+'
    phone_regex = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'

    emails = findall(email_regex, text)
    phones = findall(phone_regex, text)

    return {
        "emails": emails,
        "phones": phones
    }

# r'[\w\.-]+@[\w\.-]+\.\w+'
# r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
