#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE   1
#define FALSE  0
#define OK     1
#define ERROR  0
#define IBFEASIBLE  -1
#define OVERFLOW    -2 

#define MAXLEN  100
#define MAXSIZE 20

#define UNVISITED 0
#define VITITED 1

typedef char VexType;
typedef int Status;

typedef struct{			//队列 
    char data[MAXSIZE];	//数据 
    int front;  		//头指针
    int rear;   		//尾指针
}SqQueue;

typedef struct{			//邻接矩阵类型
	VexType *vexs;		//顶点数组
	int **arcs;			//关系数组，用0或1表示相邻否 
	int n, e;			//顶点数和边数
	int *tags;			//标志数组，可用于在图的遍历中标记顶点
}MGraph;				

typedef struct{			//边的信息 
	VexType v, w;		//边的端点 
}ArcInfo;				

void InitQueue(SqQueue *Q){	//队列初始化
    Q->front = 0;
    Q->rear = 0;
}

bool EnQueue(SqQueue *Q, char e){	//入队
    if((Q->rear + 1) % MAXSIZE == Q->front){
    	return false;
	}
    Q->data[Q->rear] = e;
    Q->rear = (Q->rear + 1) % MAXSIZE;
    return true;
}

char* DeQueue(SqQueue *Q, char *e){	//出队，删除队首元素，并赋给e
    if(Q->front == Q->rear){
    	return NULL;
	} 
    *e = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXSIZE;
    return e;
}

bool isEmptyQueue(SqQueue *Q){	//队列判空
    return Q->front == Q->rear ? true : false;
}

Status PrintGraph(MGraph G){	//输出图的邻接矩阵 
	int i, j;
	printf("\n\n\n\n");			
	printf("图的邻接的矩阵为：\n");
	for(i = 0; i < G.n; i++){
		printf("%d %c\t", i, G.vexs[i]);
		for(j = 0; j < G.n; j++){
			printf("%d ", G.arcs[i][j]);
		}
		printf("\n");
	}
	printf("\n\n\n\n");
	return OK;
}

Status InitGraph(MGraph &G, VexType *vexs, int n){	//初始化含n个顶点且无边的图G
	int i, j;
	if(n < 0 or (n > 0 and !vexs)){
		printf("信息出错！\n");
		return ERROR;
	}
	G.n = n;
	G.e = 0;	//顶点和边数 
	if(n == 0){
		printf("初始化成功！\n");
		return OK;	//空图 
	}
	if(!(G.vexs = (VexType*)malloc(n * sizeof(VexType)))){
		printf("初始化失败！\n");
		return OVERFLOW;
	}
	for(i = 0; i < G.n; i++){
		G.vexs[i] = vexs[i];	//建立顶点数组 
	}
	if(!(G.arcs = (int**)malloc(n * sizeof(int*)))){	//分配指针数组 
		printf("初始化失败！\n");
		return OVERFLOW;
	}
	for(i = 0; i < n; i++){	//分配每个指针所指向的数组 
		if(!(G.arcs[i] = (int*)malloc(n * sizeof(int)))){
			printf("初始化失败！\n");
			return OVERFLOW;
		}
	}
	if(!(G.tags = (int*)malloc(n * sizeof(int)))){
		printf("初始化失败！\n");
		return OVERFLOW;
	}
	for(i = 0; i < n; i++){	//初始化标志数组和关系数组 
		G.tags[i] = 0;
		for(j = 0; j < n; j++){
			G.arcs[i][j] = 0;
		}
	}
	printf("初始化成功！\n");
	return OK;
}

Status CreatGraph(MGraph &G, VexType *vexs, int n, ArcInfo *arcs, int e){	//创建n个顶点和e条边的图G，vexs为顶点信息，arcs为边信息
	int LocateVex(MGraph G, VexType v);	
	if(n < 0 or e < 0 or (n > 0 and vexs == NULL) or (e > 0 and arcs == NULL) or !InitGraph(G, vexs, n)){
		printf("创建失败！\n");
    	return ERROR;
  	}
  	int i, j, k;
  	VexType v, w;
  	G.e = e;
  	G.n = n;
  	for(i = 0; i<G.n; i++){
    	G.vexs[i] = vexs[i];
  	}
	for(k=0;k<G.e;k++){
	    v = arcs[k].v;
	    w = arcs[k].w;
	    i = LocateVex(G, v);
	    j = LocateVex(G, w);
	    if(i < 0 or j < 0){
	    	printf("创建失败！\n");
	    	return ERROR;
	    }
	    G.arcs[i][j] = 1;
	    G.arcs[j][i] = 1;
	  }
	printf("创建成功！\n");
	return OK;
}

Status DestroyGraph(MGraph &G){	//销毁图G
	if(!G.n){
		printf("该图不存在，销毁失败！\n");
		return ERROR;
	}
	int i, j;
	for(i = 0; i < G.n; i++){
		G.tags[i] = 0;
		G.vexs[i] = 0;
		for(j = 0; j < G.n; j++){
			G.arcs[i][j] = 0;
			G.arcs[j][i] = 0;
		}
	}
	G.n = 0;
	G.e = 0;
	free(G.arcs);
	free(G.vexs);
	free(G.tags);
	printf("销毁成功！\n");
	return OK;
}

int LocateVex(MGraph G, VexType v){	//查找顶点v在图G中的位序
	int i;
	for(i = 0; i < G.n; i++){
		if(v == G.vexs[i]){
			return i;
		}
	}
	printf("该节点不存在！\n");
	return -1;
}

Status GetVex(MGraph G, int k, VexType &w){	//取图G的k顶点赋值到w
	int i;
	for(i = 0; i < G.n; i++){
		if(k == i){
			w = G.vexs[i];
			return OK;
		}
	}
	printf("该节点不存在！\n");
	return -1;
}

Status PutVex(MGraph G, int k, VexType w){	//取图G的k顶点赋值w
	int i;
	for(i = 0; i < G.n; i++){
		if(k == i){
			G.vexs[i] = w;
			printf("赋值成功！");
			return OK;
		}
	}
	printf("该节点不存在！\n");
	return -1;
}

int FirstAdjVex(MGraph G, int k){	//求图G中k顶点的第一个邻接顶点的位序
	int i;
	if(k < 0 or k >= G.n){
		printf("该节点不存在！");
		return -1;
	}
	for(i = 0; i < G.n; i++){
		if(G.arcs[k][i]){
			return i;
		}
	}
	printf("该节点无邻接顶点！"); 
	return -1;
}

int NextAdjVex(MGraph G, int k, int m){	//m顶点为k顶点的邻接顶点，求图G中k顶点相对于m顶点的下一个邻接顶点的位序
	int i;
	if(k == 0 and m == 0){
		return 0;  
	}
	for(i = m + 1; i < G.n; i++){
		if(G.arcs[k][i]){
		  return i;
		}
	}
	if(i == (G.n - 1)){
		printf("该节点无邻接顶点！"); 
		return -1;
	}
	printf("输入有误！");
	return -1;
}

Status AddArc(MGraph &G, int k, int m){	//在图G中增加k顶点到m顶点的边或弧
	if(k < 0 or m < 0 or k >= G.n or m >= G.n){
		printf("输入错误！\n");
		return -1; 
	}
	if(G.arcs[k][m] == 1){
		printf("该边已存在！\n");
		return -1; 
	}
	G.arcs[k][m] = 1;
	printf("增加成功！\n");
	return OK;
}

Status RemoveArc(MGraph &G, int k, int m){	//在图G中删除k顶点到m顶点的边或弧 
	if(k < 0 or m < 0 or k >= G.n or m >= G.n){
		printf("输入错误！\n");
		return -1; 
	}
	if(G.arcs[k][m] == 0){
		printf("该边不存在！\n");
		return -1; 
	}
	G.arcs[k][m] = 0;
	printf("删除成功！\n");
	return OK;
}

void DFS(MGraph G, int k){	//从连通图G的k顶点出发进行深度优先遍历 
    int j;
    printf("%c ", G.vexs[k]);
    G.tags[k] = 1;
    for(j = 0; j < G.n; j++){
        if(G.arcs[k][j] != 0 and !G.tags[j]){
            DFS(G, j);
        }
    }
}

void DFSTraverse(MGraph G){	//深度优先遍历图G
    int i;
    for(i = 0; i < G.n; i++){
        G.tags[i] = 0;
    }
    for(i = 0; i < G.n; i++){
        if(!G.tags[i]){
            DFS(G, i);
        }
    }
}

void BFSTraverse(MGraph G){	//广度优先遍历图G
	SqQueue Q;
    int i, j, mark;
    char data;
    for(i = 0; i < G.n; i++){
    	G.tags[i] = 0;
	}
    InitQueue(&Q);	//初始化队列
    for(i = 0; i < G.n; i++){	//对未访问的顶点做BFS
        if(!G.tags[i]){
            G.tags[i] = 1;
            EnQueue(&Q, G.vexs[i]);
            while(!isEmptyQueue(&Q)){
                DeQueue(&Q, &data);  //队首顶点出队，并赋值给data
                printf("%c ", data);
                for(j = 0; j < G.n; j++){	//找所删除顶点的下标，更新该下标值，以便正确找到与出队元素相连的其他顶点
                    if(G.vexs[j] == data){
                    	mark = j;
					}
            	}
                for(j = 0; j < G.n; j++){
                    if(G.arcs[mark][j] == 1 and !G.tags[j]){
                        G.tags[j] = 1;
                        EnQueue(&Q, G.vexs[j]);
                    }
                }
            }
        }
    }
}

int main(){
	MGraph G;
	VexType vexs_1[MAXSIZE];
	ArcInfo arcs_1[MAXSIZE];
	int n_1, e_1;
	int op;
	int k_3, k_4, k_5, k_6, k_7, k_8;
	int m_6, m_7, m_8;
	int temp_1, temp_2, temp_5, temp_6;
	char v_1, v_2;
	char w_3, w_4, w_5, w_6;
	begin:{
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*           	  无向图UDG基本操作              *\n");
		printf("\t\t\t*                    请选择功能                  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.创建一个无向图     *    2.查找顶点的位序  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.查找顶点的值       *    4.赋值图的顶点    *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    5.查找顶点的第一个邻接顶点                  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    6.查找顶点相对于中间顶点的下一个邻接顶点    *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    7.增加一条边         *    8.删除一条边      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    9.DFS                *    10.BFS            *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    11.销毁一个图        *    0.退出            *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t                ********************               \n"); 
		printf("\t\t\t                *     你的操作     *               \n");
		printf("\t\t\t                ********************               \n"); 	
		printf("\t\t\t\t\t\t  ");
		scanf("%d",&op); 
		getchar();
		switch(op){
			case 1: {
				printf("请输入节点数：");
				scanf("%d", &n_1);
				getchar();
				printf("请输入边数：");
				scanf("%d", &e_1);
				getchar();
				if(e_1 > (n_1 * (n_1 - 1) / 2)){
					printf("输出错误！");
				}
				else{
					for(temp_1 = 0; temp_1 < n_1; temp_1++){
						printf("请输入一个节点：");
						scanf("%c", &v_1);
						getchar();
						vexs_1[temp_1] = v_1;
					}
					for(temp_1 = 0; temp_1 < e_1; temp_1++){
						printf("请输入相邻两边的第一个端点：");
						scanf("%c", &arcs_1[temp_1].v);
						getchar();
						printf("请输入相邻两边的第二个端点：");
						scanf("%c", &arcs_1[temp_1].w);
						getchar();
					} 
					CreatGraph(G, vexs_1, n_1, arcs_1, e_1);
					PrintGraph(G);	
					goto begin;
					break;	
				}
			}
			case 2:	{
				printf("\n请输入要查找位序的顶点：");
				scanf("%c", &v_2);
				getchar();
				temp_2 = LocateVex(G, v_2); 
				if(temp_2 != -1){
					printf("该顶点的位序为：%d\n", temp_2);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 3:	{
				printf("\n请输入要查找的顶点位序：");
				scanf("%d", &k_3);
				getchar();
				if(GetVex(G, k_3, w_3) != -1){
					printf("该顶点的值为：%c\n", w_3);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 4:	{
				printf("\n请输入要赋值的顶点位序：");
				scanf("%d", &k_4);
				getchar();
				printf("请输入要赋的值：");
				scanf("%c", &w_4);
				getchar();
				if(PutVex(G, k_4, w_4) != -1){
					PrintGraph(G);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 5: {
				printf("\n请输入要查找的顶点位序：");
				scanf("%d", &k_5);
				getchar();
				temp_5 = FirstAdjVex(G, k_5); 
				if(temp_5 != -1){
					GetVex(G, temp_5, w_5);
					printf("该顶点的第一个邻接顶点为：%c\n", w_5);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 6: {
				printf("\n请输入要查找的顶点位序：");
				scanf("%d", &k_6);
				getchar();
				printf("请输入中间顶点的位序：");
				scanf("%d", &m_6);
				getchar();
				temp_6 = NextAdjVex(G, k_6, m_6); 
				if(temp_6 != -1){
					GetVex(G, temp_6, w_6);
					printf("该顶点相对于中间顶点的下一个邻接顶点为：%c\n", w_6);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 7: {
				printf("\n请输入要增加的边的一个端点位序：");
				scanf("%d", &k_7);
				getchar();
				printf("\n请输入要增加的边的另一个端点位序：");
				scanf("%d", &m_7);
				getchar();
				if(AddArc(G, k_7, m_7) != -1){
					PrintGraph(G);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 8: {
				printf("\n请输入要删除的边的一个端点位序：");
				scanf("%d", &k_8);
				getchar();
				printf("\n请输入要删除的边的另一个端点位序：");
				scanf("%d", &m_8);
				getchar();
				if(RemoveArc(G, k_8, m_8) != -1){
					PrintGraph(G);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 9: {
				printf("\n经DFS遍历后的序列为：");
				DFSTraverse(G);
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 10: {
				printf("\n经BFS遍历后的序列为：");
				BFSTraverse(G);
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 11: {
				DestroyGraph(G); 
				PrintGraph(G);
				goto begin;
				break;
			}
			case 0:	{
				printf("\n\n\n感谢使用！");
				exit(0);
				break;
			}
		}
	}
	return 0;
}
