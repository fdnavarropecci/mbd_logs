import pandas as pd
import csv
import codecs

file_path = r"C:\Users\fdnav\mbd_logs\spanish.txt"
save_path = r"C:\Users\fdnav\mbd_logs\es_cw.py"

es_cw = pd.read_csv(file_path, header=None)

print(es_cw.head(5))

#es_cw_list = es_cw.values.tolist()

es_cw_list = [row[0] for row in es_cw.values]

print(type(es_cw_list))

print(es_cw_list)

with  codecs.open(save_path, mode='w', encoding="utf-8-sig") as f:
    f.write(str(es_cw_list))

    
