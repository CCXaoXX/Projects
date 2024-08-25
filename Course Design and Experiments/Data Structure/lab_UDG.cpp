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

typedef struct{			//���� 
    char data[MAXSIZE];	//���� 
    int front;  		//ͷָ��
    int rear;   		//βָ��
}SqQueue;

typedef struct{			//�ڽӾ�������
	VexType *vexs;		//��������
	int **arcs;			//��ϵ���飬��0��1��ʾ���ڷ� 
	int n, e;			//�������ͱ���
	int *tags;			//��־���飬��������ͼ�ı����б�Ƕ���
}MGraph;				

typedef struct{			//�ߵ���Ϣ 
	VexType v, w;		//�ߵĶ˵� 
}ArcInfo;				

void InitQueue(SqQueue *Q){	//���г�ʼ��
    Q->front = 0;
    Q->rear = 0;
}

bool EnQueue(SqQueue *Q, char e){	//���
    if((Q->rear + 1) % MAXSIZE == Q->front){
    	return false;
	}
    Q->data[Q->rear] = e;
    Q->rear = (Q->rear + 1) % MAXSIZE;
    return true;
}

char* DeQueue(SqQueue *Q, char *e){	//���ӣ�ɾ������Ԫ�أ�������e
    if(Q->front == Q->rear){
    	return NULL;
	} 
    *e = Q->data[Q->front];
    Q->front = (Q->front + 1) % MAXSIZE;
    return e;
}

bool isEmptyQueue(SqQueue *Q){	//�����п�
    return Q->front == Q->rear ? true : false;
}

Status PrintGraph(MGraph G){	//���ͼ���ڽӾ��� 
	int i, j;
	printf("\n\n\n\n");			
	printf("ͼ���ڽӵľ���Ϊ��\n");
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

Status InitGraph(MGraph &G, VexType *vexs, int n){	//��ʼ����n���������ޱߵ�ͼG
	int i, j;
	if(n < 0 or (n > 0 and !vexs)){
		printf("��Ϣ����\n");
		return ERROR;
	}
	G.n = n;
	G.e = 0;	//����ͱ��� 
	if(n == 0){
		printf("��ʼ���ɹ���\n");
		return OK;	//��ͼ 
	}
	if(!(G.vexs = (VexType*)malloc(n * sizeof(VexType)))){
		printf("��ʼ��ʧ�ܣ�\n");
		return OVERFLOW;
	}
	for(i = 0; i < G.n; i++){
		G.vexs[i] = vexs[i];	//������������ 
	}
	if(!(G.arcs = (int**)malloc(n * sizeof(int*)))){	//����ָ������ 
		printf("��ʼ��ʧ�ܣ�\n");
		return OVERFLOW;
	}
	for(i = 0; i < n; i++){	//����ÿ��ָ����ָ������� 
		if(!(G.arcs[i] = (int*)malloc(n * sizeof(int)))){
			printf("��ʼ��ʧ�ܣ�\n");
			return OVERFLOW;
		}
	}
	if(!(G.tags = (int*)malloc(n * sizeof(int)))){
		printf("��ʼ��ʧ�ܣ�\n");
		return OVERFLOW;
	}
	for(i = 0; i < n; i++){	//��ʼ����־����͹�ϵ���� 
		G.tags[i] = 0;
		for(j = 0; j < n; j++){
			G.arcs[i][j] = 0;
		}
	}
	printf("��ʼ���ɹ���\n");
	return OK;
}

Status CreatGraph(MGraph &G, VexType *vexs, int n, ArcInfo *arcs, int e){	//����n�������e���ߵ�ͼG��vexsΪ������Ϣ��arcsΪ����Ϣ
	int LocateVex(MGraph G, VexType v);	
	if(n < 0 or e < 0 or (n > 0 and vexs == NULL) or (e > 0 and arcs == NULL) or !InitGraph(G, vexs, n)){
		printf("����ʧ�ܣ�\n");
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
	    	printf("����ʧ�ܣ�\n");
	    	return ERROR;
	    }
	    G.arcs[i][j] = 1;
	    G.arcs[j][i] = 1;
	  }
	printf("�����ɹ���\n");
	return OK;
}

Status DestroyGraph(MGraph &G){	//����ͼG
	if(!G.n){
		printf("��ͼ�����ڣ�����ʧ�ܣ�\n");
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
	printf("���ٳɹ���\n");
	return OK;
}

int LocateVex(MGraph G, VexType v){	//���Ҷ���v��ͼG�е�λ��
	int i;
	for(i = 0; i < G.n; i++){
		if(v == G.vexs[i]){
			return i;
		}
	}
	printf("�ýڵ㲻���ڣ�\n");
	return -1;
}

Status GetVex(MGraph G, int k, VexType &w){	//ȡͼG��k���㸳ֵ��w
	int i;
	for(i = 0; i < G.n; i++){
		if(k == i){
			w = G.vexs[i];
			return OK;
		}
	}
	printf("�ýڵ㲻���ڣ�\n");
	return -1;
}

Status PutVex(MGraph G, int k, VexType w){	//ȡͼG��k���㸳ֵw
	int i;
	for(i = 0; i < G.n; i++){
		if(k == i){
			G.vexs[i] = w;
			printf("��ֵ�ɹ���");
			return OK;
		}
	}
	printf("�ýڵ㲻���ڣ�\n");
	return -1;
}

int FirstAdjVex(MGraph G, int k){	//��ͼG��k����ĵ�һ���ڽӶ����λ��
	int i;
	if(k < 0 or k >= G.n){
		printf("�ýڵ㲻���ڣ�");
		return -1;
	}
	for(i = 0; i < G.n; i++){
		if(G.arcs[k][i]){
			return i;
		}
	}
	printf("�ýڵ����ڽӶ��㣡"); 
	return -1;
}

int NextAdjVex(MGraph G, int k, int m){	//m����Ϊk������ڽӶ��㣬��ͼG��k���������m�������һ���ڽӶ����λ��
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
		printf("�ýڵ����ڽӶ��㣡"); 
		return -1;
	}
	printf("��������");
	return -1;
}

Status AddArc(MGraph &G, int k, int m){	//��ͼG������k���㵽m����ı߻�
	if(k < 0 or m < 0 or k >= G.n or m >= G.n){
		printf("�������\n");
		return -1; 
	}
	if(G.arcs[k][m] == 1){
		printf("�ñ��Ѵ��ڣ�\n");
		return -1; 
	}
	G.arcs[k][m] = 1;
	printf("���ӳɹ���\n");
	return OK;
}

Status RemoveArc(MGraph &G, int k, int m){	//��ͼG��ɾ��k���㵽m����ı߻� 
	if(k < 0 or m < 0 or k >= G.n or m >= G.n){
		printf("�������\n");
		return -1; 
	}
	if(G.arcs[k][m] == 0){
		printf("�ñ߲����ڣ�\n");
		return -1; 
	}
	G.arcs[k][m] = 0;
	printf("ɾ���ɹ���\n");
	return OK;
}

void DFS(MGraph G, int k){	//����ͨͼG��k�����������������ȱ��� 
    int j;
    printf("%c ", G.vexs[k]);
    G.tags[k] = 1;
    for(j = 0; j < G.n; j++){
        if(G.arcs[k][j] != 0 and !G.tags[j]){
            DFS(G, j);
        }
    }
}

void DFSTraverse(MGraph G){	//������ȱ���ͼG
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

void BFSTraverse(MGraph G){	//������ȱ���ͼG
	SqQueue Q;
    int i, j, mark;
    char data;
    for(i = 0; i < G.n; i++){
    	G.tags[i] = 0;
	}
    InitQueue(&Q);	//��ʼ������
    for(i = 0; i < G.n; i++){	//��δ���ʵĶ�����BFS
        if(!G.tags[i]){
            G.tags[i] = 1;
            EnQueue(&Q, G.vexs[i]);
            while(!isEmptyQueue(&Q)){
                DeQueue(&Q, &data);  //���׶�����ӣ�����ֵ��data
                printf("%c ", data);
                for(j = 0; j < G.n; j++){	//����ɾ��������±꣬���¸��±�ֵ���Ա���ȷ�ҵ������Ԫ����������������
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
		printf("\t\t\t*           	  ����ͼUDG��������              *\n");
		printf("\t\t\t*                    ��ѡ����                  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.����һ������ͼ     *    2.���Ҷ����λ��  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.���Ҷ����ֵ       *    4.��ֵͼ�Ķ���    *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    5.���Ҷ���ĵ�һ���ڽӶ���                  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    6.���Ҷ���������м䶥�����һ���ڽӶ���    *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    7.����һ����         *    8.ɾ��һ����      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    9.DFS                *    10.BFS            *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    11.����һ��ͼ        *    0.�˳�            *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t                ********************               \n"); 
		printf("\t\t\t                *     ��Ĳ���     *               \n");
		printf("\t\t\t                ********************               \n"); 	
		printf("\t\t\t\t\t\t  ");
		scanf("%d",&op); 
		getchar();
		switch(op){
			case 1: {
				printf("������ڵ�����");
				scanf("%d", &n_1);
				getchar();
				printf("�����������");
				scanf("%d", &e_1);
				getchar();
				if(e_1 > (n_1 * (n_1 - 1) / 2)){
					printf("�������");
				}
				else{
					for(temp_1 = 0; temp_1 < n_1; temp_1++){
						printf("������һ���ڵ㣺");
						scanf("%c", &v_1);
						getchar();
						vexs_1[temp_1] = v_1;
					}
					for(temp_1 = 0; temp_1 < e_1; temp_1++){
						printf("�������������ߵĵ�һ���˵㣺");
						scanf("%c", &arcs_1[temp_1].v);
						getchar();
						printf("�������������ߵĵڶ����˵㣺");
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
				printf("\n������Ҫ����λ��Ķ��㣺");
				scanf("%c", &v_2);
				getchar();
				temp_2 = LocateVex(G, v_2); 
				if(temp_2 != -1){
					printf("�ö����λ��Ϊ��%d\n", temp_2);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 3:	{
				printf("\n������Ҫ���ҵĶ���λ��");
				scanf("%d", &k_3);
				getchar();
				if(GetVex(G, k_3, w_3) != -1){
					printf("�ö����ֵΪ��%c\n", w_3);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 4:	{
				printf("\n������Ҫ��ֵ�Ķ���λ��");
				scanf("%d", &k_4);
				getchar();
				printf("������Ҫ����ֵ��");
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
				printf("\n������Ҫ���ҵĶ���λ��");
				scanf("%d", &k_5);
				getchar();
				temp_5 = FirstAdjVex(G, k_5); 
				if(temp_5 != -1){
					GetVex(G, temp_5, w_5);
					printf("�ö���ĵ�һ���ڽӶ���Ϊ��%c\n", w_5);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 6: {
				printf("\n������Ҫ���ҵĶ���λ��");
				scanf("%d", &k_6);
				getchar();
				printf("�������м䶥���λ��");
				scanf("%d", &m_6);
				getchar();
				temp_6 = NextAdjVex(G, k_6, m_6); 
				if(temp_6 != -1){
					GetVex(G, temp_6, w_6);
					printf("�ö���������м䶥�����һ���ڽӶ���Ϊ��%c\n", w_6);
				}
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 7: {
				printf("\n������Ҫ���ӵıߵ�һ���˵�λ��");
				scanf("%d", &k_7);
				getchar();
				printf("\n������Ҫ���ӵıߵ���һ���˵�λ��");
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
				printf("\n������Ҫɾ���ıߵ�һ���˵�λ��");
				scanf("%d", &k_8);
				getchar();
				printf("\n������Ҫɾ���ıߵ���һ���˵�λ��");
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
				printf("\n��DFS�����������Ϊ��");
				DFSTraverse(G);
				printf("\n\n\n");
				goto begin;
				break;
			}
			case 10: {
				printf("\n��BFS�����������Ϊ��");
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
				printf("\n\n\n��лʹ�ã�");
				exit(0);
				break;
			}
		}
	}
	return 0;
}
