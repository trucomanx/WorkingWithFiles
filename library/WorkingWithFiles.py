#!/usr/bin/python
import os
from natsort import os_sorted


def reaname_files_in(dirpath,prename,fmt_out=".jpg",formats_search=['.jpeg','.JPEG','.jpg','.JPG']):
    '''
    Renombra los archivos de forma ordenada usando un prename
    
    :param dirpath: Path a analizar.  
    :type dirpath: string
    :param prename: Nombre previo. Los nombres nuevos tendran la forma `prename+str(id)+fmt_out`.
    :type prename: string
    :param fmt_out: Formato de salida. Los nombres nuevos tendran la forma `prename+str(id)+fmt_out`.
    :type fmt_out: string
    :param formats_search: Lista de formatos aceptados.
    :type formats_search: list[string]
    :warning: El prename no debe ser el prename de los archivos actuales o seran sobrescritos varios archivos.
    '''
    print("Working on:",dirpath)
    if(os.path.isdir(dirpath)==False):
        print("Directory",dirpath,"no exist!");
        return 0;
    for x in os.walk(dirpath):
        print('Found some files:',x[2])
    
    if len(x[2])>0:
        k=1;
        for name in x[2]:
            #print("id:",k,"name:",os.path.join(dirpath,name),"out:",os.path.join(dirpath,prename+str(k)+fmt_out))
            filename, ext = os.path.splitext(name);
            if(ext in formats_search):
                os.rename(os.path.join(dirpath,name), os.path.join(dirpath,prename+str(k)+fmt_out))
                k=k+1;



def get_all_files_in_dir_list(dirpath_list,formats_search=['.jpeg','.JPEG','.jpg','.JPG']):
    """
    Busca archivos.
    Retorna todos los archivos en los directorios listados en `dirpath_list`.
    Restringe su busqueda a las extensiones en `formats_search`.
    
    :param dirpath_list: lista de directorios
    :type dirpath_list: list[string]
    :param formats_search: Lista de formatos
    :type formats_search: list[string]
    :return: Lista ordenada de todos los archivos en dirpath_list.
    :rtype: list[string]
    """
    lista=[];
    for dirpath in dirpath_list:
        #print("Working on:",dirpath)
        if(os.path.isdir(dirpath)==False):
            print("Directory",dirpath,"no exist!");
            return [];
        for x in os.walk(dirpath):
            #print('Found some files:',x[2])
            for name in x[2]:
                filename, ext = os.path.splitext(name);
                if(ext in formats_search):
                    lista.append(os.path.join(dirpath,name));
    return os_sorted(lista);
