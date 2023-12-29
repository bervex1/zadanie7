import os
import shutil
import zipfile
from unicodedata import normalize as unicode_normalize

def normalize(filename):
    filename = unicode_normalize('NFKD', filename).encode('ascii', 'ignore').decode('utf-8')
    filename = ''.join(c if c.isalnum() or c in ['.', '_', '-'] else '_' for c in filename)
    return filename

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            extension = extension[1:].upper() 

            if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
                move_and_rename(file_path, 'images', extension)
            elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
                move_and_rename(file_path, 'video', extension)
            elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
                move_and_rename(file_path, 'documents', extension)
            elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
                move_and_rename(file_path, 'audio', extension)
            elif extension in ['ZIP', 'GZ', 'TAR']:
                extract_and_move(file_path, 'archives')
            else:
                print(f"Unknown extension: {extension} for file {file_path}")

def move_and_rename(file_path, category, extension):
    new_filename = normalize(os.path.splitext(file_path)[0]) + '.' + extension
    new_path = os.path.join(category, new_filename)
    os.makedirs(category, exist_ok=True)
    shutil.move(file_path, new_path)
    print(f"Moved and renamed: {file_path} -> {new_path}")

def extract_and_move(file_path, category):
    new_folder = os.path.join(category, normalize(os.path.splitext(file_path)[0]))
    os.makedirs(new_folder, exist_ok=True)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(new_folder)
    os.remove(file_path)
    print(f"Extracted and moved: {file_path} -> {new_folder}")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    process_folder(folder_path)

if __name__ == "__main__":
    main()
