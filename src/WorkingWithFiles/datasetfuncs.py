
import os
import WorkingWithFiles.WorkingWithFiles as wf
import csv  
import numpy as np


def generate_csv_file_from_dir_structure(base_dir,format_list,csv_path,header = ['filename', 'label']):
    label_list = [ name for name in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, name)) ]
    file_list_list=[];
    #print('label_list:',label_list)
    
    for label in label_list:
        tmp_path = os.path.join(base_dir,label);
        file_list = wf.get_all_files_in_dir(tmp_path,formats_search=format_list,is_relative=True);
        file_list_list.append(file_list);
    
    with open(csv_path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        writer.writerow(header)
        
        Nel=[];
        for file_list in file_list_list:
            Nel.append(len(file_list));
            
        N=np.max(Nel);
        M=len(label_list);
        
        out=[]
        for n in range(N):
            for m in range(M):
                if(n<Nel[m]):
                    item=[os.path.join(label_list[m],file_list_list[m][n]), label_list[m]];
                    writer.writerow(item);
                    out.append(item);
        
        category=set();
        for m in range(M):
            category.add(label_list[m]);
    return out,category;
