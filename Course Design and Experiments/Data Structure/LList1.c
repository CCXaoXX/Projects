//无头结点单链表
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
typedef char ElemType; /* 元素类型为字符类型*/

typedef struct LNode {
	      ElemType data;
	      struct LNode *next;
} LNode, *LList;     /* 不带头结点单链表类型*/

void SetEmpty(LList &L) { /* 置无头结点的空单链表*/
	L = (LNode*)malloc(sizeof(LNode));
	if(L==NULL){
		return FALSE;
	} 
	L->next = NULL;
}
Status Destroy (LList &L) { /* 销毁链表*/
  
}

int Length(LList L) { /* 求表长*/
  
}
Status Get(LList L, int i, ElemType &e) { /* 获取第i元素 */
  
}
int Locate(LList L, ElemType x) { /* 确定x在表中的位序 */
   
}
Status Insert(LList &L, int i, ElemType e) { /* 插入第i元素*/
  
}
Status Delete(LList &L, int i, ElemType &e) { /* 删除第i元素*/
   
}
void Display(LList L) { /* 依次显示表中元素 */

}

void main() { /* 主函数*/

}
