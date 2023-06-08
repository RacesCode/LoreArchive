import json
import re
from datetime import datetime

# Open the JSON file
with open("messages.json", "r", encoding="utf-8") as f:
  lore = json.load(f)
# Define a regular expression to match URLs
url_regex = re.compile(r"(https?://\S+|www\.\S+)")

# Define a regular expression to match @ tags
at_regex = re.compile(r"@(\S+)")

# define list of names to tag
names = ['Aarand Vullan'
, 'Aarand'
, 'Khri Ettur'
, 'Khri'
, 'Roln'
, 'Armedius'
, 'Undel, Exiled King'
, 'Kyr'
, 'Ryn'
, 'Petyl'
, 'Mirh'
, 'Baz'
, 'H\'rol'
, 'Eri'
, 'Captain'
, 'Don'
, 'Gull'
, 'Xeno'
, 'Pavel'
, 'Ki'
, 'Cel'
, 'Rallyn'
, 'Irie'
, 'Egol'
, 'Tal'
, 'Jun'
, 'Barnib'
, 'Linim'
, 'Jov The God of Chance'
, 'Leon The Scholar'
, 'Riv'
, 'Ganren'
, 'King Tem'
, 'Kedrel'
, 'Fin'
, 'Y\'lyat'
, 'Vuli'
, 'Penm'
, 'Teagel '
, 'Nim'
, 'Sellira'
, 'Bell '
, 'Lez'
, 'Orel'
, 'Wendel'
, 'Ven Rallet'
, 'Cera Forethrell'
, 'Rib'
, 'Pipe'
, 'Judge Forethrell'
, 'Perin'
, 'Nym Blas'
, 'Wev'
, 'Visia'
, 'Jack'
, 'Samson'
, 'Gren'
, 'Rel'
, 'Fellren'
, 'Brint'
, 'Seers'
, 'Silvena'
        ]

# define list of place names to tag
places = [
     'Windfall'
, 'Wintrell'
, 'Fifteen'
, 'Eden'
, 'Outer Edge'
, 'Ysimji'
, 'Multiverse'
, 'Universe'
, 'Mivera'
, 'Veil'
, 'Pulse'
, 'Divide'
, 'Colorless Grove'
, 'Aether'
, 'Gentig'
, 'Aurium'
, 'Elrin'
]

# Define a function to process the content of a message
def process_content(content):
  # Remove URLs
  content = url_regex.sub("", content)
  
  # Remove @ tags
  content = at_regex.sub("", content)
  
  # Convert \n to new line
  content = content.replace("\\n", "\n")

  # Remove ; identifier
  content = content.replace(";","")

  # search for names and add [[]] tags
  for name in names:
    pattern = r'\b{}\b'.format(name)
    content = re.sub(pattern, f'[[{name}]]', content)
    
    return content

# Loop through the messages and create .md files for the ones that meet the criteria
count = 1
for messages in lore["messages"]:
  content = messages["content"]
  if messages["timestamp"] >= "2023-06-08":
    if ";" in content:
      filename = str(count).zfill(4) + ".md"
      with open(filename, "w", encoding="utf-8") as f:
        timestamp = messages["timestamp"][:10]
        content = process_content(content)
        f.write(f"**[{timestamp}]**\n\n**{content}**")
      count += 1