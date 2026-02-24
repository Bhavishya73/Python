# web Intellgent scrapper

import json
import requests
import pandas as pd
from pathlib import Path

# function to the files in current folder
def filepath():
    path = Path('.')
    items = list(path.rglob('*'))
    for index , value in enumerate(items):
        print(f'{index}. {value}')

# function to extract the data from url
def extract_data(url):
    response = requests.get(url)
    data = response.json()
    
    # check the data is in dict or list
    if isinstance(data , dict):
        print(" Dictonary Format Data ")
        for i , key in enumerate(data.keys()):
            print(f'{i}. {key}')
    elif isinstance(data , list):
        print(" List Format Data ")
        for i  in enumerate(data):
            print(f'{i}. ')  

    return data 

# function to create file
def save_data( filename , choice):

    # getting data from extract_data function
    data = extract_data(url)

    try:
        # loop to iterate items in dict
        if isinstance(data  ,  dict):
            for i , (key , value) in enumerate(data.items()):
                if choice == i:
                    print(f'{key} : {value}')
                    # using path to take the file
                    p = Path(filename)
                    # checking some conditions
                    if p.exists() and p.stat().st_size > 0:
                        with open(filename , 'r') as f:
                            data = json.load(f)
                    else:
                        data = []

                    data.append({key : value})
                    print("New Data is Append Successfully !!! ")

                    with open(filename , 'w' , encoding='utf-8') as file:
                        json.dump(data , file , indent=4)
                        # print("New File Created Successfully !!! ")

                    return


        elif isinstance(data , list) :
            for i , value in enumerate(data):
                if choice == i:
                    print(f'{i}. {value}')
                    # using path to take the file
                    p = Path(filename)
                     # checking some conditions
                    if p.exists() and p.stat().st_size > 0:
                        with open(filename , 'r') as f:
                            data = json.load(f)
                    else:
                        data = []

                    # ensuring the data
                    if not isinstance(data , list):
                        data = [data]

                    data.append(value)
                    print("New Data is Append Successfully !!! ")

                    with open(filename , 'w' , encoding='utf-8') as f:
                        json.dump(data , f , indent=4 )
                        # print("New File creted Successfully !!! ")

                    return
                
        else : 
            print("Invalid Choice !!! ")

    except ValueError:
        print('Error to enter valid input ')    


# functon to convert json to exel 
def export_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = []

    # Case 1: JSON is list
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                for value in item.values():
                    if isinstance(value, list):
                        records.extend(value)   # 👈 collect all

    # Case 2: JSON is dict
    elif isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list):
                records.extend(value)

    if not records:
        raise ValueError("Unsupported JSON format: no list of records found")

    df_new = pd.json_normalize(records)

    excel_file = Path("raw.xlsx")

    if excel_file.exists():
        print("raw.xlsx already exists → updating file...")

        df_old = pd.read_excel(excel_file)
        df_final = pd.concat([df_old, df_new], ignore_index=True)

    else:
        print("raw.xlsx not found → creating new file...")
        df_final = df_new

    df_final.to_excel(excel_file, index=False)
    print("Excel Sheet Created/Updated Successfully !!!")



# fuction to clean the excel file raw data
def clean_data():
    excel_file = Path("raw.xlsx")

    df = pd.read_excel(excel_file)

    # ---------- Remove duplicates ----------
    print("Removing Duplicate values")
    total_before = len(df)
    duplicate = df[df.duplicated()]
    print("Total Data:", total_before)
    print("Total Duplicate Data:", len(duplicate))

    df.drop_duplicates(inplace=True)
    print("After Removing Duplicate Data:", len(df))

    # ---------- Remove empty values ----------
    print("\nRemoving Empty values")
    total_before_na = len(df)
    df.dropna(inplace=True)
    print("Total Missing Data:", total_before_na - len(df))
    print("After Removing Missing Data:", len(df))

    # ---------- Save cleaned file ----------
    filename = "Cleaned_data.xlsx"

    # ✅ DO NOT open with open()
    df.to_excel(filename, index=False)

    print("Data Exported Successfully")



# main code 
while True:
    print('-------Menu---------')
    print('1. Fetch Data')
    print('2. Save Data')
    print('3. Export Data')
    print('4. Cleaned Data')
    print('5. Exit')
    print('---------------------')

    try:
        res = int(input('Enter your choice : '))
    except ValueError:
        print('Invalid Choice .... ')

    match res:
        case 1:
            url = input('Enter the Url to fetch [Json only] : ')
            extract_data(url)

        case 2:
            print('File exixt in Folder - ')
            filepath()
            print('Saving Data ')
            choice = int(input('Enter your fetch choice : '))
            filename = input('Enter the filename : ' )
            save_data(filename , choice)

        case 3:
            print('Export the data')
            filename = input('Enter filename for json to excle : ')
            export_data(filename)

        case 4:
            print("Cleaning Data")
            clean_data()

        case 5:
            print('Thank You ')
            break

        case _:
            print('Invalid Choice ')