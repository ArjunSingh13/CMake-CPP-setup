#Limitation of python script:
# It does not help move to inner directory on command line, need to explore how we can do that.
# using makefile instead fix this issue, but curious to find a way in python.

import os
import shutil

def setup_build_folder():
    #define the build folder path
    build_folder = os.path.join(os.getcwd(), "build")

    #remove the build folder if exists
    if os.path.exists(build_folder):
        print(f"Removing existing build folder: {build_folder}")
        shutil.rmtree(build_folder)

    #create new build folder
    os.makedirs(build_folder, exist_ok=True)
    print(f"Created new build folder: {build_folder}")

    #change the working directory to the build folder
    # Change the directory using a system command
    print("To move into the build folder, run:")
    print(f"cd {build_folder}")


if __name__ == "__main__":
    setup_build_folder()