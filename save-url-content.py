import requests
from bs4 import BeautifulSoup
import json
import sys

def fetch_and_save_content(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text(separator=' ', strip=True)
        
        data = {"content": content}
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print("Data saved to {}".format(output_file))
    
    except requests.exceptions.RequestException as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <output_file>")
    else:
        url = sys.argv[1]
        output_file = sys.argv[2]
        fetch_and_save_content(url, output_file)
