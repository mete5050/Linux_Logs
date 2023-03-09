import subprocess
from github import Github

# Authentication
g = Github('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')

# Get the repository where you want to save the files
repo = g.get_repo('mete5050/Linux_Logs')

# Define the commands to run
commands = ['ls -l', 'df -h', 'uname -a']

# Run the commands and save their outputs to separate files
for i, command in enumerate(commands):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    filename = f'output_{i}.txt'
    with open(filename, 'w') as file:
        file.write(result.stdout)

    # Upload or update the file on GitHub
    with open(filename, 'r') as file:
        file_contents = file.read()
    try:
        file = repo.get_contents(filename)
        repo.update_file(file.path, 'commit message', file_contents, file.sha)
        print(f'File {filename} updated successfully!')
    except:
        repo.create_file(filename, 'commit message', file_contents)
        print(f'File {filename} uploaded successfully!')

