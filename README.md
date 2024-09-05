Define a function **replicate_directory_structure** that takes source_dir and target_dir as arguments.
  Use **os.walk** to traverse the source directory.
  For each directory in the source:
  Calculate the relative path.
  Construct the corresponding path in the target directory.
  Check if the directory exists in the target.
  If it doesn’t exist, create it using **os.makedirs**.
Log the actions taken (e.g., directory created, already exists).


Instructions on How to Run the Script:

Ensure Python 3.x is installed on your machine.
Save the script as replicate_directory.py.
To run the script, use the following command:
**python replicate_directory.py**

Modify the replicate_directory_structure function call to include your actual source and target directories.
