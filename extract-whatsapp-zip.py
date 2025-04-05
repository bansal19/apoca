import os
import zipfile
import glob

def extract_whatsapp_zips(folder_path):
    """
    Extract WhatsApp chat zip files and rename the extracted .txt files
    by appending "whatsapp" to the original zip file name.
    """
    # Get all zip files in the specified folder
    zip_files = glob.glob(os.path.join(folder_path, "*.zip"))
    
    # Create an output directory if it doesn't exist
    output_dir = os.path.join(folder_path, "extracted")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each zip file
    for zip_path in zip_files:
        try:
            # Get the base name of the zip file without extension
            zip_filename = os.path.basename(zip_path)
            base_name = os.path.splitext(zip_filename)[0]
            
            # Create a new output filename by appending "whatsapp"
            output_filename = f"{base_name} whatsapp.txt"
            output_path = os.path.join(output_dir, output_filename)
            
            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Get list of files in the zip
                file_list = zip_ref.namelist()
                
                # Find the .txt file in the zip (usually there's only one)
                txt_files = [f for f in file_list if f.lower().endswith('.txt')]
                
                if txt_files:
                    # Extract the first .txt file found
                    txt_file = txt_files[0]
                    # Extract and rename
                    with zip_ref.open(txt_file) as source, open(output_path, 'wb') as target:
                        target.write(source.read())
                    print(f"Extracted: {output_filename}")
                else:
                    print(f"No .txt file found in {zip_filename}")
        
        except Exception as e:
            print(f"Error processing {zip_path}: {str(e)}")

if __name__ == "__main__":
    # Path to the folder containing WhatsApp chat zip files
    folder_path = "processed_chats"
    
    # Extract all zip files
    extract_whatsapp_zips(folder_path)
    print("Extraction complete!")
