from bs4 import BeautifulSoup

with open("b.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

data_list = []

for person_div in soup.find_all('div', {'id': 'divResultsAttorney'}):
    person_name = person_div.find('h4').text.strip() if person_div.find('h4') else ''
    active_status = person_div.find('span', {'style': 'font-size:.8em;'}).text.strip() if person_div.find('span', {'style': 'font-size:.8em;'}) else ''
    
    profile_div = person_div.find_next_sibling('div', {'class': 'col-sm-6'})
    profile_info = profile_div.text.strip() if profile_div else ''

    data_list.append(f"{person_name} - {active_status}\n{profile_info}\n\n")

# Save data to a text file
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.writelines(data_list)