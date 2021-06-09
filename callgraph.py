'''
Author: Radon
Date: 2020-09-28 13:18:56
LastEditors: Radon
LastEditTime: 2021-05-16 10:04:43
Description: Hi, say something
'''
import re
import public

def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

def createCallGraph(source_loc,graph_loc):
    f_source = open(source_loc)
    f_graph = open(graph_loc,mode="w+")
    brace = 0

    lines = f_source.readlines()
    lines = public.deleteNote(lines)

    start = "empty"
    graph = []
    customize = []      #这个列表用于存储自定义的函数
    # print(lines)
    for line in lines:
        if "(" in line and brace == 0:
            start = line.split("(")[0].split(" ")[-1]
            start = re.sub("[^A-Za-z1-9_]","",start)
            if not start in customize:
                customize.append(start)
        elif "(" in line and brace != 0:
            words = re.sub("[^A-Za-z1-9_(]"," ",line).split("(")
            for end in words:
                end = end.split(" ")[-1]
                if end in customize:
                    path = start+","+end
                    #先把路径信息存到一个list中，下面是在write前检测一下是否已存在这个路径（这是针对调用多次同一函数的情况）
                    found = False
                    for i in range(0,len(graph)):
                        if path in graph[i]:
                            print("I found it!\n")
                            found = True
                            break
                    if found == False :
                        graph.append(path+",1")
                    else:
                        path = graph.pop(i).split(",")
                        weight = int(path[2])+1
                        graph.append(path[0]+","+path[1]+","+str(weight))
        if "{" in line:
            brace += 1
        if "}" in line:
            brace -= 1

    print("graph:",graph)
    print("customize:",customize)
    for i in range(0,len(graph)):
        f_graph.write(graph[i]+"\n")
    f_graph.close()

if __name__ == '__main__':
    source_loc = "D:\\VS2015Project\\FuzzExperiment\\Project6\\Project6\\main.c"
    graph_loc = "D:\\VS2015Project\\FuzzExperiment\\Project6\\Project6\\graph_cg.txt"
    createCallGraph(source_loc,graph_loc)