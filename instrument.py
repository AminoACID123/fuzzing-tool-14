import re
import os
import subprocess

def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

def printInfo(msg):
    print("\n\033[0;32mInfo:\033[0m"+msg)

def deleteNote(source):
    skip = False
    for i in range(len(source)):
        if "//" in source[i]:
            source[i]=source[i].split("//")[0]+"\n"
        if "/*" in source[i]:
            skip = True
            if "*/" in source[i]:
                skip = False
                source[i]=source[i].split("/*")[0]+"\n"
        elif "*/" in source[i]:
            skip=False
            source[i]="\n"
        if skip==True:
            source[i]="\n"
    return source

def instrument(source_loc,instrument_loc,output_loc):
    brace = 0      # 记录大括号数量，方便后续操作
    instr = False
    f = open(source_loc)
    lines = f.readlines()
    f.close()
    lines = deleteNote(lines)
    length = len(lines)
    i = 0
    while i != length:
        if "(" in lines[i] and brace == 0:
            code = lines[i].split("(")[0]
            code = re.sub("[^A-Za-z1-9_]"," ",code)
            # 插桩语句，可能需要换
            instrCode = "\tprintf(\"execute-"+code.split(" ")[-1]+"\\n\");\n"
            instr = True
        if "{" in lines[i]:
            brace += 1
        if "}" in lines[i]:
            brace -= 1
        if instr == True and brace > 0:
            lines.insert(i+1,instrCode)
            instr = False
            length += 1
        i += 1
    f = open(instrument_loc,mode="w")
    for code in lines:
        f.write(code)
    f.close()
    printInfo("Successfully inserted.")
    cmd_exe = ["gcc "+instrument_loc+" -o "+output_loc+"instrument.exe"]
    printInfo("The new instrumented file will overwrite the old instrumented file.\n")
    # os.chdir(cmd_exe[0])
    os.system(cmd_exe[0])
    printInfo("The instrumented file successfully generated.\n")
    os.remove(instrument_loc)       # 删掉已插桩的源文件

def multiFileCompile(source_locs):
    command = "gcc "
    source_list = source_locs.split("\n")
    root_loc = re.sub(source_list[0].split("\\")[-1],"",source_list[0])
    for data in source_list:
        command += data + " "
    command += " -o " + root_loc + "temp.exe"
    if os.system(command) == 0:
        print("compile success")
    else:
        print("compile error")

if __name__=="__main__":
    # source_loc = "D:\\VS2015Project\\FuzzExperiment\\Project6\\Project6\\main.c"
    # instrument_loc = "D:\\VS2015Project\\FuzzExperiment\\Project6\\Debug\\instrument.c"
    # output_loc = "D:\\VS2015Project\\FuzzExperiment\\Project6\\Debug\\"  # 输出exe和obj的位置
    # instrument(source_loc,instrument_loc,output_loc)
    # command = "gcc C:\\Users\\Radon\\Desktop\\fuzztest\\2nd\\main.c C:\\Users\\Radon\\Desktop\\fuzztest\\2nd\\myfile.c -o C:\\Users\\Radon\\Desktop\\fuzztest\\2nd\\temp.exe"
    command = "gcc C:\\Users\\Radon\\Desktop\\fuzztest\\2nd\\main.c"
    print(os.system(command))
    print("yes")