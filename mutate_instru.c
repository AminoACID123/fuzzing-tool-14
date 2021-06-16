/*
 * @Author: Radon
 * @Date: 2021-06-15 11:52:40
 * @LastEditors: Radon
 * @LastEditTime: 2021-06-16 12:27:12
 * @Description: Hi, say something
 */
#include <stdio.h>
#include <stdbool.h>
#include "C:\\Users\\Radon\\Desktop\\fuzztest\\4th\\example\\Trajectory.h"
#include "C:\\Users\\Radon\\Desktop\\fuzztest\\4th\\example\\Datagram.h"

int getInstrumentValue(Datagram data){
    return data.header.conBCDT.wMonth;
}

void mutate(Datagram data, char* savePath, int r){
    data.header.dwFrmHead = 100;
    printf("%d.\n",data.header.SourceSystemID);
    printf("%s",savePath);

    unsigned char* p = (unsigned char*)&data;
	FILE* f = fopen(savePath, "w");
    for (; p < (unsigned char*)&data + sizeof(data); p++) {
		fprintf(f,"%d", *p);
		if (p != (unsigned char*)&data + sizeof(data)-1)
			fprintf(f, ",");
	}
    fclose(f);
    // 变异操作...
}
// gcc -shared -o mutate_instru.dll mutate_instru.c