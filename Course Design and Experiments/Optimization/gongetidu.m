function [error,x]=gongetidu(A,b,e0)
%共轭梯度法求线性方程组
%   'A';系数矩阵
%   'b':右端项
%   'e0':求解精度
%给定初始向量x0和计算精度e0,error代表误差。
n=length(b);
x=zeros(n,1);
r=b-A*x;				%r为误差
d=r;					%d为搜索方向
i=1;
for k=1:500
    alpha=(r'*d)/(d'*A*d);
    x=x+alpha*d;
    r1=b-A*x; 
    error(i)=norm(r1);
    bt=-(r1'*A*d)/(d'*A*d);
    d=r1+bt*d;
    r=r1;
    i=i+1;
    if norm(r1)<=e0
        fprintf('x=\n')
        disp(x)
        fprintf('k=%d', i)
        break;
    end
end