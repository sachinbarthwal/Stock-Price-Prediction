import subprocess

# Define the relative path to the 'src' directory from the project root
src_directory = './src/'

# List of scripts to run in order, with the relative path included
scripts = ['data_fetcher.py', 'model.py', 'predict.py', 'visualize.py']

for script in scripts:
    # Use the relative path to run each script
    subprocess.run(['python', src_directory + script])

print("All scripts have been run successfully.")