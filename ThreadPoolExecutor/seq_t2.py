import os
import time
import concurrent.futures
from fnmatch import fnmatch
import pandas as pd
from Bio import SeqIO

DIR = './VOCs/'
FILE_FORMAT = 'fasta'

def sequence(file_path, file_name):
    return print(file_path + " " + file_name)
    

if __name__ == '__main__':
    t_proof = time.process_time()
    
    file_list = [name for name in os.listdir(DIR) if fnmatch(name, '*.' + FILE_FORMAT)]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #futures = {executor.submit(sequence, file_path=os.path.join(DIR, file), file_name=file): file for file in file_list}
        futures = {executor.submit(sequence, file_path=DIR, file_name=file): file for file in file_list}
    
    elapsed_time_proof = time.process_time() - t_proof
    print("\nTempo de leitura e escrita de todos os arquivos: " + str(elapsed_time_proof) + "s")
