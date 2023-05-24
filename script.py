import os
import random
import string
import subprocess

try:
    print("----------------------------------------------------------------------")
    
    print("""
██████╗ ██╗  ██╗ █████╗ ████████╗     █████╗  █████╗ ███████╗██╗███╗   ███╗
██╔══██╗██║  ██║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗██╔════╝██║████╗ ████║
██████╔╝███████║███████║   ██║       ███████║███████║███████╗██║██╔████╔██║
██╔══██╗██╔══██║██╔══██║   ██║       ██╔══██║██╔══██║╚════██║██║██║╚██╔╝██║
██████╔╝██║  ██║██║  ██║   ██║       ██║  ██║██║  ██║███████║██║██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚═╝
""")
    
    print("---------------------------------------------------------------------")
    print("\n[\033[1;32m+\033[1;37m] Twitter  ~ @bhataasim9\n")
    print("\n[\033[1;32m+\033[1;37m] Instagram ~ @bhataasim1\n")
    print("---------------------------------------------------------------------")
except:
    print("\n[\033[1;31m!\033[1;37m] The script do not require root privileges")
    exit(1)

def download_repo(url, folder_name):
    # Clone the repository using Git
    subprocess.run(["git", "clone", url, folder_name])

def generate_random_string(length=6):
    # Generate a random string of lowercase letters and digits
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    # Read the list of GitHub URLs from a text file
    with open('github_urls.txt', 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace
        folder_name = 'repo_' + generate_random_string()  # Generate a random folder name

        print(f"Downloading {url} to folder {folder_name}...")
        download_repo(url, folder_name)
        print("Download completed.\n")

if __name__ == '__main__':
    main()
