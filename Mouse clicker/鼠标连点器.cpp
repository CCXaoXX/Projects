#include<stdio.h>
#include<windows.h>

int main()
{
    int i,res;//每秒点击i次，每res秒点击1次
    printf("请输入每秒点击的频率\n");
    scanf("%d",&i);
    res=1000/i;//
	printf("按空格执行");
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

