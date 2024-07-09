import os
import priv

# can be any dir, but this one contains .md files
dir = priv.givedir()

# read files in a directory
def read_dir(dir):
    file_contents = {}
    # reading logic
    for filename in os.listdir(dir):
        if filename.endswith('.md'):
            with open(os.path.join(dir, filename), 'r') as file:
                file_contents[filename] = file.readlines()
    return file_contents


def search_for_term(file_contents, term):
    results = {}
    # go through each line of the file from recieved contents
    for filename, lines in file_contents.items():
        matching_lines = []
        for line_num, line in enumerate(lines, start=1):
            if term.lower() in line.lower():
                matching_lines.append((line_num, line.strip()))
        if matching_lines:
            results[filename] = matching_lines
    return results

def display_results(results):
    for filename, matches in results.items():
        print(f"\nIn file: {filename}")
        for line_num, line in matches:
            print(f"  Line {line_num}: {line}")
            
