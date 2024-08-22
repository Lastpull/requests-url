import requests
import os

def download_files(url_file):
    with open(url_file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]

    for url in urls:
        try:
            response = requests.get(url, stream=True)
            filename = url.split('/')[-1]
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {filename} successfully!")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    url_file = os.path.join(script_dir, 'urls.txt')
    download_files(url_file)