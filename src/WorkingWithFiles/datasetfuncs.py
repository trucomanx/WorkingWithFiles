
import os
import WorkingWithFiles.WorkingWithFiles as wf
import csv  
import numpy as np
from collections import Counter

'''
Generate a CSV file analizing a directory structure from a root directory
'''
def generate_csv_file_from_dir_structure(base_dir,format_list,csv_path,header = ['filename', 'label'],label_first=True):
    
    ## find the labels with only the first level name directory
    label_list = [ name for name in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, name)) ];
    #print('label_list:',label_list)    
    
    ## Find all subdirectories
    file_list_list=[];    
    for label in label_list:
        tmp_path = os.path.join(base_dir,label);
        file_list = wf.get_all_files_in_dir(tmp_path,formats_search=format_list,is_relative=True);
        file_list_list.append(file_list);
    
    ## Write a CSV file
    with open(csv_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        writer.writerow(header)
        
        Nel=[];
        for file_list in file_list_list:
            Nel.append(len(file_list));
            
        N=np.max(Nel);
        M=len(label_list);
        
        out=[]
        Count=Counter();
        for n in range(N):
            for m in range(M):
                if(n<Nel[m]):
                    filepath=os.path.join(label_list[m],file_list_list[m][n]);
                    
                    if label_first:
                        category=label_list[m];
                    else:
                        diretorio, nome_arquivo = os.path.split(filepath)
                        category=os.path.basename(diretorio);
                    
                    item=[filepath, category];
                    Count[category]=Count[category]+1;
                    
                    writer.writerow(item);
                    out.append(item);
    
    return out,Count;
