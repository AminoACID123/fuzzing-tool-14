#ifndef TRAJECTORY_H
#define TRAJECTORY_H

#include <stdbool.h>

typedef struct EularAngle {
	char valA : 2; //��λ��ǰ
	char valB : 2;
	char valC : 4;
	unsigned short int dRoll;   //��ת�� ����
	double Pitch;  //ƫ���� ����
	double Yaw;    //������ ����
	//����汾
}EularAngle;

typedef struct DETECTED_CFAR_ARRAY {
	//float target_range_f;
	//float target_freq_f;
	//float target_sigma_amp_f;     /**change to i *******/
	//float target_sigma_pha_f;     /***change to q *****/
	//float target_sigma_noise_f;   /****SN****/
	//float target_delta_ev_amp_f;   /***change to i****/
	//float target_delta_ev_pha_f;  /*****change to q*****/
	unsigned int bak;
}DETECTED_CFAR_ARRAY;

typedef struct RadarInfo {
	unsigned char ucRadarID;	//ȡֵ��Χ[0,5]
	unsigned char ucRadarType;	//ȡֵ��Χ[0,2]
	//bool bPatternEnable;
	DETECTED_CFAR_ARRAY detected[2];
}RadarInfo;

typedef struct {
	//int d_Time;        //��������         ���ʱ��
	//double fnPosition[4096]; //���ľ�������
	//double fnVelocity[4]; //���ľ����ٶ�
	//EularAngle sEularAngle[2][2];
	RadarInfo radarinfo[3];
	unsigned int radonInstr:20;
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		bool bPatternEnable;
	}TestA;
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		bool bPatternEnable;
	}TestB;
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		bool bPatternEnable;
		struct {
			unsigned char ucRadarID;
			unsigned char ucRadarType;
			bool bPatternEnable;
		}TestC;
	}TestD;
}Trajectory;
#endif // TRAJECTORY_H
