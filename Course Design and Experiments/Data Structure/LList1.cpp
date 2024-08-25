//��ͷ��㵥����
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define TRUE   1
#define FALSE  0
#define OK     1
#define ERROR  0
#define IBFEASIBLE  -1
#define OVERFLOW    -2 

#define MAXLEN  20
#define MAXSIZE 20

typedef int Status;
typedef char ElemType; /* Ԫ������Ϊ�ַ�����*/

typedef struct LNode {
	      ElemType data;
	      struct LNode *next;
} LNode, *LList;     /* ����ͷ��㵥��������*/
void SetEmpty(LList &L) { /* ����ͷ���Ŀյ�����*/
	L = NULL;
}
Status Destroy(LList &L) { /* ��������*/
	L = NULL;
	free(L);
	printf("\n���ٳɹ�\n"); 
	return TRUE;
}
int Length(LList L) { /* ���*/
	int length = 0;
	LNode *p = L;
	while(p!=NULL){
		p = p->next;
		length++;
	}
	return length;
}
Status Get(LList L, int i, ElemType &e) { /* ��ȡ��iԪ�� */
	if(Length(L) < i){
		printf("�������\n"); 
		return ERROR;
	}
	int j = 1;
	LNode *p = L->next;
	if(i == 0) return L->data;
	if(i < 1){
		return ERROR;
	}
    while(j < i and p != NULL){
    	p = p->next;
    	j++;
	}
	e = p->data;
	printf("��Ԫ��Ϊ��%c", e);
	return TRUE;
}
int Locate(LList L, ElemType x) { /* ȷ��x�ڱ��е�λ�� */
	int j = 0;
	LNode *p = L;
    while(p != NULL and p->data != x){
    	p = p->next;
    	j++;
	}
	printf("��Ԫ��λ��Ϊ��%d", j);
	if(Length(L) < j){
		printf("�������\n"); 
		return ERROR;
	}
	return TRUE;
}
Status Insert(LList &L, int i, ElemType e) { /* �����iԪ��*/
	if(i < 1) return ERROR;  
	if(i==1){
		LNode *s = (LNode *)malloc(sizeof(LNode));
		s->data = e;
		s->next = L;
		L = s;
		return TRUE;
	}
	LNode *p;
    p = L;
    int j = 1;
    while(p !=NULL and j < i - 1){
      p = p->next;
      j++;
    }
    if(p==NULL){
    	return FALSE;
	}
	LNode *s = (LNode *)malloc(sizeof(LNode));
	s->data = e;
	s->next = p->next;
	p->next = s;
	return TRUE;
}
Status Delete(LList &L, int i, ElemType &e) { /* ɾ����iԪ��*/
	if(Length(L) < i){
		printf("�������"); 
		return ERROR;
	}
	if(i < 1) return ERROR;  
	if(i==1){
		e = L->data;
		L = L->next;
		return TRUE;
	}
	LNode *p;
    p = L;
    int j = 1;
    while(p !=NULL and j < i - 1){
      p = p->next;
      j++;
    }
    if(p==NULL){
    	return FALSE;
	}
	LNode *q = p->next;
	e = q->data;
	p->next = q->next;
	free(q);
	return TRUE;
}
void Display(LList L) { /* ������ʾ����Ԫ�� */
	LNode *p = L;
	while(p != NULL){
		printf("%c\n",p->data);
		p = p->next;
	}
}

int main() { /* ������*/
	LList L;
	int i;
	ElemType e, x; 
	SetEmpty(L);
	printf("��ʼ����ı���");
	printf("%d", Length(L));
	Insert(L, 1, 'a');
	Insert(L, 2, 'b');
	Insert(L, 3, 'c');
	printf("\n�����ֵ���������Ϊ��\n");
	Display(L);
	printf("\n��Ϊ��");
	printf("%d", Length(L));

	printf("\n���������ĵ�iλԪ�أ�");
	scanf("%d",&i);
	getchar(); 
	printf("����ֵΪ��");
	scanf("%c",&e);
	Insert(L, i, e);
	printf("����������Ϊ��\n");
	Display(L); 
	printf("�����ı�Ϊ��\n");
	printf("%d", Length(L));
	
	printf("\n������ɾ���ĵ�iλԪ�أ�");
	scanf("%d",&i);
	getchar(); 
	Delete(L, i, e);
	printf("ɾ����ı�Ϊ��\n");
	Display(L); 
	printf("ɾ����Ԫ��Ϊ��%c\n", e); 
	
	printf("\n������Ҫ���ҵ�λ�Σ�");
	scanf("%d",&i);
	getchar(); 
	Get(L, i, e);
	
	printf("\n������Ҫ���ҵ�Ԫ�أ�");
	scanf("%c",&x);
	getchar(); 
	Locate(L, x);
	
	printf("\n���ٱ�\n");
	Destroy(L);
	printf("���ٺ�Ϊ��");
	Display(L);
	printf("��Ϊ��");
	printf("%d", Length(L));
	return 0;
}
