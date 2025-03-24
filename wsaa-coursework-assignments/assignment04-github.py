#The program should then replace all the instances of the text 
# "Andrew" with your name. 
# The program should then commit those changes and push the file 
# back to the repository (You will need authorisation to do this).
# Author: Andre Machado

from github import Github
from config import config as cfg  # Importing configuration file with API keys

# Initialize GitHub connection using Personal Access Token
g = Github(cfg['githubkey'])

# Specify the repository
repo = g.get_repo('deMachad0/test-replace_text')

# Get the file
file = repo.get_contents('Andrew_to_Andre.txt')

# Read the file content
file_content = file.decoded_content.decode('utf-8')

# Replace the text
modified_content = file_content.replace('Andrew', 'Andre')

# Update the file in the repository
repo.update_file(
    file.path,       # File path
    'Replace Andrew with Andre',  # Commit message
    modified_content,  # New file content
    file.sha         # File's current SHA
)

print("Text Replacement completed")