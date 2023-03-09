import subprocess
from github import Github

# Authentication
g = Github('YOUR_GITHUB_TOKEN')

# Get the repository where you want to save the file
repo = g.get_repo('USERNAME/REPO_NAME')

# Define the commands to run
commands = ['ls -l', 'df -h', 'uname -a']

# Run the commands and capture their outputs
outputs = []
for command in commands:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    outputs.append(result.stdout)

# Save the outputs to a text file
with open('output.txt', 'w') as file:
    file.writelines(outputs)

# Get the contents of the output file
with open('output.txt', 'r') as file:
    file_contents = file.read()

# Check if the file already exists on GitHub
try:
    file = repo.get_contents('output.txt')
    # Update the file on GitHub
    repo.update_file(file.path, 'commit message', file_contents, file.sha)
    print('File updated successfully!')
except:
    # Create a new file on GitHub
    repo.create_file('output.txt', 'commit message', file_contents)
    print('File uploaded successfully!')
