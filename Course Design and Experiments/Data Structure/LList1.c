//��ͷ��㵥����
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <values.h>

#define TRUE   1
#define FALSE  0
#define OK     1
#define ERROR  0
#define NULL  0
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
	L = (LNode*)malloc(sizeof(LNode));
	if(L==NULL){
		return FALSE;
	} 
	L->next = NULL;
}
Status Destroy (LList &L) { /* ��������*/
  
}

int Length(LList L) { /* ���*/
  
}
Status Get(LList L, int i, ElemType &e) { /* ��ȡ��iԪ�� */
  
}
int Locate(LList L, ElemType x) { /* ȷ��x�ڱ��е�λ�� */
   
}
Status Insert(LList &L, int i, ElemType e) { /* �����iԪ��*/
  
}
Status Delete(LList &L, int i, ElemType &e) { /* ɾ����iԪ��*/
   
}
void Display(LList L) { /* ������ʾ����Ԫ�� */

}

void main() { /* ������*/

}
