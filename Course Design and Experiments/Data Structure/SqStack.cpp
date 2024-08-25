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
   ElemType *elem;     // �洢�ռ�Ļ�ַ
   int top;    // ջ��Ԫ�ص���һ��λ�ã����ջ��λ��
   int size;    // ��ǰ����Ĵ洢����
   int increment;    // ����ʱ�����ӵĴ洢����
} SqStack;

Status InitStack_Sq(SqStack &S, int size, int increment){ // ��ʼ���յ�˳��ջS
	S.elem = (ElemType*)malloc(size*sizeof(ElemType));
	if(OVERFLOW == S.elem){
		return OVERFLOW;
	}
	S.top = 0;
	S.size = size;
	S.increment = increment;
	return OK;
}
 
Status StackEmpty_Sq(SqStack &S){//�ж�ջ�Ƿ�Ϊ�գ�
	if (S.top == OVERFLOW){
      return TRUE;
    }
    return FALSE;
}

Status Push_Sq(SqStack &S, ElemType e) { // Ԫ��eѹ��ջS
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

Status GetTop_Sq(SqStack S, ElemType &e) { // ȡջS��ջ��Ԫ�أ���e����
	if (S.top == OVERFLOW){
      return FALSE;
    }
    e = S.elem[S.top];
    return OK;
}

Status Pop_Sq(SqStack &S, ElemType &e) { // ջS��ջ��Ԫ�س�ջ������e����
	if (S.top == OVERFLOW){
      return FALSE;
    }
    e = S.elem[--S.top];
    return OK;
}

Status DestroyStack_Sq(SqStack &S){// ջS������
	if (S.top == OVERFLOW){
      return FALSE;
    }
    int i, t;
    for(i = 0;S.elem[i] != OVERFLOW;i++){
      S.elem[i] = 0;
    }
}

void Converstion(int N) {//ʮ����ת��Ϊ�˽���
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

Status Matching(char *exp, int n) {//����ƥ�� 
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
              printf("\nƥ��ɹ�");
              continue;
            }
          if(exp[i] == ')' && a=='('){
              Pop_Sq(S1,b);
              printf("\nƥ��ɹ�");
              continue;
            }
          if(exp[i] == '}' && a=='{'){
              Pop_Sq(S1,b);
              printf("\nƥ��ɹ�");
              continue;
            }
            printf("\nƥ��ʧ��");
          	return FALSE;
      }
    }
	if(StackEmpty_Sq(S1)){
		printf("\nƥ��ʧ��");
		return TRUE;
	}
}


int main(){
//����һ��ջ����ջ������ɾ��Ԫ�أ������Բ����ɾ����Ľ��
	SqStack S;
	char e;
	InitStack_Sq(S, STACK_INIT_SIZE, STACKINCREMENT);
	printf("����Ԫ��ǰ��");
	printf("%c \n", S.elem[--S.top]);
	printf("������Ԫ�أ�\n");
	scanf("%c", &e); 
	Push_Sq(S, e);
	printf("����Ԫ�غ�");
	printf("%c \n", S.elem[--S.top]);
	Pop_Sq(S, e);
	printf("ɾ��Ԫ�غ�");
	printf("%c \n", S.elem[S.top]);
//���԰˽��Ƶ�ת������������
	int n;
	printf("������һ������");
	scanf("%d", &n);
	Converstion(n);
//����һ��ֻ�������ŵ��ַ������飬���������Ƿ�ƥ�䣬��������
	char *s1 = "{]{[]]})(";
	printf("����Ϊ��%s", s1);
	Matching(s1, n);
	return 0;
}
