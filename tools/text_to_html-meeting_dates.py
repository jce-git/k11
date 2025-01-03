import re
import os
import datetime
import shutil

path_to_data = "html_code_data/meeting_dates/"

# variable that is responsible for the first part of the name of the file that will be created
beginning_of_file_name = "news"

# List of .txt files to check and read with optional custom paths
txt_files = {
    'html_start.txt': path_to_data,
    # '' stands for the current directory where the script is located
    'text_to_convert.txt': '',
    'html_end.txt': path_to_data,
    'news.html_page_replace.txt': path_to_data
}

# Function to read file content or create an empty file if it doesn't exist
def read_or_create_file(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Creating an empty file...")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('')
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Access the contents of each file
html_start, text_to_convert, html_end, news_html_page_replace = [
    read_or_create_file(f'{path}{file}') for file, path in txt_files.items()
]

# Mapping of locations to Google Maps links
location_links = {
    "Masoneria Szisza Bar": "https://www.google.com/maps/place/Masoneria+shisha+bar/@53.7760269,20.4699986,17z/data=!3m1!4b1!4m6!3m5!1s0x46e27f1e067b02ef:0xf5f51cdc05767785!8m2!3d53.7760238!4d20.4748641!16s%2Fg%2F11g0hm8247?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D",
    "Świetlica Rady Osiedla Dajtki, ul. Żytnia 71": "https://www.google.com/maps/place/%C5%BBytnia+71,+11-041+Olsztyn/@53.7647175,20.4262845,17.29z/data=!4m6!3m5!1s0x46e27f1111041ed5:0xb840e3620f3c52c4!8m2!3d53.7649399!4d20.4293494!16s%2Fg%2F11b8v4hpzl?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D"
}

# Function to generate HTML for each event
def generate_html(event):
    date, day, name, location, time = event
    location_link = location_links.get(location, "#")
    return f"""
    <p class="paragraph-header-01">{name}</p>
    <p>{date} ({day}), {time}</p>
    <p>w {location} - <a href="{location_link}" class="button-link">link do Google Maps !</a></p>
    <br>
    """

# Parse the input text
events = re.findall(r"(\d{2}\.\d{2}\.\d{4}r\.) \((.*?)\) (.*?) - (.*?), godz\. (.*?)$", text_to_convert, re.MULTILINE)

# Create output filename based on current date
today = datetime.date.today()
year, month, day = today.year, today.month, today.day
output_filename = f"{beginning_of_file_name}_{year:04d}.{month:02d}.{day:02d}.html"

# Add beginning of HTML code from html_start.txt to html_output
html_output = html_start

for event in events:
    html_output += generate_html(event)

# Add final information from html_end.txt
html_output += html_end

# Write the HTML output to the dynamically named file
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(html_output)

# Move the file to ../page/news folder
destination_folder = '../page/news/'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
shutil.move(output_filename, os.path.join(destination_folder, output_filename))

# Mapping of month numbers to Polish month names
polish_months = {
    1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec",
    7: "Lipiec", 8: "Sierpień", 9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"
}

# Dynamically create the link and add it to news_html_page_replace
month_name = polish_months[month]
news_html_page_replace = f'<p><a href="{output_filename}" class="button-link">{day:02d}.{month:02d}.{year} Plan spotkań - {month_name} {year}</a></p>\n'

# Copy news.html_page_replace.txt to current working directory and rename it to news.html
source_file = f'{path_to_data}news.html_page_replace.txt'
copied_file = 'news.html'
shutil.copy(source_file, copied_file)

# Read the contents of copied file
with open(copied_file, 'r', encoding='utf-8') as file:
    copied_content = file.readlines()

# Write the updated news_html_page_replace back to the file
with open(copied_file, 'a', encoding='utf-8') as file:
    file.write(news_html_page_replace)
    #print(news_html_page_replace)

# Read the updated contents of copied file
with open(copied_file, 'r', encoding='utf-8') as file:
    copied_content = file.readlines()

source_path = '../page/news/news.html'

# Read the source news.html file that will be compared with the copied file
with open(source_path, 'r', encoding='utf-8') as file:
    source_content = file.readlines()

# Find missing lines
missing_lines = [line for line in source_content if line not in copied_content]

# Remove the first line from missing_lines list if it starts with '<br>'
if '<br>' in missing_lines [0]:
    missing_lines.pop(0)

# Append missing lines to the copied file
if missing_lines:
    with open(copied_file, 'a', encoding='utf-8') as file:
        file.writelines(missing_lines)

# Rename the source (original) file to news_backup.html and move the copied_file
backup_path = os.path.join(destination_folder, 'news_backup.html')
if os.path.exists(backup_path):
    os.remove(backup_path)
os.rename(source_path, backup_path)
shutil.move(copied_file, source_path)

# Wait for user to press Enter
input("Press Enter to exit...")
