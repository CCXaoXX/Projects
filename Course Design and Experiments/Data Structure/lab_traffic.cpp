#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define OK     1
#define OVERFLOW    -2 
#define DMAX 33
#define VMAX 31
#define SMAX 10
#define TMAX 10

typedef int Status;
typedef int CityType;

typedef struct TNode{			//边的信息 
	char name[SMAX];			//班次
	int StartTime, StopTime;	//起止时间
	int EndCity; 				//有向边的端点，指向顶点数组的位序
	int Cost; 					//价格 
}TNodeData;
typedef struct VNode{			//节点信息 
	CityType city;				//城市序号 
	int TrainNum, FlightNum;	//班次个数
	TNodeData Train[TMAX];		//边
	TNodeData Flight[TMAX];	
}VNodeData;
typedef struct PNode{			//时间路径节点 
	int City;
	int TraNo;
}PNodeData;

//全局变量 
VNodeData FList[VMAX]; 			//文件信息
char name_city[VMAX][SMAX];		//城市名，第一下标为顶点数组中的位序 
int num_city;					//城市数目
PNodeData Path[VMAX];			//存储临时最小时间路径
PNodeData MinPath[VMAX];		//存储搜索到当前的最小时间路径
int MinTime, StartTime;
int CPath;

const char Path_city[] = "city.txt";
const char Path_train[] = "train.txt";
const char Path_flight[] = "flight.txt";

Status SearchCity(char *Name){	//查找城市 
	int i;
	for(i = 0; i < num_city; i++){
		if (strcmp(Name, name_city[i]) == 0){
			return i;
		}
	}
	return -1;
}

Status InsertCity(char *Name){	//添加城市 
	if(SearchCity(Name) == -1){
		strcpy(name_city[num_city],Name);
		FList[num_city].city = num_city;
		FList[num_city].FlightNum = 0;
		FList[num_city].TrainNum = 0;
		num_city++;
		return OK;
	}
	printf("该城市已存在！\n\n\n\n");
	return -1;
}

Status DeleteCity(char *Name){	//删除城市 
	int city, i, j;
	city = SearchCity(Name);
	if(city != -1){
		for(i=city;i<num_city-1;i++){
			strcpy(name_city[i], name_city[i+1]);
			FList[i].FlightNum = FList[i+1].FlightNum;
			FList[i].TrainNum = FList[i+1].TrainNum;
			for(j = 0; j < FList[i].FlightNum; j++){
				FList[i].Flight[j].Cost = FList[i+1].Flight[j].Cost;
				FList[i].Flight[j].EndCity = FList[i+1].Flight[j].EndCity;
				strcpy(FList[i].Flight[j].name, FList[i+1].Flight[j].name);
				FList[i].Flight[j].StartTime = FList[i+1].Flight[j].StartTime;
				FList[i].Flight[j].StopTime = FList[i+1].Flight[j].StopTime;
			}
		}
		num_city--;
		return OK;
	} 
	printf("该城市不存在！\n\n\n\n");
	return -1;
}

Status ToFiles(){	//存入文件 
	FILE *fp;
	int i, j, total;
	fp = fopen(Path_city, "w");
	fprintf(fp, "%d\n", num_city);
	for(i = 0; i < num_city; i++){
		fprintf(fp, "%s\n", name_city[i]);
	}
	fclose(fp);
	total = 0;
	fp = fopen(Path_train, "w");
	for(i = 0; i < num_city; i++){
		total += FList[i].TrainNum;
	}
	fprintf(fp, "%d\n", total);
	for(i = 0; i < num_city; i++){
		for(j = 0; j < FList[i].TrainNum; j++){
			fprintf(fp, "%s %s %s ", FList[i].Train[j].name, name_city[i], name_city[FList[i].Train[j].EndCity]);
			fprintf(fp, "%2d:%2d %2d:%2d %d\n", FList[i].Train[j].StartTime / 60, FList[i].Train[j].StartTime%60, FList[i].Train[j].StopTime / 60, FList[i].Train[j].StopTime % 60, FList[i].Train[j].Cost);
		}
	}
	fclose(fp);
	total = 0;
	fp = fopen(Path_flight, "w");
	for(i = 0; i < num_city; i++){
		total += FList[i].FlightNum;
	}
	fprintf(fp, "%d\n", total);
	for(i = 0; i < num_city; i++){
		for(j = 0; j < FList[i].FlightNum; j++){
			fprintf(fp, "%s %s %s ", FList[i].Flight[j].name, name_city[i], name_city[FList[i].Flight[j].EndCity]);
			fprintf(fp, "%2d:%2d %2d:%2d %d\n", FList[i].Flight[j].StartTime / 60, FList[i].Flight[j].StartTime % 60, FList[i].Flight[j].StopTime / 60, FList[i].Flight[j].StopTime % 60, FList[i].Flight[j].Cost);
		}
	}
	fclose(fp);
	return OK;
}

Status InitFiles(){	//初始化文件数据
	FILE *fp;
	int i, j, hour, minute, num, cost;
	char stmp1[SMAX];
	char stmp2[SMAX];
	char stmp3[SMAX];
	fp = fopen(Path_city, "r");
	if(!fp){
		printf("\n打开文件失败\n");
		return -1;
	}
	fscanf(fp, "%d", &num_city);
	for(i = 0; i < num_city; i++){
		fscanf(fp, "%s", &name_city[i]);
		FList[i].city = i;
		FList[i].TrainNum = 0;
		FList[i].FlightNum = 0;
	}
	fclose(fp);
	fp = fopen(Path_train, "r");
	if(!fp){
		printf("\n打开文件失败\n");
		return -1;
	}
	fscanf(fp, "%d", &num);
	for(i = 0; i < num; i++){
		fscanf(fp,"%s", &stmp1);
		fscanf(fp,"%s", &stmp2);
		fscanf(fp,"%s", &stmp3);
		j = SearchCity(stmp2);
		FList[j].Train[FList[j].TrainNum].EndCity = SearchCity(stmp3);
		strcpy(FList[j].Train[FList[j].TrainNum].name, stmp1);
		fscanf(fp, "%d:%d", &hour, &minute);
		FList[j].Train[FList[j].TrainNum].StartTime = hour * 60 + minute;
		fscanf(fp, "%d:%d", &hour, &minute);
		FList[j].Train[FList[j].TrainNum].StopTime = hour * 60 + minute;
		fscanf(fp, "%d", &cost);
		FList[j].Train[FList[j].TrainNum].Cost = cost;
		FList[j].TrainNum++;
	}
	fclose(fp);
	fp = fopen(Path_flight, "r");
	if(!fp){
		printf("\n打开文件失败\n");
		return -1;
	}
	fscanf(fp, "%d", &num);
	for(i = 0; i < num; i++){
		fscanf(fp, "%s", &stmp1);
		fscanf(fp, "%s", &stmp2);
		fscanf(fp, "%s", &stmp3);
		j = SearchCity(stmp2);
		FList[j].Flight[FList[j].FlightNum].EndCity = SearchCity(stmp3);
		strcpy(FList[j].Flight[FList[j].FlightNum].name, stmp1);
		fscanf(fp, "%d:%d", &hour, &minute);
		FList[j].Flight[FList[j].FlightNum].StartTime = hour * 60 + minute;
		fscanf(fp, "%d:%d", &hour, &minute);
		FList[j].Flight[FList[j].FlightNum].StopTime = hour * 60 + minute;
		fscanf(fp, "%d", &cost);
		FList[j].Flight[FList[j].FlightNum].Cost = cost;
		FList[j].FlightNum++;
	}
	fclose(fp);
	return OK;
}

Status InsertTrain(char *train, char *StartCity, char *EndCity, int StartTime, int EndTime, int cost){	//添加火车路线 
	int i, j;
	i = SearchCity(StartCity);
	j = SearchCity(EndCity);
	FList[i].Train[FList[i].TrainNum].Cost = cost;
	FList[i].Train[FList[i].TrainNum].EndCity = j;
	FList[i].Train[FList[i].TrainNum].StartTime = StartTime;
	FList[i].Train[FList[i].TrainNum].StopTime = EndTime;
	strcpy(FList[i].Train[FList[i].TrainNum].name, train);
	FList[i].TrainNum++;
	return OK;
}

Status InsertFlight(char *flight, char *StartCity, char *EndCity, int StartTime, int EndTime, int cost){	//添加飞机路线 
	int i,j;
	i = SearchCity(StartCity);
	j = SearchCity(EndCity);
	FList[i].Flight[FList[i].FlightNum].Cost = cost;
	FList[i].Flight[FList[i].FlightNum].EndCity = j;
	FList[i].Flight[FList[i].FlightNum].StartTime = StartTime;
	FList[i].Flight[FList[i].FlightNum].StopTime = EndTime;
	strcpy(FList[i].Flight[FList[i].FlightNum].name, flight);
	FList[i].FlightNum++;
	return OK;
}

Status DeletePath(char *name){	//删除路线 
	int i, j, flag = 0;
	for(i = 0; i < num_city; i++){
		for(j = 0; j < FList[i].FlightNum; j++){
			if(strcmp(FList[i].Flight[j].name, name) == 0){
				flag = 1;
				break;
			}
		}
		if(flag){
			for(;j < FList[i].FlightNum - 1; j++){
				FList[i].Flight[j].Cost = FList[i].Flight[j+1].Cost;
				FList[i].Flight[j].EndCity = FList[i].Flight[j+1].EndCity;
				strcpy(FList[i].Flight[j].name, FList[i].Flight[j+1].name);
				FList[i].Flight[j].StartTime = FList[i].Flight[j+1].StartTime;
				FList[i].Flight[j].StopTime = FList[i].Flight[j+1].StopTime;
			}
			FList[i].FlightNum--;
			return OK;
		}
		for(j = 0; j < FList[i].TrainNum; j++){
			if(strcmp(FList[i].Train[j].name, name) == 0){
				flag = 1;
				break;
			}
		}
		if(flag){
			for (; j < FList[i].TrainNum - 1; j++){
				FList[i].Train[j].Cost = FList[i].Train[j+1].Cost;
				FList[i].Train[j].EndCity = FList[i].Train[j+1].EndCity;
				strcpy(FList[i].Train[j].name, FList[i].Train[j+1].name);
				FList[i].Train[j].StartTime = FList[i].Train[j+1].StartTime;
				FList[i].Train[j].StopTime = FList[i].Train[j+1].StopTime;
			}
			FList[i].TrainNum--;
			return OK;
		}
	}
	printf("未找到该路线！\n\n\n\n");
	return -1;
}

void Output_Dijkstra(int matx[DMAX][DMAX], int PreCity[DMAX], int p_end, int TravelType){	//迪杰斯特拉算法输出花费最少路线 
	int track[DMAX];
	int i = 0, j, k, min, tmp, end, cost = 0;
	int startH, startM, endH, endM;
	j = p_end;
	track[i++] = j;
	while(PreCity[j] >= 0){
		cost += matx[PreCity[j]][j];
		track[i++] = j = PreCity[j];
	}
	printf("\n\n\n\n最小花费：%d元", cost);
	printf("\n出发地：%s", name_city[track[i -1]]);
	printf("\t目的地：%s\n\n", name_city[track[0]]);
	printf("\n最小费用路线为：\n");
	if(!TravelType){
		for(i--; i > 0; i--){
			end = track[i - 1];
			min = 32767;
			for(k = 0; k < FList[track[i]].TrainNum; k++){
				if(FList[track[i]].Train[k].EndCity == end and min > FList[track[i]].Train[k].Cost){
					min = FList[track[i]].Train[k].Cost;
					tmp = k;
				}
			}
			printf("\n班次：%s", FList[track[i]].Train[tmp].name);
			printf("\n起始站：%s	终点站：%s", name_city[track[i]], name_city[track[i - 1]]);
			printf("\n始末时间：");
			startH = FList[track[i]].Train[tmp].StartTime / 60 ;
			startM = FList[track[i]].Train[tmp].StartTime % 60;
			endH = FList[track[i]].Train[tmp].StopTime / 60 ;
			endM = FList[track[i]].Train[tmp].StopTime % 60 ;
			if(!(startH / 10)){
				printf("0");
			}
			printf("%d:", startH);
			if(!(startM / 10)){
				printf("0");
			}
			printf("%d -- ", startM);
			if(!(endH / 10)){
				printf("0");
			}
			printf("%d:", endH);
			if(!(endM / 10)){
				printf("0");
			}
			printf("%d\n", endM);
		}
	}
	else{
		for(i--; i > 0; i--){
			end = track[i-1];
			min = 32767;
			for(k = 0; k < FList[track[i]].FlightNum; k++){
				if(FList[track[i]].Flight[k].EndCity == end and min > FList[track[i]].Flight[k].Cost){
					min = FList[track[i]].Flight[k].Cost;
					tmp = k;
				}
			}
			printf("\n班次：%s", FList[track[i]].Flight[tmp].name);
			printf("\n起始站：%s	终点站：%s", name_city[track[i]], name_city[track[i - 1]]);
			printf("\n始末时间：");
			startH = FList[track[i]].Flight[tmp].StartTime / 60;
			startM = FList[track[i]].Flight[tmp].StartTime % 60;
			endH = FList[track[i]].Flight[tmp].StopTime / 60 ;
			endM = FList[track[i]].Flight[tmp].StopTime % 60 ;
			if(!(startH / 10)){
				printf("0");
			}
			printf("%d:", startH);
			if(!(startM / 10)){
				printf("0");
			}
			printf("%d -- ", startM);
			if(!(endH/10)){
				printf("0");
			}
			printf("%d:", endH);
			if(!(endM / 10)){
				printf("0");
			}
			printf("%d\n", endM);
		}
	}
}

void Dijkstra(int matx[DMAX][DMAX], int p_start, int p_end, int TravelType){	//迪杰斯特拉算法寻找花费最少路线 
	int PreCity[DMAX]; 
	int i, j, min, pre, pos;
	for(i = 0; i < num_city; i++){
		PreCity[i] = -1;
	}
	PreCity[p_start] = -2;
	while(PreCity[p_end] == -1){
		min = -1;
		for(i = 0; i < num_city; i++){
			if(PreCity[i] != -1){
				for(j = 0; j < num_city; j++){
					if(PreCity[j] == -1 and matx[i][j] > 0 and (min < 0 or matx[i][j] < min)){
						pre = i;
						pos = j;
						min = matx[i][j];
					}
				}
			}
		}
		PreCity[pos] = pre;
	}
	Output_Dijkstra(matx, PreCity, p_end, TravelType);
}

Status SearchMinCost(int StartCity, int EndCity, int TravelType){	//寻找花费最少路线
	int ma[DMAX][DMAX];
	int i, j, min, end;
	for(i = 0; i < num_city; i++){
		for(j = 0; j < num_city; j++){
			ma[i][j]=-1;
		}
	}
	if(TravelType == 0){
		for(i = 0; i < num_city; i++){
			min = 32767;
			j = 0;
			while(j < FList[i].TrainNum){
				min = 32767;
				end = FList[i].Train[j].EndCity;
				while(end == FList[i].Train[j].EndCity and j < FList[i].TrainNum){
					if (FList[i].Train[j].Cost < min){
						min = FList[i].Train[j].Cost;
					}
					j++;
				}
				ma[i][end] = min;
			}
		}
	}
	else{
		for(i = 0; i < num_city; i++){
			min = 32767;
			j = 0;
			while(j < FList[i].FlightNum){
				min = 32767;
				end = FList[i].Flight[j].EndCity;
				while(end == FList[i].Flight[j].EndCity and j < FList[i].FlightNum){
					if(FList[i].Flight[j].Cost < min){
						min = FList[i].Flight[j].Cost;
					}
					j++;
				}
				ma[i][end] = min;
			}
		}
	}
	Dijkstra(ma, StartCity, EndCity, TravelType);
	return OK;
}

Status SearchMinTime(CityType City, CityType EndCity, int CurTime, int CPathNo, int TravelType){	 //寻找耗时最短路线 
	int i;
	if(City == EndCity){
		if(MinTime > CurTime - StartTime){
			for(i = 0;i <= CPathNo; i++){
				MinPath[i].City = Path[i].City;
				MinPath[i].TraNo = Path[i].TraNo;
				CPath = CPathNo;
			}
			MinTime = CurTime - StartTime;
		}
	}
	else{
		CPathNo++;
		Path[CPathNo].City = City;
		if(!TravelType){
			for(i = 0; i < FList[City].TrainNum; i++){
				if((FList[City].Train[i].StartTime >= (CurTime % 1440)) and (FList[City].Train[i].StopTime + (CurTime / 1440) * 1440 - StartTime < MinTime)){
					Path[CPathNo].TraNo = i;
					SearchMinTime(FList[City].Train[i].EndCity, EndCity, FList[City].Train[i].StopTime + (CurTime / 1440) * 1440, CPathNo, TravelType);
				}
				if((FList[City].Train[i].StartTime < (CurTime % 1440)) and (FList[City].Train[i].StopTime + (CurTime / 1440) * 1440 - StartTime < MinTime)){
					Path[CPathNo].TraNo = i;
					SearchMinTime(FList[City].Train[i].EndCity, EndCity, FList[City].Train[i].StopTime + (CurTime / 1440 + 1) * 1440, CPathNo, TravelType);
				}
			}
		}
		else{
			for(i = 0; i < FList[City].FlightNum; i++){
				if((FList[City].Flight[i].StartTime >= CurTime) and (FList[City].Flight[i].StopTime + (CurTime / 1440) * 1440 - StartTime < MinTime)){
					Path[CPathNo].TraNo = i;
					SearchMinTime(FList[City].Flight[i].EndCity, EndCity, FList[City].Flight[i].StopTime + (CurTime / 1440) * 1440, CPathNo, TravelType);
				}
				if((FList[City].Flight[i].StartTime < CurTime) and (FList[City].Flight[i].StopTime + (CurTime / 1440) * 1440 - StartTime < MinTime)){
					Path[CPathNo].TraNo = i;
					SearchMinTime(FList[City].Flight[i].EndCity, EndCity, FList[City].Flight[i].StopTime + (CurTime / 1440 + 1) * 1440, CPathNo, TravelType);
				}
			}
		}
	}
	return OK;
}

Status FindMinTime(int StartCity, int EndCity, int TravelType){	//输出耗时最短路线 
	int i;
	int startH, startM, endH, endM;
	MinTime = 32767;
	CPath = 0;
	Path[0].City = StartCity;
	if(!TravelType){
		for(i = 0; i < FList[StartCity].TrainNum; i++){
			Path[0].TraNo = i;
			StartTime = FList[StartCity].Train[i].StartTime;
			SearchMinTime(FList[StartCity].Train[i].EndCity, EndCity, FList[StartCity].Train[i].StopTime, 0, TravelType);
		}
	}
	else{
		for(i = 0; i < FList[StartCity].FlightNum; i++){
			Path[0].TraNo = i;
			StartTime = FList[StartCity].Flight[i].StartTime;
			SearchMinTime(FList[StartCity].Flight[i].EndCity, EndCity, FList[StartCity].Flight[i].StopTime, 0, TravelType);
		}
	}
	if(MinTime == 32767){
		printf("\n错误!\n\n\n\n");
		return 0;
	}
	printf("\n\n\n\n最短耗时（包括中转等待时间）：%2d小时%2d分钟", MinTime / 60, MinTime % 60);
	printf("\n出发地：%s", name_city[StartCity]);
	printf("\t目的地：%s\n\n", name_city[EndCity]);
	printf("\n最短耗时路线为：\n");
	for (i = 0; i <= CPath; i++){
		if(!TravelType){
			printf("\n班次：%s", FList[MinPath[i].City].Train[MinPath[i].TraNo].name);
			if(i == CPath){
				printf("\n起始站：%s	终点站：%s", name_city[MinPath[i].City], name_city[EndCity]);
			} 
			else{
				printf("\n起始站：%s	终点站：%s", name_city[MinPath[i].City], name_city[MinPath[i + 1].City]);
			}
			printf("\n始末时间：");
			startH = FList[MinPath[i].City].Train[MinPath[i].TraNo].StartTime / 60;
			startM = FList[MinPath[i].City].Train[MinPath[i].TraNo].StartTime % 60;
			endH = FList[MinPath[i].City].Train[MinPath[i].TraNo].StopTime / 60;
			endM = FList[MinPath[i].City].Train[MinPath[i].TraNo].StopTime % 60;
			if(!(startH / 10)){
				printf("0");
			}
			printf("%d:", startH);
			if(!(startM / 10)){
				printf("0");
			}
			printf("%d -- ", startM);
			if(!(endH / 10)){
				printf("0");
			}
			printf("%d:", endH);
			if(!(endM / 10)){
				printf("0");
			}
			printf("%d\n", endM);
		}
		else{
			printf("\n班次：%s", FList[MinPath[i].City].Flight[MinPath[i].TraNo].name);
			if(i == CPath){
				printf("\n起始站：%s	终点站：%s", name_city[MinPath[i].City], name_city[EndCity]);
			} 
			else{
				printf("\n起始站：%s	终点站：%s", name_city[MinPath[i].City], name_city[MinPath[i + 1].City]);
			}
			printf("\n始末时间：");
			startH = FList[MinPath[i].City].Flight[MinPath[i].TraNo].StartTime / 60;
			startM = FList[MinPath[i].City].Flight[MinPath[i].TraNo].StartTime % 60;
			endH = FList[MinPath[i].City].Flight[MinPath[i].TraNo].StopTime / 60;
			endM = FList[MinPath[i].City].Flight[MinPath[i].TraNo].StopTime % 60;
			if(!(startH / 10)){
				printf("0");
			}
			printf("%d:", startH);
			if(!(startM / 10)){
				printf("0");
			}
			printf("%d -- ", startM);
			if(!(endH / 10)){
				printf("0");
			}
			printf("%d:", endH);
			if(!(endM / 10)){
				printf("0");
			}
			printf("%d\n", endM);
		}
	}
	return OK;
}

void Menu_1(){	//菜单1 
	printf("\t\t\t************************************\n");
	printf("\t\t\t*          全国交通咨询模拟        *\n");
	printf("\t\t\t*             请选择功能           *\n");
	printf("\t\t\t************************************\n");
	printf("\t\t\t*            1.用户咨询            *\n");
	printf("\t\t\t************************************\n");
	printf("\t\t\t*            2.管理员编辑          *\n");
	printf("\t\t\t************************************\n");
	printf("\t\t\t*            0.退出                *\n");
	printf("\t\t\t************************************\n");
	printf("\t\t\t        ********************        \n"); 
	printf("\t\t\t        *     你的操作     *        \n");
	printf("\t\t\t        ********************        \n"); 	
	printf("\t\t\t\t\t  ");
}

void Menu_2(){	//菜单2 
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    1.添加城市           *    2.删除城市        *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    3.添加路线           *    4.删除路线        *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    0.返回                                      *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t                ********************               \n"); 
	printf("\t\t\t                *     你的操作     *               \n");
	printf("\t\t\t                ********************               \n"); 	
	printf("\t\t\t\t\t\t  ");
}

int main(){
	char name[SMAX], city_1[SMAX], city_2[SMAX];
	char s_city[SMAX];
	char e_city[SMAX];
	int op, op_1, op_2, op_2_1, op_2_2, cost;
	int startcity, endcity, traveltype;
	int s_hour, s_minute, e_hour, e_minute;
	while(1){
		Menu_1();
		scanf("%d", &op); 
		switch(op){
			case 1:{	//用户咨询 
				system("cls");
				printf("\t\t\t**************************************************\n");
				printf("\t\t\t*       1.花费最优       *       2.耗时最优      *\n");
				printf("\t\t\t**************************************************\n");
				printf("\t\t\t*       0.返回                                   *\n");
				printf("\t\t\t**************************************************\n");
				printf("\t\t\t                ********************               \n"); 
				printf("\t\t\t                *     你的操作     *               \n");
				printf("\t\t\t                ********************               \n"); 
				printf("\t\t\t\t\t\t  ");
				scanf("%d", &op_1); 
				switch(op_1){
					case 1:{	//最小耗费
						InitFiles();
						begin_5:{
							printf("\n请输入起始城市：");
							scanf("%s", &name);
							startcity = SearchCity(name);
							printf("请输入终点城市：");
							scanf("%s", &name);
							endcity = SearchCity(name);
							printf("请选择交通工具（列车 0	航班 1）：");
							scanf("%d", &traveltype);
							if((traveltype != 0 and traveltype != 1) or startcity == -1 or endcity == -1 or startcity == endcity){
								printf("\n\n输入错误！\n\n");
								goto begin_5;
							} 
							SearchMinCost(startcity, endcity, traveltype);
							printf("\n");
							break;
						}		
					}
					case 2:{	//最短耗时 
						InitFiles();
						begin_6:{
							printf("\n请输入起始城市：");
							scanf("%s", &name);
							startcity = SearchCity(name);
							printf("请输入终点城市：");
							scanf("%s", &name);
							endcity = SearchCity(name);
							printf("请选择交通工具（列车 0	航班 1）：");
							scanf("%d", &traveltype);
							if((traveltype != 0 and traveltype != 1) or startcity == -1 or endcity == -1  or startcity == endcity){
								printf("\n\n输入错误！\n\n");
								goto begin_6;
							} 
							FindMinTime(startcity, endcity, traveltype);
							printf("\n");
							break;
						} 
					}
					case 0:{
						system("cls");
						main();
						break;
					}
				} 
				break;
			} 
			case 2:{	//管理员编辑 
				system("cls");
				printf("\t\t\t**************************************************\n");
				printf("\t\t\t*       1.键盘输入       *       2.文件编辑      *\n");
				printf("\t\t\t**************************************************\n");
				printf("\t\t\t                ********************               \n"); 
				printf("\t\t\t                *     你的操作     *               \n");
				printf("\t\t\t                ********************               \n"); 	
				printf("\t\t\t\t\t\t  ");
				scanf("%d", &op_2); 
				switch(op_2){
					case 1:{	//键入 
						system("cls");
						Menu_2();
						scanf("%d", &op_2_1); 
						switch(op_2_1){
							case 1:{	//添加城市 
								InitFiles();
								printf("\n请输入要添加的城市名：");
								scanf("%s", &city_1);
								if(InsertCity(city_1) != -1){
									ToFiles();
									printf("添加成功!\n\n\n\n");
								}
								break;
							}
							case 2:{	//删除城市
								InitFiles();
								printf("\n输入要删除的城市名：");
								scanf("%s", &city_2);
								if(DeleteCity(city_2) != -1){
									ToFiles();
									printf("删除成功!\n");
								}
								break;
							}
							case 3:{	//添加路线
								InitFiles();
								begin_3:{
									printf("请输入起始城市：");
									scanf("%s", &s_city);
									printf("请输入终点城市：");
									scanf("%s", &e_city);
									printf("请选择交通工具（列车 0航班 1）:");
									scanf("%d", &traveltype);
									if(traveltype) {
										printf("请输入飞机班次：");
										scanf("%s", &name);
									}
									else{
										printf("请输入列车班次：");
										scanf("%s", &name);
									}
									printf("请输入起始时刻(00:0024 小时制)：");
									scanf("%2d:%2d", &s_hour, &s_minute);
									printf("请输入到达时刻(00:0024 小时制)：");
									scanf("%2d:%2d", &e_hour, &e_minute);
									printf("请输入票价：");
									scanf("%d", &cost);
									if(s_hour > 24 or e_hour > 24 or s_minute > 60 or e_minute > 60 or (traveltype != 0 and traveltype != 1) or SearchCity(s_city) == -1 or SearchCity(e_city) == -1){
										printf("\n\n输入错误！\n\n");
										goto begin_3;
									} 
									if(traveltype){
										InsertFlight(name, s_city, e_city, s_hour * 60 + s_minute, e_hour * 60 + e_minute, cost);
									}
									else{
										InsertTrain(name, s_city, e_city, s_hour * 60 + s_minute, e_hour * 60 + e_minute, cost);
									}
									ToFiles();
									printf("添加成功!\n\n\n\n");
									break;
								}
							}
							case 4:{	//删除路线
								InitFiles();
								printf("请输入班次：");
								scanf("%s", &name);
								if(DeletePath(name) != -1){
									ToFiles();
									printf("删除路线成功!\n");
								}
								break;
							}
							case 0:{
								system("cls");
								main();
								break;
							}
						}
						break;
					}
					case 2:{	//文件 
						system("cls");
						printf("\t\t\t**************************************************\n");
						printf("\t\t\t*     1.城市     *     2.火车     *     3.航班   *\n");
						printf("\t\t\t**************************************************\n");
						printf("\t\t\t                ********************               \n"); 
						printf("\t\t\t                *     你的操作     *               \n");
						printf("\t\t\t                ********************               \n"); 
						printf("\t\t\t\t\t\t  ");
						scanf("%d", &op_2_2); 
						if(op_2_2 == 1){
							printf("提示：根据原有格式输入！"); 
							system("city.txt");
							system("cls");
						}
						if(op_2_2 == 2){
							printf("提示：根据原有格式输入！"); 
							system("train.txt");
							system("cls");
						}
						if(op_2_2 == 3){
							printf("提示：根据原有格式输入！"); 
							system("flight.txt");
							system("cls");
						}
						break;
					}
				}
				break;
			}
			case 0:{	 
				return 0;
			}
		}
	}
}
