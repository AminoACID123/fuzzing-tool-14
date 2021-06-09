'''
Author: Radon
Date: 2021-05-16 10:03:05
LastEditors: Radon
LastEditTime: 2021-05-16 10:07:19
Description: Some pulic function
'''

import re

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