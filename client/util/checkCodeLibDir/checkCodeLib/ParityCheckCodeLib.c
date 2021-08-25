#include <stdbool.h>

static char *transfer2Bin(unsigned int num) {
    static char binary[33];
    int flag = 1;
    int i;
    for (i = 31; i >= 0; i--) {
        if (num & flag) {
            binary[i] = '1';
        } else {
            binary[i] = '0';
        }
        flag <<= 1;
    }
    binary[32] = '\0';
    return binary;
}

static unsigned int getParity(const unsigned int *checkList, int length, bool isEven) {
    //isEven �Ƿ�Ϊż��֤������У���룬1�ĸ�ʽΪż��
    int count = 0;
    for (int i = 0; i < length; ++i) {
        char *oneItemBinList = transfer2Bin(checkList[i]);
        for (int j = 0; j <= 32; ++j) {
            if (oneItemBinList[j] == '1') {
                count += 1;
            } else {
            }
        }
    }
    if (count % 2) {
        if (isEven) {
            //�����ż��֤���͵ü���1��
            return 1;
        } else {
            return 0;
        }
    } else {
        if (isEven) {
            return 0;
        } else {
            return 1;
        }
    }
}