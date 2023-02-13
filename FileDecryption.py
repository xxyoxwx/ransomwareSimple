from cryptography.fernet import Fernet
import os
def crg_key():
    return open('key.key', 'rb').read()

def decryptFiles(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

if __name__ == '__main__':
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #UNCOMMENT FOR USAGE//path_to_encrypt = 'C:\\'
    #path to directory u wanna encrypt.Currently located in C: drive.
    os.remove(path_to_encrypt+'\\'+'readme.txt')
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    key = crg_key()
    decryptFiles(full_path, key)
