import os
import time
import concurrent.futures
from fnmatch import fnmatch
import pandas as pd
from Bio import SeqIO

DIR = './VOCs/'
FILE_FORMAT = 'fasta'

def sequence(file_path):
    with open(file_path, encoding="utf8") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                seq = str(record.seq).upper()
    return seq
    

if __name__ == '__main__':
    t_proof = time.process_time()
    
    file_list = [name for name in os.listdir(DIR) if fnmatch(name, '*.' + FILE_FORMAT)]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for file in file_list:
            futures.append(executor.submit(sequence, file_path=os.path.join(DIR, file)))
            #print("Finished: " + file)
        for future in concurrent.futures.as_completed(futures):
            with open("results.txt", "a") as out_file:
                out_file.write(future.result())
    
    elapsed_time_proof = time.process_time() - t_proof
    print("\nTempo de leitura e escrita de todos os arquivos: " + str(elapsed_time_proof) + "s")
