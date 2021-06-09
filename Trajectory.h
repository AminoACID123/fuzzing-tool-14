#define TRAJECTORY_H

typedef struct EularAngle {
	char valA : 2;
	char valB : 2;
	char valC : 4;
	unsigned short int dRoll;
	double Pitch;
	double Yaw;
}EularAngle;

typedef struct DETECTED_CFAR_ARRAY {
	unsigned int bak;
}DETECTED_CFAR_ARRAY;

typedef struct RadarInfo {
	unsigned char ucRadarID;
	unsigned char ucRadarType;
	DETECTED_CFAR_ARRAY detected[2];
}RadarInfo;

typedef struct {
	RadarInfo radarinfo[3];
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		int bPatternEnable;
	}TestA;
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		int bPatternEnable;
	}TestB;
	struct {
		unsigned char ucRadarID;
		unsigned char ucRadarType;
		int bPatternEnable;
		struct
		{
			unsigned char ucRadarID;
			unsigned char ucRadarType;
			int bPatternEnable;
		}TestC;
	}TestD;
}Trajectory;