#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#define max 40
char name2[max],name3[max],name4[max],name5[max],name6[max];
char number2[5],number3[5],afnumber[5],afnumber2[5];
char phone2[12],phone3[12],phone4[12],afphone[5],afphone2[5];
int flagdate1,flagdate2,flagday1,flagday2,flagcom1=0,flagcom2=0,flagcom3=0,flagcom4=0,flagnum,flaglab,flaglab1;
int flag10,flag11,flag12,flag13,flag14,flag15,flag16,flag21,flag22,flag23,flag24,flag25,flag31,flag32,flag33,flag34,flag35,flag36,flag41,flag42,flag43,flag51;
int sdop,exop,serop,numop,op,op12,op21,op211,op212,op22,op221,op222,op31,op32,op33,swop1,swop2,swop3,swop4;
int num=1,num1=0,i,j,k,fi=0,fi1=0;
int mon,day,lmon,lday;
char ch = 0,re,ser[max],count[max],labor[max];
FILE *fp1,*fp2,*fp3;
time_t t;
struct tm * lt;
struct laboratory{//��history�л�ȡ���� 
	char lab[max];//���ƺ� 
	char number[max];//ѧ�� 
	int lmonth;
	int lday;
	int hour;
	int min;
	int lhour;
	int lmin;
	char uesless[max]; 
	char uesless1[max];
	char uesless2[max];  
}lab[max];
struct labor{//���� 
	char lab[max];
	int count;
}lab1[max];
struct labor1{//��ѯͳ�� 
	char lab[max];
	char number[max];
	int lmonth;
	int lday;
}lab2[max],lab5[max];
struct labor2{ //��ѯͳ�� 
	char number[max];
	char name[max];
	char phone[max];
	int count;
}lab3[max],lab4[max];
struct student{//����ȡ��student��Ϣ0
	char number[11];
	char name[max];
	char phone[12];
	int month;
	int day;
	int hour;
	int min;
	int lmonth;
	int lday;
	int lhour;
	int lmin;
	char lab[max];	
	int count;
}stu[max],stu1[max];
char* Substrend(char*str,int n){//ȡ�ַ�������λ���� 
	char *substr=(char*)malloc(n+1);
	int length=strlen(str);
	if (n>=length){
		strcpy(substr,str);
		return substr;
	}
	int k=0,i;
	for ( i=length-n;i<length;i++){
		substr[k]=str[i];
		k++;
	}
	substr[k]='\0';
	return substr;
}
void begin(){//��ʼ���� 
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*           ��ӭʹ��ʵ���ҳ���ϵͳ1.1            *\n");
	printf("\t\t\t*                  ��ѡ����                    *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    1.ѧ����Ϣ����     *    2.ʵ���ҳ���Ǽ�    *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    3.��ѯ��¼         *    4.ͳ�Ƽ�¼          *\n");
	printf("\t\t\t**************************************************\n");
	printf("\t\t\t*    5.����             *    0.�˳�              *\n");
	printf("\t\t\t**************************************************\n\n");
	printf("\t\t\t               ********************               \n"); 
	printf("\t\t\t               *     ��Ĳ���     *               \n");
	printf("\t\t\t               ********************               \n"); 	
} 
void menu1(){//ѧ����Ϣ���� 
	{
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*                  ѧ����Ϣ����                  *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.����ѧ����Ϣ     *    2.��ѯѧ����Ϣ      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.�޸�ѧ����Ϣ     *    4.ɾ��ѧ����Ϣ      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    5.����             *    0.�˳������˵�      *\n");
		printf("\t\t\t**************************************************\n\n");
		printf("\t\t\t              **********************              \n"); 
		printf("\t\t\t              *      ��Ĳ���      *              \n");
		printf("\t\t\t              **********************              \n");
		printf("\t\t\t              * ������ɺ��мǱ��� *              \n");
		printf("\t\t\t              **********************              \n");
		printf("\t\t\t\t\t\t ");
		scanf("%d",&sdop); 
	}
	switch(sdop){
		case 1:{//����ѧ������ 
			printf("\n***��������Ҫ�����ѧ������***\n");
			scanf("%d",&num);
			for(i = 0;i<num;i++){
				printf("\n***�������%dλѧ����Ϣ***\n",i+1);
				fail111:{
					printf("\nѧ�ţ�");
					scanf("%s",stu1[i].number);
					for(j=0;j<max;j++){
						if(strcmp(stu1[i].number,stu[j].number)==0){
							printf("\n**��ѧ���Ѵ���**\n");
							goto fail111;
						}
					} 
					if(strlen(stu1[i].number)!=10){
						printf("\n**������10λѧ��**\n");
						goto fail111;
					}
				}
				printf("\n������");
				scanf("%s",stu1[i].name);
				fail112:{
					printf("\n�ֻ����룺");
					scanf("%s",stu1[i].phone);		
					if(strlen(stu1[i].phone)!=11){
						printf("\n**������11λ�ֻ���**\n");
						goto fail112;
					}
				}					
				printf("\n***�����%dλѧ����Ϣ�ɹ�***\n",i+1);
			}break;
		}
		case 2:{//��ѯѧ����Ϣ 
			printf("\n***��������Ҫ��ѯѧ��������(1)���ֻ���(2)�Ի��ȫ����Ϣ***\n");
			fail12:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op12); 
				if(op12==1){
					printf("\n������");
					scanf("%s",name2);
					for(i=0;i<max;i++){
						if((strcmp(name2,stu[i].name)==0)){
							printf("\n\t*����Ϊ%s��ѧ����Ϣ*\n",name2);
							printf("ѧ�ţ�%s\t",stu[i].number);
							printf("������%s\t",stu[i].name);
							printf("�ֻ��ţ�%s",stu[i].phone);
							flag11=1;
							break;
						}
					}
					if(flag11!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else if(op12==2){
					fail221:{
						printf("\n�ֻ��ţ�");
						scanf("%s",phone2);
						if(strlen(phone2)!=11){
							printf("\n**������11λ�ֻ���**\n");
							goto fail221;
						}
					}			
					for(i=0;i<max;i++){
						if((strcmp(phone2,stu[i].phone)==0)){
							printf("\n\t�ֻ���Ϊ%s��ѧ����Ϣ\n",phone2);
							printf("ѧ�ţ�%s\t\t",stu[i].number);
							printf("������%s\t",stu[i].name);
							printf("�ֻ��ţ�%s",stu[i].phone);
							flag12=1;
							break; 
						}
					}
					if(flag12!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else{
					printf("\n***���������(1)��(2)***\n");
					goto fail12;
				}break;
			}
		}
		case 3:{//�޸�ѧ����Ϣ 
			printf("\n\n***������ѧ�����������޸�***\n");
			scanf("%s",name3);
			for(i=0;i<max;i++){				
				if((strcmp(name3,stu[i].name)==0)){
					printf("\n\t*����Ϊ%s��ѧ����Ϣ*\n",name3);
					printf("ѧ�ţ�%s\t",stu[i].number);
					printf("������%s\t",stu[i].name);
					printf("�ֻ��ţ�%s",stu[i].phone);
					printf("\n\n**������Ҫ�޸ĵ�ѧ����Ϣ**\n");
					printf("ѧ�ţ�");
					scanf("%s",stu[i].number);
					printf("������");
					scanf("%s",stu[i].name);
					printf("�ֻ��ţ�");
					scanf("%s",stu[i].phone);
					printf("\n\t*�޸ĺ��ѧ����Ϣ*\n");
					printf("ѧ�ţ�%s\t\t",stu[i].number);
					printf("������%s\t",stu[i].name);
					printf("�ֻ��ţ�%s\n",stu[i].phone);
					num++;
					flag13=1;
					break;
				}
			}
			if(flag13!=1){
				printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
			}break;
		}
		case 4:{//ɾ��ѧ����Ϣ 
			printf("\n***��������Ҫɾ����ѧ������***\n");
			scanf("%s",name4);
			for(i=0;i<max;i++){
				if((strcmp(name4,stu[i].name)==0)){
					for (j=i;j<max;j++){
						stu[j] = stu[j+1];
					}
					printf("\n***��Ϣ�����ݿ���ɾ���ɹ�***\n");
					flag14=1;
					break;
				}
			}
			if(flag14!=1){
				printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
			}break;
		}
		case 5:{//����ѧ����Ϣ 
			fp1=fopen("student.txt","w+");
			for (i=0;i<fi+1;i++){
				fprintf(fp1,"%s\t%s\t%s\n",stu[i].number,stu[i].name,stu[i].phone);
				flag15=1;
			}
			fclose(fp1);
			for (i=0;i<num+2;i++){
				fp1=fopen("student.txt","a+");
				fprintf(fp1,"%s\t%s\t%s\n",stu1[i].number,stu1[i].name,stu1[i].phone);
				flag16=1;
				fclose(fp1);
			}
			if(flag16==1&&flag15==1){
				printf("\n***���������ݿ�ɹ�***\n");
			}
			else{
				printf("\n***���������ݿ�ʧ��***\n");
			}
			break;
		}
		case 0:{//�뿪 
			system("cls");
			main();break;
		}
		default:{
			printf("\n*���ڲ���(0-5)��ѡ��*\n");
		} 
	}
		{
			printf("\n\n***�Ƿ�����ڴ˽������(�мǱ���)***\n");		
			printf("�ǣ�1��\n");
			printf("��0��\n");
			fail1:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&swop1);
				if(swop1==1){
					system("cls");
					return menu1();
				}
				else if(swop1==0){
					system("cls");
					main();
				}
				else{
					printf("\n*���ڲ���(0-1)��ѡ��*\n");
					goto fail1;
				}
			}
		}	
}
void menu2(){//ʵ���ҽ����Ǽ� 
	time (&t);
	{
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*                 ʵ���ҳ���Ǽ�                 *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.����Ǽ�         *    2.�뿪�Ǽ�          *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.����             *    0.�˳�              *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*              ����ǼǺ����뿪�Ǽ�              *\n");
		printf("\t\t\t*                 �뿪���мǱ���                 *\n");
		printf("\t\t\t**************************************************\n\n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t               *     ��Ĳ���     *               \n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t\t\t\t ");
		scanf("%d",&exop); 
	}
	switch(exop){
		case 1:{//����Ǽ� 
			printf("\n***������ѧ�ź���λ(1)���ֻ��ź���λ(2)�Խ���Ǽ�***\n");
			fail21:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op21);
				if(op21==1){
					printf("\nѧ�ţ�");
					scanf("%s",number2);
					for(i=0,j=0;i<max;i++){
						strcpy(afnumber,Substrend(stu[i].number,4));
						if((strcmp(number2,afnumber)==0)){
							lt= localtime(&t);
							printf("\n**����������ʵ�������ƺ�**\n");
							scanf("%s",stu[i].lab);
							printf("\n��ѧ������Ϊ%s\n",stu[i].name);
							stu[i].month=lt->tm_mon+1;
							stu[i].day=lt->tm_mday;
							stu[i].hour=lt->tm_hour;
							stu[i].min=lt->tm_min;
							printf("\n��ǰ����ʱ��Ϊ��%d-%d %d:%d\n",stu[i].month,stu[i].day,stu[i].hour,stu[i].min);
							printf("\n*��(1)��(0)�޸�ʱ��*\n");
							printf("\n**��Ĳ���**\n");
							scanf("%d",&op211);
							if(op211==1){
								printf("\n*��Ҫ�޸ĵ�ʱ*\n");
								scanf("%d",&stu[i].hour);
								printf("\n*��Ҫ�޸ĵķ�*\n");
								scanf("%d",&stu[i].min);
								printf("\n�޸ĺ�Ľ���ʱ��Ϊ��%d-%d %d:%d\n",stu[i].month,stu[i].day,stu[i].hour,stu[i].min);
							}											
							flag21=1;
							break;
						}
					}
					if(flag21!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else if(op21==2){
					printf("\n�ֻ��ţ�");
					scanf("%s",&phone3);
					for(i=0,j=0;i<max;i++){
						strcpy(afphone,Substrend(stu[i].phone,4));
						if((strcmp(phone3,afphone)==0)){
							lt= localtime(&t);
							printf("\n**����������ʵ�������ƺ�**\n");
							scanf("%s",stu[i].lab);
							printf("\n��ѧ������Ϊ%s\n",stu[i].name);
							stu[i].month=lt->tm_mon+1;
							stu[i].day=lt->tm_mday;
							stu[i].hour=lt->tm_hour;
							stu[i].min=lt->tm_min;
							printf("\n��ǰ����ʱ��Ϊ��%d-%d %d:%d\n",stu[i].month,stu[i].day,stu[i].hour,stu[i].min);
							printf("\n*��(1)��(0)�޸�ʱ��*\n");
							printf("\n**��Ĳ���**\n");
							scanf("%d",&op212);
							if(op212==1){
								printf("\n*��Ҫ�޸ĵ�ʱ*\n");
								scanf("%d",&stu[i].hour);
								printf("\n*��Ҫ�޸ĵķ�*\n");
								scanf("%d",&stu[i].min);
								printf("\n�޸ĺ�Ľ���ʱ��Ϊ��%d-%d %d:%d\n",stu[i].month,stu[i].day,stu[i].hour,stu[i].min);
							}	
							j++;					
							flag22=1;
							break;
						}
					}
					if(flag22!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else{
						printf("\n***���������(1)��(2)***\n");
						goto fail21;
					}break;		
			}	
			}			
		case 2:{//�뿪�Ǽ� 
			printf("\n***������ѧ�ź���λ(1)���ֻ��ź���λ(2)���뿪�Ǽ�***\n");
			fail22:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op22);
				if(op22==1){
					printf("\nѧ�ţ�");
					scanf("%s",&number3);
					for(i=0;i<max;i++){
						strcpy(afnumber2,Substrend(stu[i].number,4));
						if((strcmp(number3,afnumber2)==0)){
							lt= localtime(&t);
							printf("\n��ѧ������Ϊ%s\n",stu[i].name);
							stu[i].lmonth=lt->tm_mon+1;
							stu[i].lday=lt->tm_mday;
							stu[i].lhour=lt->tm_hour;
							stu[i].lmin=lt->tm_min;
							printf("\n��ǰ�뿪ʱ��Ϊ��%d-%d %d:%d\n",stu[i].lmonth,stu[i].lday,stu[i].lhour,stu[i].lmin);							
							printf("\n*��(1)��(0)�޸�ʱ��*\n");
							printf("\n**��Ĳ���**\n");
							scanf("%d",&op221);
							if(op221==1){
								printf("\n*��Ҫ�޸ĵ�ʱ*\n");
								scanf("%d",&stu[i].lhour);
								printf("\n*��Ҫ�޸ĵķ�*\n");
								scanf("%d",&stu[i].lmin);
								printf("\n�޸ĺ���뿪ʱ��Ϊ��%d-%d %d:%d\n",stu[i].lmonth,stu[i].lday,stu[i].lhour,stu[i].lmin);
							}		
							num1=i;					
							flag23=1;
							break;
						}
					}
					if(flag23!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else if(op22==2){
					printf("\n�ֻ��ţ�");
					scanf("%s",&phone4);
					for(i=0;i<max;i++){
						strcpy(afphone2,Substrend(stu[i].phone,4));
						if((strcmp(phone4,afphone2)==0)){
							lt= localtime(&t);
							printf("\n��ѧ������Ϊ%s\n",stu[i].name);
							stu[i].lmonth=lt->tm_mon+1;
							stu[i].lday=lt->tm_mday;
							stu[i].lhour=lt->tm_hour;
							stu[i].lmin=lt->tm_min;
							printf("\n��ǰ�뿪ʱ��Ϊ��%d-%d %d:%d\n",stu[i].lmonth,stu[i].lday,stu[i].lhour,stu[i].lmin);
							printf("\n*��(1)��(0)�޸�ʱ��*\n");
							printf("\n**��Ĳ���**\n");
							scanf("%d",&op222);
							if(op222==1){
								printf("\n*��Ҫ�޸ĵ�ʱ*\n");
								scanf("%d",&stu[i].lhour);
								printf("\n*��Ҫ�޸ĵķ�*\n");
								scanf("%d",&stu[i].lmin);
								printf("\n�޸ĺ���뿪ʱ��Ϊ��%d-%d %d:%d\n",stu[i].lmonth,stu[i].lday,stu[i].lhour,stu[i].lmin);
							}		
							num1=i;					
							flag24=1;
							break;
						}
					}
					if(flag24!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else{
						printf("\n***���������(1)��(2)***\n");
						goto fail22;
					}break;		
			}
		}		
		case 3:{//���� 
			fp2=fopen("log.txt","a+");
			for (i=0;i<num1+1;i++){
				if(stu[i].lmonth!=0){
					fprintf(fp2,"%s %s %d - %d %d : %d %d : %d\n",stu[i].lab,stu[i].number,stu[i].lmonth,stu[i].lday,stu[i].hour,stu[i].min,stu[i].lhour,stu[i].lmin);
					flag25=1;
				}
			}fclose(fp2);
			if(flag25==1){
				printf("\n***���������ݿ�ɹ�***\n");
			}
			else{
				printf("\n**���ڵǼ��뿪�󱣴�**\n");
			}
			break;
		}
		case 0:{//�뿪 
			system("cls");
			main();break;
		}
		default:{
			printf("\n*���ڲ���(0-3)��ѡ��*\n");
		}		
	}
	{
		printf("\n\n***�Ƿ�����ڴ˽������(�мǱ���)***\n");
		printf("�ǣ�1��\n");
		printf("��0��\n");
		fail2:{
			printf("\n**��Ĳ���**\n");
			scanf("%d",&swop2);
			if(swop2==1){
				system("cls");
				return menu2();
			}
			else if(swop2==0){
				system("cls");
				main();
			}
			else{
				printf("\n*���ڲ���(0-1)��ѡ��*\n");
				goto fail2;
			}
		}
	}
}
void menu3(){//��ѯ��¼ 
	{
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*                      ��ѯ                      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.������Ϣ         *    2.ʵ���ҽ�����¼    *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.���ڲ�ѯ         *    0.�˳�              *\n");
		printf("\t\t\t**************************************************\n\n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t               *     ��Ĳ���     *               \n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t\t\t\t ");
		scanf("%d",&serop);
	} 
	switch(serop){
		case 1:{//��ѯ������Ϣ 
			printf("\n***��������Ҫ��ѯѧ��������(1)���ֻ���(2)�Ի��ȫ����Ϣ***\n");
			fail31:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op31); 
				if(op31==1){
					printf("\n������");
					scanf("%s",name2);
					for(i=0;i<max;i++){
						if((strcmp(name2,stu[i].name)==0)){
							printf("\n\t*����Ϊ%s��ѧ����Ϣ*\n",name2);
							printf("ѧ�ţ�%s\t",stu[i].number);
							printf("������%s\t",stu[i].name);
							printf("�ֻ��ţ�%s",stu[i].phone);
							flag31=1;
							break;
						}
					}
					if(flag31!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else if(op31==2){
					fail311:{
						printf("\n�ֻ��ţ�");
						scanf("%s",phone2);
						if(strlen(phone2)!=11){
							printf("\n**������11λ�ֻ���**\n");
							goto fail311;
						}
					}			
					for(i=0;i<max;i++){
						if((strcmp(phone2,stu[i].phone)==0)){
							printf("\n\t�ֻ���Ϊ%s��ѧ����Ϣ\n",phone2);
							printf("ѧ�ţ�%s\t\t",stu[i].number);
							printf("������%s\t",stu[i].name);
							printf("�ֻ��ţ�%s",stu[i].phone);
							flag32=1;
							break; 
						}
					}
					if(flag32!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else{
					printf("\n***���������(1)��(2)***\n");
					goto fail31;
				}break;
			}
		}
		case 2:{//��ѯʵ���ҽ�����¼ 
			printf("\n***��������Ҫ��ѯѧ��������(1)���ֻ���(2)�Ի��ʵ���ҽ�����¼***\n");
			fail32:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op32); 
				if(op32==1){
					printf("\n������");
					scanf("%s",name2);
					for(i=0;i<max;i++){
						if((strcmp(name2,stu[i].name)==0)){
							printf("\n\t*����Ϊ%s��ѧ������ʵ���Ҽ�¼*\n",name2);
							for(j=0;j<max;j++){
								if(strcmp(stu[i].number,lab[j].number)==0){
									printf("���ƺţ�%s\t",lab[j].lab);
									printf("���ڣ�%d-%d\t",lab[j].lmonth,lab[j].lday);
									printf("����ʱ�䣺%d:%d\t",lab[j].hour,lab[j].min);
									printf("�뿪ʱ�䣺%d:%d\n",lab[j].lhour,lab[j].lmin);
								}		
							}
							flag33=1;
							break;
						}
					}
					if(flag33!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else if(op32==2){
					fail321:{
						printf("\n�ֻ��ţ�");
						scanf("%s",phone2);
						if(strlen(phone2)!=11){
							printf("\n**������11λ�ֻ���**\n");
							goto fail321;
						}
					}			
					for(i=0;i<max;i++){
						if((strcmp(phone2,stu[i].phone)==0)){
							printf("\n\t*�ֻ���Ϊ%s��ѧ������ʵ���Ҽ�¼*\n",phone2);
							for(j=0;j<max;j++){
								if((strcmp(stu[i].number,lab[j].number)==0)){
									printf("���ƺţ�%s\t",lab[j].lab);
									printf("���ڣ�%d-%d\t",lab[j].lmonth,lab[j].lday);
									printf("����ʱ�䣺%d:%d\t",lab[j].hour,lab[j].min);
									printf("�뿪ʱ�䣺%d:%d\n",lab[j].lhour,lab[j].lmin);
								}		
							}
							flag34=1;
							break; 
						}
					}
					if(flag34!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
				}
				else{
					printf("\n***���������(1)��(2)***\n");
					goto fail32;
				}break;
			}
		}
		case 3:{//��ѯһ��ʱ����ʵ���ҽ�����¼ 
			printf("\n***��������Ҫ��ѯѧ��������(1)���ֻ���(2)�Ի��ʵ���ҽ�����¼***\n");
			fail33:{
				printf("\n**��Ĳ���**\n");
				scanf("%d",&op33); 
				if(op33==1){
					printf("\n������");
					scanf("%s",name2);
					for(i=0;i<max;i++){
						if((strcmp(name2,stu[i].name)==0)){
							printf("\n***������Ҫ��ѯ��ʱ���***\n");
							printf("\n**��ʼ����**\n");
							printf("\n*��*\n");
							scanf("%d",&mon);
							printf("*��*\n");
							scanf("%d",&day);
							printf("\n**����ʱ��**\n");
							printf("\n*��*\n");
							scanf("%d",&lmon);
							printf("*��*\n");
							scanf("%d",&lday);
							if(mon==lmon){
								if(day>=lday||day>lday){
									printf("\n**��������ȷ������**\n");
									flagcom1=1;
									flagdate1=1;
								}
							}
							if(mon>lmon){
								printf("\n**��������ȷ������**\n");
								flagcom1=1;
								flagdate1=1;
							}
							for(j=0;j<max;j++){
								if((strcmp(stu[i].number,lab[j].number)==0)&&mon<=lab[j].lmonth&&lmon>=lab[j].lmonth&&flagcom1!=1){
									if(day<=lab[j].lday&&lday>=lab[j].lday||day==lab[j].lday&&lday==lab[j].lday){
										printf("\n\t*����Ϊ%s��ѧ���ڸ�ʱ����ڽ���ʵ���Ҽ�¼*\n",name2);
									}break;
								}
							}
							for(j=0;j<max;j++){
								if((strcmp(stu[i].number,lab[j].number)==0)&&mon<=lab[j].lmonth&&lmon>=lab[j].lmonth&&flagcom1!=1){
									if(day<=lab[j].lday&&lday>=lab[j].lday||day==lab[j].lday&&lday==lab[j].lday){
										printf("���ƺţ�%s\t",lab[j].lab);
										printf("���ڣ�%d-%d\t",lab[j].lmonth,lab[j].lday);
										printf("����ʱ�䣺%d:%d\t",lab[j].hour,lab[j].min);
										printf("�뿪ʱ�䣺%d:%d\n",lab[j].lhour,lab[j].lmin);
										flagday1=1; 
									}	
								}		
							}
							flag35=1;
							break;
						}
					}
					if(flag35!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
					if(flagdate1!=1&&flagday1!=1){
						printf("\n**��ѧ���ڴ�ʱ������޽���ʵ���Ҽ�¼**\n");
					}
				}
				else if(op33==2){
					fail331:{
						printf("\n�ֻ��ţ�");
						scanf("%s",phone2);
						if(strlen(phone2)!=11){
							printf("\n**������11λ�ֻ���**\n");
							goto fail331;
						}
					}			
					for(i=0;i<max;i++){
						printf("\n***������Ҫ��ѯ��ʱ���***\n");
						printf("\n**��ʼ����**\n");
						printf("\n*��*\n");
						scanf("%d",&mon);
						printf("*��*\n");
						scanf("%d",&day);
						printf("\n**����ʱ��**\n");
						printf("\n*��*\n");
						scanf("%d",&lmon);
						printf("*��*\n");
						scanf("%d",&lday);
						if(mon==lmon){
							if(day>=lday){
								printf("\n**�������뿪���ڲ�����ͬ**\n");
								flagcom2=1;
								flagdate2=1;
							}
						}
						if(mon>lmon){
							printf("\n**��������ȷ������**\n");
							flagcom2=1;
							flagdate2=1;
						}
						for(j=0;j<max;j++){
							if((strcmp(stu[i].number,lab[j].number)==0)&&mon<=lab[j].lmonth&&lmon>=lab[j].lmonth&&flagcom2!=1){
								if(day<=lab[j].lday&&lday>=lab[j].lday||day==lab[j].lday&&lday==lab[j].lday){
									printf("\n\t*�ֻ���Ϊ%s��ѧ���ڸ�ʱ����ڽ���ʵ���Ҽ�¼*\n",phone2);
								}break;
							}
						}
						for(j=0;j<max;j++){
							if((strcmp(stu[i].number,lab[j].number)==0)&&mon<=lab[j].lmonth&&lmon>=lab[j].lmonth&&flagcom2!=1){
								if(day<=lab[j].lday&&lday>=lab[j].lday||day==lab[j].lday&&lday==lab[j].lday){
									printf("���ƺţ�%s\t",lab[j].lab);
									printf("���ڣ�%d-%d\t",lab[j].lmonth,lab[j].lday);
									printf("����ʱ�䣺%d:%d\t",lab[j].hour,lab[j].min);
									printf("�뿪ʱ�䣺%d:%d\n",lab[j].lhour,lab[j].lmin);
									flagday2=1;
								}	
							}		
						}
						flag36=1;
						break; 
					}
					if(flag36!=1){
						printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
					}
					if(flagdate2!=1&&flagday2!=1){
						printf("\n**��ѧ���ڴ�ʱ������޽���ʵ���Ҽ�¼**\n");
					}
				}
				else{
					printf("\n***���������(1)��(2)***\n");
					goto fail33;
				}	
			}
			break;
		}
		case 0:{//�뿪 
			system("cls");
			main();break;
		}
		default:{
			printf("\n*���ڲ���(0-3)��ѡ��*\n");
		}
	}
	{
		printf("\n\n***�Ƿ�����ڴ˽������***\n");
		printf("�ǣ�1��\n");
		printf("��0��\n");
		fail3:{
			printf("\n**��Ĳ���**\n");
			scanf("%d",&swop3);
			if(swop3==1){
				system("cls");
				return menu3();
			}
			else if(swop3==0){
				system("cls");
				main();
			}
			else{
				printf("\n*���ڲ���(0-1)��ѡ��*\n");
				goto fail3;
			}
		}
	}
}
void menu4(){ //ͳ�Ƽ�¼ 
	{
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*                      ͳ��                      *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    1.����ͳ��         *    2.���ƺ�ͳ��        *\n");
		printf("\t\t\t**************************************************\n");
		printf("\t\t\t*    3.ʱ��ͳ��         *    0.�˳�              *\n");
		printf("\t\t\t**************************************************\n\n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t               *     ��Ĳ���     *               \n");
		printf("\t\t\t               ********************               \n"); 
		printf("\t\t\t\t\t\t ");
		scanf("%d",&numop); 
	}
	switch(numop){
		case 1:{//����ʵ���Ҵ��� 
			printf("\n***������Ҫͳ�Ƶ�����***\n");
			scanf("%s",name2);
			for(i=0;i<max;i++){
				if(strcmp(name2,stu[i].name)==0){
					for(j=0,k=0;j<max;j++){
						if(strcmp(stu[i].number,lab[j].number)==0){
							strcpy(lab1[k].lab,lab[j].lab);
							k++;
							flagnum=1;
						}		
					}
					flag41=1;
					break;
				}
			}
			for(i=0;i<k;i++){
				lab1[i].count=0;
			}
			for(i=0;i<k;i++){
				for(j=i;j<k;j++){
					if(strcmp(lab1[i].lab,lab1[j].lab)==0){
						lab1[i].count++;
					}
				}
			}
			for(i=1;i<k;i++){
				for(j=0;j<i;j++){
					if(strcmp(lab1[i].lab,lab1[j].lab)==0){
						lab1[i].count=0;
						break;
					}
				}
			}
			if(flag41==1&flagnum==1){
				printf("\n\t**��ѧ����������ʵ���ҵļ�¼Ϊ**\n");
			}
			for(i=0;i<k;i++){
				if(lab1[i].count!=0){
					printf("���ƺţ�%s\t",lab1[i].lab);
					printf("������%d\n",lab1[i].count);
				}
			}
			if(flag41!=1){
				printf("\n**���ݿ������޴�ѧ����Ϣ**\n");
			}
			if(flagnum!=1&&flag41==1){
				printf("\n***��ѧ�����޽���ʵ���Ҽ�¼***\n");
			}
			break;
		}			
		case 2:{//����ʵ�������� 
			printf("\n***������Ҫͳ�Ƶ�ʵ�������ƺ�***\n");
			scanf("%s",labor);
			for(i=0,j=0;i<max;i++){
				if(strcmp(labor,lab[i].lab)==0){
					strcpy(lab2[j].lab,lab[i].lab);
					strcpy(lab2[j].number,lab[i].number);
					lab2[j].lmonth=lab[i].lmonth;
					lab2[j].lday=lab[i].lday;
					j++;
					flaglab=1;
				}
			} 
			if(flaglab!=1){
				printf("\n**���޸�ʵ������Ϣ**\n");
			}
			for(i=0;i<max;i++){
				stu[i].count=0;
			}
			for(i=0;i<max;i++){
				for(k=0;k<j;k++){
					if(strcmp(stu[i].number,lab2[k].number)==0){
						stu[i].count++;
					}	
				}
			}
			if(flaglab==1){
				printf("\n\t**��ʵ��������ѧ������ʱ��������**\n");
				for(i=0;i<fi;i++){
					printf("ѧ�ţ�%s\t",stu[i].number);
					printf("������%s\t",stu[i].name);
					printf("�ֻ��ţ�%s\t",stu[i].phone);
					printf("��ʵ���ҽ��������%d��\n",stu[i].count);	
				}
			}
			break;
		}
		case 3:{//ʵ���ҿ��� 
			printf("\n***������Ҫ��ѯ��ʱ���***\n");
			printf("\n**��ʼ����**\n");
			printf("\n*��*\n");
			scanf("%d",&mon);
			printf("*��*\n");
			scanf("%d",&day);
			printf("\n**����ʱ��**\n");
			printf("\n*��*\n");
			scanf("%d",&lmon);
			printf("*��*\n");
			scanf("%d",&lday);
			if(mon==lmon){
				if(day>=lday){
					printf("\n**��������ȷ������**\n");
					flagcom4=1; 
				}
			}
			if(mon>lmon){
				printf("\n**��������ȷ������**\n");
				flagcom4=1; 
			}
			if(flagcom4!=1){
				printf("\n***������Ҫͳ�Ƶ�ʵ�������ƺ�***\n");
				scanf("%s",labor);
				for(i=0,j=0;i<max;i++){
					if(strcmp(labor,lab[i].lab)==0&&mon<=lab[i].lmonth&&lmon>=lab[i].lmonth){
						if(day<=lab[i].lday&&lday>=lab[i].lday||day==lab[i].lday&&lday==lab[i].lday){
							strcpy(lab5[j].lab,lab[i].lab);
							strcpy(lab5[j].number,lab[i].number);
							lab5[j].lmonth=lab[i].lmonth;
							lab5[j].lday=lab[i].lday;
							j++;
							flaglab1=1;
						}
					}
				}
				if(flaglab1!=1){
					printf("\n**������Ϣ**\n");
				}
				if(flaglab1==1){
					for(i=0;i<max;i++){
						stu[i].count=0;
					}
					for(i=0;i<max;i++){
						for(k=0;k<j;k++){
							if(strcmp(stu[i].number,lab5[k].number)==0){
								stu[i].count++;
							}	
						}
					}
					for(j=0,k=0;j<fi;j++){
						strcpy(lab4[k].name,stu[j].name);
						strcpy(lab4[k].number,stu[j].number);
						strcpy(lab4[k].phone,stu[j].phone);
						lab4[k].count=stu[j].count;
						k++;
					}
					for(j=0;j<fi;j++){
						for(i=0;i<fi-j;i++){
							if(lab4[i].count<lab4[i+1].count){
								lab3[i]=lab4[i];
								lab4[i]=lab4[i+1];
								lab4[i+1]=lab3[i];
							}
						}
					}
					printf("\n\t**��ʱ����ڴ�ʵ��������ѧ����������**\n");
					for(i=0;i<fi;i++){
						printf("ѧ�ţ�%s\t",lab4[i].number);
						printf("������%s\t",lab4[i].name);
						printf("�ֻ��ţ�%s\t",lab4[i].phone);
						printf("��ʵ���ҽ���������%d��\n",lab4[i].count);	
					}
				}
			}
			break;
		}			
		case 0:{//�뿪 
			system("cls");
			main();break;
		}		
		default:{
			printf("\n*���ڲ���(0-3)��ѡ��*\n");
		}		
	}
	{
		printf("\n\n***�Ƿ�����ڴ˽������***\n");
		printf("�ǣ�1��\n");
		printf("��0��\n");
		fail4:{
			printf("\n**��Ĳ���**\n");
			scanf("%d",&swop4);
			if(swop4==1){
				system("cls");
				return menu4();
			}
			else if(swop4==0){
				system("cls");
				main();
			}
			else{
				printf("\n*���ڲ���(0-1)��ѡ��*\n");
				goto fail4;
			}
		}
	}
}
void moveDate(){//���� 
	fp2=fopen("log.txt","r+");
	fp3=fopen("history.txt","a+");
	ch=getc(fp2);
	while (!feof(fp2)){
		putc(ch,fp3);
		ch=fgetc(fp2);
		flag51=1;
	}
	fclose(fp2);
	fclose(fp3);
	fp2=fopen("log.txt","w+");
	fclose(fp2);
	if(flag51==1){
		printf("\n***�ļ����ݳɹ�***\n\n");
	}
	else{
		printf("\n***�ļ�����ʧ��***\n\n");
	}
	printf("\n***����������Է���***\n");
	scanf("%s",&re);
	system("cls");
	main();
}
int main(){//������ 
	fp1=fopen("student.txt","a+");
	while(fscanf(fp1,"%s%s%s",stu[fi].number,stu[fi].name,stu[fi].phone)!=EOF){
        fi++;
	}fclose(fp1);
	fp2=fopen("history.txt","a+");
	while(fscanf(fp2,"%s%s%d%s%d%d%s%d%d%s%d",lab[fi1].lab,lab[fi1].number,&lab[fi1].lmonth,lab[fi1].uesless,&lab[fi1].lday,&lab[fi1].hour,lab[fi].uesless1,&lab[fi1].min,&lab[fi1].lhour,lab[fi1].uesless2,&lab[fi1].lmin)!=EOF){
		fi1++;
	}fclose(fp2);
	begin();
	printf("\t\t\t\t\t\t ");
	scanf("%d",&op); 
	printf("------------------------------------------------------------------------------------------------------------------------\n"); 
	switch(op){
		case 1: menu1();	break; 
		case 2:	menu2();	break;
		case 3:	menu3();	break;
		case 4:	menu4();	break; 
		case 5:	moveDate();	break; 
		case 0:	exit(0);
		default:	
			system("cls");
			main();	
	}
	return 0; 
} 
