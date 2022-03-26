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
    
    for file in file_list:
        seq = sequence(file_path=os.path.join(DIR, file))
        print("Finished: " + file)
        with open("results2.txt", "a") as out_file:
            out_file.write(seq)

    elapsed_time_proof = time.process_time() - t_proof
    print("\nTempo de leitura e escrita de todos os arquivos: " + str(elapsed_time_proof) + "s")
