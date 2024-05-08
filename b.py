import requests
import pandas as pd
from bs4 import BeautifulSoup

# def fetch_data(path,url):
#     r= requests.get(url)
#     with open(path,"w") as f:
#         f.write(r.text)

# url = "https://www.azbar.org/for-lawyers/practice-tools-management/member-directory/"
# # fetch_data("arizon.html", url)

with open("b.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser") 
# print(soup.title)   
# row = soup.select("div.row")
# row = str(row)
# with open("t.html", "w") as f:
#     f.write(row)

# print(soup.select("div#divResultsAttorney"))
# print(soup.div.get('class'))

# print(soup.find(class_ = 'row'))

# a = soup.find(id='divResultsAttorney')
# print(a)
# with open("b.txt", "w") as f:
#     f.write(a.text)

# a = soup.find_all("span", class_ = "col-sm-4")
# print(a)

# Find all divs with class 'col-sm-4'
col_sm_4_divs = soup.find_all('div', {'class': 'col-sm-4'})

# Find all span tags within each col-sm-4 div
all_span_tags = [div.find_all('span') for div in col_sm_4_divs]

all_h4_tags = [div.find_all('h4') for div in col_sm_4_divs]

# Extract data from class 'col-sm-6' for each col-sm-4 div
# for div in col_sm_4_divs:
#     # Find the next sibling div with class 'col-sm-6'
#     col_sm_6_div = div.find_next_sibling('div', {'class': 'col-sm-6'})
    
#     # Extract and print the text content
#     if col_sm_6_div:
#         print(col_sm_6_div.text.strip())

# Print the result
# for span_tags in all_span_tags:
#     for span_tag in span_tags:
#         print(span_tag.text)
        
# Create lists to store data
names = []
status = []
profile = []

# # extracting status 
# for span_tags in all_span_tags:
#     for span_tag in span_tags:
#         status.append(span_tag.text)

# # extracting names
# for h4_tags in all_h4_tags:
#     for h4_tag in h4_tags:
#         names.append(h4_tag.text)

# # Fill the 'names' list with empty strings for entries where 'h4' tag is not present
# for _ in range(len(all_span_tags) - len(names)):
#     names.append('')


# # Extract data from class 'col-sm-6' for each col-sm-4 div
# for div in col_sm_4_divs:
#     # Find the next sibling div with class 'col-sm-6'
#     col_sm_6_div = div.find_next_sibling('div', {'class': 'col-sm-6'})
    
#     # Extract and store the data
#     if col_sm_6_div:
#         # names.append(div.h4.text.strip())
#         profile.append(col_sm_6_div.text.strip())

# # Create a DataFrame
# df = pd.DataFrame({'Name': names, 'Status': status, 'Profile': profile})

# # Save to Excel file
# df.to_excel("output.xlsx", index=False)

# extracting status 
for span_tags in all_span_tags:
    for span_tag in span_tags:
        if span_tag.text == 'Active':
            status.append(span_tag.text)
       
# extracting names
for h4_tags in all_h4_tags:
    for h4_tag in h4_tags:
        names.append(h4_tag.text)

# Extract data from class 'col-sm-6' for each col-sm-4 div
for div in col_sm_4_divs:
    # Find the next sibling div with class 'col-sm-6'
    col_sm_6_div = div.find_next_sibling('div', {'class': 'col-sm-6'})
    
    # Extract and store the data
    if col_sm_6_div:
        profile.append(col_sm_6_div.text.strip())
    # else:
    #     profile.append('')  # Add an empty string if 'col-sm-6' is not found


# print(len(names))
# print(len(status))
# print(len(profile))

# # Make sure all lists have the same length
# max_length = max(len(names), len(status), len(profile))
# names += [''] * (max_length - len(names))
# status += [''] * (max_length - len(status))
# profile += [''] * (max_length - len(profile))

# print(len(names))
# print(len(status))
# print(len(profile))

# Create a DataFrame
df = pd.DataFrame({'Name': names, 'Status': status, 'Profile': profile})

# Save to Excel file
df.to_excel("output.xlsx", index=False)    
