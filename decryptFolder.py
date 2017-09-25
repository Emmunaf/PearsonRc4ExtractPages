#Rc4 decryptor with pearson key already loaded in.
from Crypto.Cipher import ARC4
import os
path_to_folder = input('Nome (con path) cartella con file cifrati?')
for file_in_folder in os.listdir(path_to_folder):
        #if file_in_folder.content("PDF"): # possibile implementare filtri sui file nela cartella
        fname = os.path.join(path_to_folder, file_in_folder)
        with open(fname, 'rb') as cipher_file:
            ciph_payload = cipher_file.read()

        obj = ARC4.new(b'\xC4\x01\x05\xB5\x15\xF4\x32\x62')
        decrypted_output = obj.decrypt(ciph_payload)
        with open(fname + "decrypted.pdf", 'wb') as out_file:
            out_file.write(decrypted_output)

