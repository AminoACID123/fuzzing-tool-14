/*
 * @Author: Radon
 * @Date: 2021-06-15 11:52:40
 * @LastEditors: Radon
 * @LastEditTime: 2021-06-15 12:18:13
 * @Description: Hi, say something
 */
#include <stdio.h>
#include <stdbool.h>
#include "C:\\Users\\Radon\\Desktop\\fuzztest\\4th\\example\\Trajectory.h"
#include "C:\\Users\\Radon\\Desktop\\fuzztest\\4th\\example\\Datagram.h"

void test(char* seedPath){
    printf("Congrulation, success!\n");
    printf("seedPath: %s.\n", seedPath);
}

int main(){
    Datagram data;
    data.header.conBCDT.wDay = 24;
    printf("Hi, say something.");
    return 0;
}