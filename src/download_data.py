import urllib.request
import zipfile
import os

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"
RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

def download():
    os.makedirs(RAW_DIR, exist_ok=True)
    zip_path = os.path.join(RAW_DIR, "student.zip")
    print("Скачиваем датасет...")
    urllib.request.urlretrieve(URL, zip_path)
    print("Распаковываем...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(RAW_DIR)
    os.remove(zip_path)
    print("Готово! Файлы в папке data/raw/")
    print(os.listdir(RAW_DIR))

if __name__ == "__main__":
    download()
