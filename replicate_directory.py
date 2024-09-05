import os

def replicate_directory_structure(source_dir, target_dir):

    # Transfer the source and replicate the directory structure in the target directory

    for root, dirs, files in os.walk(source_dir):
        # Checks for the directory that needs to be created in the target directory
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)
        
        # Creats the directory in target host if it doesn't exists
      
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print(f"Created directory: {target_path}")
        else:
            print(f"Directory already exists: {target_path}")

replicate_directory_structure("path/to/source_dir", "/path/to/target_dir")
