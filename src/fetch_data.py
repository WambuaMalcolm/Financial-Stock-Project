import os
import urllib.request as request
import zipfile

data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"

def download_file():
    filename, headers = request.urlretrieve(
        url=data_url,
        filename="articles.zip"
    )
    
    # Extract the zip file
    with zipfile.ZipFile("articles.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    
    # Remove the zip file after extraction
    if os.path.exists("articles.zip"):
        os.remove("articles.zip")

if __name__ == "__main__":
    download_file()