#include<stdio.h>
#include<windows.h>

int main()
{
    int i,res;//ÿ����i�Σ�ÿres����1��
    printf("������ÿ������Ƶ��\n");
    scanf("%d",&i);
    res=1000/i;//
	printf("���ո�ִ��");
    while(1)
    {
        if(GetAsyncKeyState(VK_SPACE))
        {
            while(1)
            {
                mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,0,0,0,0);
                if(GetAsyncKeyState(VK_ESCAPE))return 0;
                Sleep(res);
            }
        }
    }
    return 0;
}

