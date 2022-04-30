import zipfile
import os

def makeZip(dir):
    os.chdir(dir)
    if not os.path.isfile(dir+'\Screenshot.zip'):
        zip_file = zipfile.ZipFile(dir+'\Screenshot.zip', 'w')
        for folder, subfolders, files in os.walk(dir):
            for file in files:
                if file.startswith('Maple_') and file.endswith('.png'):
                    zip_file.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), dir+'\Screenshot'), 
                    compress_type = zipfile.ZIP_DEFLATED)
        zip_file.close()
        return True
    else:
        return False
    