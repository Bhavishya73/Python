# Web Scrapper

import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

# function to see current folder files
def all_files():
    path = Path('.')
    items = list(path.rglob('*'))
    for index , value in enumerate(items):
        print(f'{index}.  {value}')

# class to inherit data
class Extract:
    def extract_data(self, url):

        # 🔹 stream=True is REQUIRED for real progress bar
        response = requests.get(url, stream=True)

        total_size = int(response.headers.get("Content-Length", 0))
        chunks = []

        # 🔹 Progress bar while downloading
        with tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading") as bar:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    chunks.append(chunk)
                    bar.update(len(chunk))

        content = b"".join(chunks)

        # 🔹 Detect content type
        content_type = response.headers.get("Content-type", "").lower()

        if "application/json" in content_type:
            data = json.loads(content.decode("utf-8", errors="ignore"))

            filename = "data.json"

            if Path(filename).exists():
                with open(filename, "r", encoding="utf-8") as f:
                    try:
                        data_list = json.load(f)
                    except json.JSONDecodeError:
                        data_list = []
            else:
                data_list = []

            data_list.append(data)

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data_list, f, indent=4, ensure_ascii=False)

        else:
            html = content.decode("utf-8", errors="ignore")
            soup = BeautifulSoup(html, "html.parser")

            filename = "index.html"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(soup.prettify())


    def view_data(self,filename):
        p = Path(filename)
        if p.exists():
            with open(p , 'r' , encoding="utf-8") as f:
                print(f.read())
        else :
            print('File not Exixtes')

    def export_data(self,filename):
        with open(filename , 'r' , encoding="utf-8") as f:
            data = json.load(f)

        all_results = []

        for item in data:
            all_results.extend(item["results"])

        df = pd.json_normalize(all_results)
        df.to_excel("output.xlsx", index=False)
        print('Data Exported Successfully ')

   

e = Extract()


# main code
while True:
    print('----------- Menu ------------')
    print('1. Extract Data')
    print('2. View Scraped Data ')
    print('3. Export Data ')
    print('4. Exit')
    print('------------------------------')

    try :
        choice = int(input('Enter your Choice : '))
    except ValueError:
        print('Invalid Choice ')

    match choice:
        case 1:
            url = []
            # to get urls 
            n = int(input('Enter no of url you want ? '))
            for i in range(n):
                i = input("Enter urls : ")
                url.append(i)
            # to rtact data from url 1 by 1
            for u in tqdm(url , desc="Fetching Data "):
                e.extract_data(u)

        case 2:
            print('Folder Files ')
            all_files()
            filename = input("Enter the file name : ")
            e.view_data(filename)

        case 3:
            print('Export Data')
            all_files()
            filename = input('Enter the file name to convert [json only] : ')
            e.export_data(filename)

        case 4:
            print('Thank you ')
            break

        case _:
            print('Invalid Choice ')