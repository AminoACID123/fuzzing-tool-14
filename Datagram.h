#include "Trajectory.h"
typedef struct TagDpHead{
	unsigned short dwFrmHead;          
	unsigned short SourceSystemID:8;
	unsigned short ObSystemId:8;
	unsigned int uiNo;
	struct{
		unsigned short wYear     :8;
		unsigned short wMonth    :8;
		unsigned short wDay      :8;
		unsigned short wHour     :8;
		unsigned short wMinute :8;
		unsigned short wSecond   :8;
		unsigned short wMillisec;
	}conBCDT;
	unsigned int checksum;
}DpHead;

typedef struct Datagram{
	DpHead header;
	Trajectory trajectory;
}Datagram;

void CheckData(Datagram* data);