input_path = r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV"
##在上面填入需要读取的mod文件夹路径  Enter the path to the mod folder you want to read above👆
output_path = r"C:\Users\wgic\Documents\Paradox Interactive\Hearts of Iron IV\mod\Universal Unlock Units\resultListMDcn.txt"
##在上面填入输出文件路径  Enter the output file path above👆


import os
import time




def find_locked_divisions(folder_path, target_field="is_locked = yes"):
    result = []
    if os.path.exists(folder_path) == False:
        print("Path not found:"+folder_path)
        return result
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "r",encoding="utf-8",errors="ignore") as file:
                content = file.read()
                while 1:
                    index = content.find(target_field)
                    if index == -1: break
                    cr=content.rfind("name = \"", 0, index)
                    if cr != -1:
                        start_index = cr + len("name = \"")
                        end_index = content.find("\"", start_index)
                        division_name = content[start_index:end_index]
                        result.append(division_name)
                    content = content[index+15:]
    return result


start = time.time()

#common,events,history
path1=input_path+r"\common"
path2=input_path+r"\events"
path3=input_path+r"\history"




locked_divisions = find_locked_divisions(path1) + find_locked_divisions(path2) + find_locked_divisions(path3)
locked_divisions_one = list(set(locked_divisions))
print(len(locked_divisions),len(locked_divisions_one))
with open(output_path,"w",encoding="utf-8") as file:
    for dname in locked_divisions_one:
        outname="    \""+dname+"\",\n"
        file.write(outname)
end = time.time()
print("Using time: "+str(end - start)+"s")