import os
import concurrent.futures
from fnmatch import fnmatch
import pandas as pd
from IPython.display import display

DIR = './VOCs/'
FILE_FORMAT = 'fasta'

def to_dataframe(file_path):
    """
    Convert a fasta file to a dataframe.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    header = lines[0].split(' ')[0]
    seq = ''.join(lines[1:])
    return pd.DataFrame({'header': [header], 'seq': [seq]})
    

if __name__ == '__main__':
    file_list = [name for name in os.listdir(DIR) if fnmatch(name, '*.' + FILE_FORMAT)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for file in file_list:
            futures.append(executor.submit(to_dataframe, file_path=os.path.join(DIR, file)))
        for future in concurrent.futures.as_completed(futures):
            with open("results.txt", "a") as out_file:
                out_file.write(future.result().to_string())
            #display(future.result().to_string())
