input_path = r"E:\SteamLibrary\steamapps\workshop\content\394360\2438003901"
##在上面填入需要读取的mod文件夹路径  Enter the path to the mod folder you want to read above👆
output_path = r"C:\Users\wgic\Documents\Paradox Interactive\Hearts of Iron IV\mod\Universal Unlock Units\resultListSubtno.txt"
##在上面填入输出文件路径  Enter the output file path above👆


import os,time,re


def find_locked_subunits(folder_path):
    results = []

    pattern = re.compile(r'(\w+)\s=\s{[^{]*?active\s=\sno', re.DOTALL)

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):  # 假设文件是文本文件，您可以根据需要更改扩展名
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'r', encoding='utf-8', errors="ignore") as f:
                content = f.read()
                matches = pattern.findall(content)
                results.extend(matches)

    return results


start = time.time()

#common\units
path1=input_path+r"\common\units"





locked_subunits = find_locked_subunits(path1)
locked_subunits_one = list(set(locked_subunits))
print(len(locked_subunits),len(locked_subunits_one))
with open(output_path,"w",encoding="utf-8") as file:
    for dname in locked_subunits_one:
        outname="    \""+dname+"\",\n"
        file.write(outname)
end = time.time()
print("Using time: "+str(end - start)+"s")