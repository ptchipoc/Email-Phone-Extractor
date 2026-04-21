import sys
from src.utils import load_text
from src.extractor import extract_email_phone
from src.transform import transform

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Args should be more the one")
        exit(1)
    text = load_text(argv[1])
    clean_content = extract_email_phone(text)
    transform(clean_content["emails"], clean_content["phones"])
