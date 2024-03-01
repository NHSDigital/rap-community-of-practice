# prints all tags appearing in the .md files in /docs to terminal  
# run with: python utils/list-tags.py  
import os  
import re  

# Function to extract tags from a markdown file  
def extract_tags_from_file(file_path):  
    
    tags = []  
    with open(file_path, 'r') as file:  

        inside_tags = False  

        for line in file:  
            # check we have reached the tags property
            if line.strip().startswith('tags:'):  
                inside_tags = True
                continue
            
            # if we're not inside the tags property, keep looping
            if not inside_tags:
                continue

            # if the first character is not '-' then the line is no longer in the tags property - break
            if not line.strip().startswith('-'):
                break
# if the second character is '-' then we are on the '---' line which ends the front matter - break
            
            if line.strip()[1] == '-':
                break

            # Extract tag (removing leading "- ")  
            tag = line.strip()[2:]  
            tags.append(tag)  
              
    return tags  

# Get list of markdown files  
md_files = []  
for root, dirs, files in os.walk('docs'):  
    for file in files:  
        if file.endswith('.md'):  
            md_files.append(os.path.join(root, file))  

# Extract tags from each markdown file  
all_tags = []  
for file_path in md_files:  
    tags = extract_tags_from_file(file_path)  
    all_tags.extend(tags)  

# Remove duplicates and sort tags  
sorted_unique_tags = sorted(set(all_tags))  

# Print sorted tags list  
for tag in sorted_unique_tags:  
    print(tag) 