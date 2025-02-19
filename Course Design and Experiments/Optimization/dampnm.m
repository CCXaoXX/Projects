function[x,val,k]=dampnm(fun,gfun,Hess,x0)
%功能:用阻尼牛顿法求解无约束问题: min f(x)
%输入:x0是初始点，fun，gfun，Hess 分别是求
%目标函数值,梯度,Hesse矩阵的函数
%输出: x，va1分别是近似最优点和最优值k是迭代次数
maxk=100;   %给出最大迭代次数
rho=0.55;sigma=0.4;
k=0; epsilon=1e-5;
while(k<maxk)
    gk=feval(gfun,x0);  %计算梯度
    Gk=feval(Hess,x0);  %计算Hesse矩阵
    dk=-Gk\gk;  %解方程组Gk*dk=-gk，计算搜索方向
    if(norm(gk)<epsilon),break;end    %检验终止准则
    m=0;mk=0;
    while(m<20) %用Armijo搜索求步长
        fprintf('m=%d\n', mk)
        if(feval(fun,x0+rho^m*dk)<feval(fun,x0)+sigma*rho^m*gk'*dk)
            mk=m;break;
        end
        m=m+1;
    end
    x0=x0+rho^mk*dk;
    k=k+1;
end
x=x0;
val=feval(fun,x);