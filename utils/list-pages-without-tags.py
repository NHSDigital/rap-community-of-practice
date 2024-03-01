# prints list of files that do not have tags defined
# run with: python utils/list-pages-without-tags.py  
import os  

# Function to extract tags from a markdown file  
def file_has_tags(file_path):  
    
    with open(file_path, 'r') as file:  

        for line in file:

            if line.strip().startswith('tags:'):
                return True

        return False
    
# Get list of markdown files  
md_files = []  
for root, dirs, files in os.walk('docs'):  
    for file in files:  
        if file.endswith('.md'):  
            md_files.append(os.path.join(root, file))  

# Find files without tags
files_without_tags = []  
for file_path in md_files:  
    if not file_has_tags(file_path):
        print(file_path)