'''
Author: Radon
Date: 2021-05-16 10:03:05
LastEditors: Radon
LastEditTime: 2021-06-14 14:55:30
Description: Some pulic function
'''

import re, time, os
from win32 import win32api

'''
@description: 删除程序中的注释
@param {*} source 代码列表，source = f.readlines()
@return {*}
'''
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

'''
@description: 获取所有定义的函数
@param {*} source_locs 所有源文件地址的字符串，用\n隔开
@return {*} 返回包含所有自定义函数的列表
'''
def getAllFunctions(source_locs):
    source_loc = source_locs.split("\n")
    funcList = []
    for source in source_loc:
        try:
            f = open(source,encoding="utf8")
            lines = f.readlines()
        except UnicodeDecodeError:
            f = open(source)
            lines = f.readlines()
        brace = 0
        f.close()
        lines = deleteNote(lines)
        for line in lines:
            if "(" in line and brace == 0:
                code = line.split("(")[0]
                code.rstrip()
                code = re.sub("[^A-Za-z0-9_]","+",code)
                funcList.append(code.split("+")[-1])
            if "{" in line:
                brace += 1
            if "}" in line:
                brace -= 1
        funcList = sorted(set(funcList))
    return funcList

'''
@description: 写一个生成初始种子的cpp文件，并编译和执行它
@param {*} header_loc 列表，里面存储了所有头文件的路径
@param {*} struct 用户所选择的结构体名称
@param {*} structDict Ui_dialog_seed里的字典，其中存储了分析得到的结构体和它的成员变量的信息
@return {*}
'''
def genSeed(header_loc, struct, structDict):
    # 先设置好相关的位置信息
    root = re.sub(header_loc[0].split("\\")[-1],"",header_loc[0]) + "\\in\\"
    if not os.path.exists(root):
        os.mkdir(root)
    genSeedPath = root + "genSeed.cpp"
    # 开始写代码，先include相关内容
    code = "#include <iostream>\n#include <Windows.h>\n"
    # 把用户选择的头文件位置也include
    for header in header_loc:
        code += "#include \"" + header + "\"\n"
    code += "using namespace std;\n\n"
    code += "int main(){\n"
    # 新建结构体变量，并向它的成员变量赋值
    code += "\t" + struct + " data;\n"
    for key,value in structDict[struct].items():
        dataName = key.split(" ")[-1].split(":")[0]
        code += "\tdata." + dataName + " = " + str(value["value"]) + ";\n"
    # 赋值结束后，向seed.txt文件中写入内容
    code += "\n\tunsigned char* p = (unsigned char*)&data;\n\t"
    code += "FILE *f = fopen(\"seed.txt\", \"w\");\n\t"
    code += "for (; p < (unsigned char*)&data + sizeof(data); p++) {\n\t\t"
    code += "fprintf(f, \"%d\", *p);\n\t\t"
    code += "if (p != (unsigned char*)&data + sizeof(data) - 1) fprintf(f, \",\");\n\t"
    code += "}\n\tfclose(f);\n\treturn 0;\n}"
    # 写完代码后，编译并执行，在第一个头文件的同目录下会生成seed.txt，它就是种子测试用例
    f = open(genSeedPath, mode="w")
    f.write(code)
    f.close()
    # 编辑命令集合
    cmds = []
    cmds.append("g++ -o genSeed.exe genSeed.cpp")
    cmds.append("genSeed.exe")
    # 切换目录并执行命令
    os.chdir(root)
    for cmd in cmds:
        os.system(cmd)

'''
@description: 模拟按下ESC键
@param {*}
@return {*}
'''
def pressESC():
    win32api.keybd_event(27,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(27,0,2,0)