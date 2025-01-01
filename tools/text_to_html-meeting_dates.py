import re
import os
import datetime
import shutil

path_to_data = "html_code_data/meeting_dates/"

# variable that is responsible for the first part of the name of the file that will be created
beginning_of_file_name = "news"

# Check if html_start.txt exists, if not create an empty file
if not os.path.exists(f'{path_to_data}html_start.txt'):
    with open(f'{path_to_data}html_start.txt', 'w', encoding='utf-8') as file:
        file.write('')

# Read HTML template from html_start.txt
with open(f'{path_to_data}html_start.txt', 'r', encoding='utf-8') as file:
    html_start = file.read()

# Check if text_to_convert.txt exists, if not create an empty file
if not os.path.exists('text_to_convert.txt'):
    with open('text_to_convert.txt', 'w', encoding='utf-8') as file:
        file.write('')

# Read input from text_to_convert.txt
with open('text_to_convert.txt', 'r', encoding='utf-8') as file:
    text_to_convert = file.read()

# Check if html_end.txt exists, if not create an empty file
if not os.path.exists(f'{path_to_data}html_end.txt'):
    with open(f'{path_to_data}html_end.txt', 'w', encoding='utf-8') as file:
        file.write('')

# Read input from html_end.txt
with open(f'{path_to_data}html_end.txt', 'r', encoding='utf-8') as file:
    html_end = file.read()

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
events = re.findall(r"⛄️(\d{2}\.\d{2}\.\d{4}r\.) \((.*?)\) (.*?) - (.*?), godz\. (.*?)$", text_to_convert, re.MULTILINE)

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
destination_folder = '../page/news'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
shutil.move(output_filename, os.path.join(destination_folder, output_filename))
# Wait for user to press Enter
input("Press Enter to exit...")
