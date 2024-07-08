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

