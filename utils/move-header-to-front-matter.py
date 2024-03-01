# loops through all .md files
# Where front matter exists, takes the page header '#' and moves it to the title property of the front matter
# adds a blank h1 '#' at the end of the page (material seems to require this somewhere)
# run with: python utils/move-header-to-front-matter.py  
import os  

def move_header_to_front_matter(filepath, header):
    lines = open(filepath).read().splitlines()
    lines.insert(1, ("title: " + header) )
    lines.append("")
    lines.append("# ")
    for i, line in enumerate(lines):
        if line.strip().startswith("# "):
            del lines[i]
            del lines[i]
    open(filepath, mode='w').write('\n'.join(lines))

def get_header(file_path):  
    
    with open(file_path, 'r') as file:  

        has_front_matter = False
        for line in file:

            if line.strip().startswith('---'):
                has_front_matter = True

            # No front matter - return False
            if not has_front_matter:
                return False
            
            if line.strip().startswith('# '):
                return line[2:]


# Get list of markdown files  
md_files = []  
for root, dirs, files in os.walk('docs'):  
    for file in files:  
        if file.endswith('.md'):  
            md_files.append(os.path.join(root, file))  

# move headers to front matter
files_without_tags = []  
for file_path in md_files:  
    print(file_path)
    header = get_header(file_path)
    if header:
        move_header_to_front_matter(file_path, header)