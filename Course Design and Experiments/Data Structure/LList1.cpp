//无头结点单链表
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
typedef char ElemType; /* 元素类型为字符类型*/

typedef struct LNode {
	      ElemType data;
	      struct LNode *next;
} LNode, *LList;     /* 不带头结点单链表类型*/
void SetEmpty(LList &L) { /* 置无头结点的空单链表*/
	L = NULL;
}
Status Destroy(LList &L) { /* 销毁链表*/
	L = NULL;
	free(L);
	printf("\n销毁成功\n"); 
	return TRUE;
}
int Length(LList L) { /* 求表长*/
	int length = 0;
	LNode *p = L;
	while(p!=NULL){
		p = p->next;
		length++;
	}
	return length;
}
Status Get(LList L, int i, ElemType &e) { /* 获取第i元素 */
	if(Length(L) < i){
		printf("输入错误\n"); 
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
	printf("该元素为：%c", e);
	return TRUE;
}
int Locate(LList L, ElemType x) { /* 确定x在表中的位序 */
	int j = 0;
	LNode *p = L;
    while(p != NULL and p->data != x){
    	p = p->next;
    	j++;
	}
	printf("该元素位置为：%d", j);
	if(Length(L) < j){
		printf("输入错误\n"); 
		return ERROR;
	}
	return TRUE;
}
Status Insert(LList &L, int i, ElemType e) { /* 插入第i元素*/
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
Status Delete(LList &L, int i, ElemType &e) { /* 删除第i元素*/
	if(Length(L) < i){
		printf("输入错误"); 
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
void Display(LList L) { /* 依次显示表中元素 */
	LNode *p = L;
	while(p != NULL){
		printf("%c\n",p->data);
		p = p->next;
	}
}

int main() { /* 主函数*/
	LList L;
	int i;
	ElemType e, x; 
	SetEmpty(L);
	printf("初始化后的表长：");
	printf("%d", Length(L));
	Insert(L, 1, 'a');
	Insert(L, 2, 'b');
	Insert(L, 3, 'c');
	printf("\n随机赋值过后的链表为：\n");
	Display(L);
	printf("\n表长为：");
	printf("%d", Length(L));

	printf("\n请输入插入的第i位元素：");
	scanf("%d",&i);
	getchar(); 
	printf("它的值为：");
	scanf("%c",&e);
	Insert(L, i, e);
	printf("插入后的链表为：\n");
	Display(L); 
	printf("插入后的表长为：\n");
	printf("%d", Length(L));
	
	printf("\n请输入删除的第i位元素：");
	scanf("%d",&i);
	getchar(); 
	Delete(L, i, e);
	printf("删除后的表为：\n");
	Display(L); 
	printf("删除的元素为：%c\n", e); 
	
	printf("\n请输入要查找的位次：");
	scanf("%d",&i);
	getchar(); 
	Get(L, i, e);
	
	printf("\n请输入要查找的元素：");
	scanf("%c",&x);
	getchar(); 
	Locate(L, x);
	
	printf("\n销毁表\n");
	Destroy(L);
	printf("销毁后为：");
	Display(L);
	printf("表长为：");
	printf("%d", Length(L));
	return 0;
}
