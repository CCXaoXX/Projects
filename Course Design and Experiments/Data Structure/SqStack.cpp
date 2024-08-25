#include <stdio.h>
#include <stdlib.h>
#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0
#define OVERFLOW 0
typedef int Status;

#define STACK_INIT_SIZE 100
#define STACKINCREMENT 10 
typedef char ElemType;
typedef struct{
   ElemType *elem;     // 存储空间的基址
   int top;    // 栈顶元素的下一个位置，简称栈顶位标
   int size;    // 当前分配的存储容量
   int increment;    // 扩容时，增加的存储容量
} SqStack;

Status InitStack_Sq(SqStack &S, int size, int increment){ // 初始化空的顺序栈S
	S.elem = (ElemType*)malloc(size*sizeof(ElemType));
	if(OVERFLOW == S.elem){
		return OVERFLOW;
	}
	S.top = 0;
	S.size = size;
	S.increment = increment;
	return OK;
}
 
Status StackEmpty_Sq(SqStack &S){//判断栈是否为空，
	if (S.top == OVERFLOW){
      return TRUE;
    }
    return FALSE;
}

Status Push_Sq(SqStack &S, ElemType e) { // 元素e压入栈S
	ElemType *newbase;
	if(S.top >= S.size){
		newbase = (ElemType*)realloc(S.elem, 
		(S.size + S.increment) * sizeof(ElemType));
		if(newbase == OVERFLOW){
			return OVERFLOW;
		}
		S.elem = newbase;
		S.size += S.increment;
	}
	S.elem[S.top++] = e;
	return OK;
}

Status GetTop_Sq(SqStack S, ElemType &e) { // 取栈S的栈顶元素，用e返回
	if (S.top == OVERFLOW){
      return FALSE;
    }
    e = S.elem[S.top];
    return OK;
}

Status Pop_Sq(SqStack &S, ElemType &e) { // 栈S的栈顶元素出栈，并用e返回
	if (S.top == OVERFLOW){
      return FALSE;
    }
    e = S.elem[--S.top];
    return OK;
}

Status DestroyStack_Sq(SqStack &S){// 栈S的销毁
	if (S.top == OVERFLOW){
      return FALSE;
    }
    int i, t;
    for(i = 0;S.elem[i] != OVERFLOW;i++){
      S.elem[i] = 0;
    }
}

void Converstion(int N) {//十进制转换为八进制
	SqStack S;
    ElemType e;
    InitStack_Sq(S, STACK_INIT_SIZE, STACKINCREMENT);
    while(N!=0){
      Push_Sq(S, N % 8);
      N /= 8;
    }
    while(StackEmpty_Sq(S)==FALSE){
      Pop_Sq(S, e);
      printf("%d", e);
    }
}

Status Matching(char *exp, int n) {//括号匹配 
	SqStack S1;
    char a = '0';
    char b = '0';
    int i;
    InitStack_Sq(S1, STACK_INIT_SIZE, STACKINCREMENT);
    for(i = 0;i <= n;i++){
      if(exp[i] == '['||exp[i] == '('||exp[i] == '{'){
          Push_Sq(S1,exp[i]);
          continue;
        }
      if(exp[i] == ']'||exp[i] == ')'||exp[i] == '}'){
          GetTop_Sq(S1,a);
          if(exp[i] == ']' && a=='['){
              Pop_Sq(S1,b);
              printf("\n匹配成功");
              continue;
            }
          if(exp[i] == ')' && a=='('){
              Pop_Sq(S1,b);
              printf("\n匹配成功");
              continue;
            }
          if(exp[i] == '}' && a=='{'){
              Pop_Sq(S1,b);
              printf("\n匹配成功");
              continue;
            }
            printf("\n匹配失败");
          	return FALSE;
      }
    }
	if(StackEmpty_Sq(S1)){
		printf("\n匹配失败");
		return TRUE;
	}
}


int main(){
//定义一个栈，在栈里插入和删除元素，并测试插入和删除后的结果
	SqStack S;
	char e;
	InitStack_Sq(S, STACK_INIT_SIZE, STACKINCREMENT);
	printf("插入元素前：");
	printf("%c \n", S.elem[--S.top]);
	printf("请输入元素：\n");
	scanf("%c", &e); 
	Push_Sq(S, e);
	printf("插入元素后：");
	printf("%c \n", S.elem[--S.top]);
	Pop_Sq(S, e);
	printf("删除元素后：");
	printf("%c \n", S.elem[S.top]);
//测试八进制的转换，并输出结果
	int n;
	printf("请输入一个数：");
	scanf("%d", &n);
	Converstion(n);
//定义一个只含有括号的字符串数组，测试括号是否匹配，并输出结果
	char *s1 = "{]{[]]})(";
	printf("括号为：%s", s1);
	Matching(s1, n);
	return 0;
}
