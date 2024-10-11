import os

def rename_with_rtlo(file_name, disguised_extension):
    # RTLO character
    rtlo = '\u202e'
    
    # Get the base name and real extension of the file
    base_name, real_extension = os.path.splitext(file_name)
    
    # Remove the dot from the extension
    real_extension = real_extension[1:]
    
    # Reverse the disguised extension (for example 'jpg' becomes 'gpj')
    reversed_extension = disguised_extension[::-1]
    
    # Create the new name with RTLO
    new_name = f"{base_name}{rtlo}{reversed_extension}.{real_extension}"
    
    return new_name

def main():
    # Input file name and disguised extension from the user
    file_name = input("Enter the path of the file you want to disguise (e.g., script.bat): ")
    
    if not os.path.exists(file_name):
        print("Error: The specified file does not exist.")
        return

    disguised_extension = input("Enter the extension you want the file to appear as (e.g., jpg, txt): ")
    
    # Get the new name with RTLO
    new_name = rename_with_rtlo(file_name, disguised_extension)
    
    # Rename the file
    new_file_path = os.path.join(os.path.dirname(file_name), new_name)
    os.rename(file_name, new_file_path)
    
    print(f"The file has been renamed to: {new_name}")
    print(f"Full path: {new_file_path}")

if __name__ == "__main__":
    main()
