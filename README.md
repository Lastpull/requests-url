# Tests were conducted only on Windows 10

# How to use:

Download latest version: https://github.com/Lastpull/requests-url/releases

A script to download files from a list of URLs.

## Usage

1. The file for changing the list of addresses is located at '_internal/urls.txt'. Add the list of URLs to download to this file. Add the list of URLs to download to this file.
2. Run the script, and it will download the files from the list.

## Requirements

* Python 3.x

## How the script works

1. The script reads the list of URLs from the `urls.txt` file.
2. For each URL, it sends a request to download the file, and the files are downloaded to the same directory where the script is located.
3. If an error occurs while downloading a file, the script displays an error message.
4. The script does not create duplicate files. If a file with the same name and extension already exists in the directory, it will simply overwrite it.