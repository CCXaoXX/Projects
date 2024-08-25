n=input('Please input n:');				%输入矩阵A的阶数
e0=1e-4;
[A,b]=build(n);						
[error,x]=gongetidu(A,b,e0);       %使用共轭梯度法进行迭代求解
fprintf('\nfx=%f',0.5 * x' * A * x - b' * x)    % 原方程结果
xlabel('迭代次数');
ylabel('log(error)');
q=log(error);
plot(q,'linewidth',1.5)
title('共轭梯度法迭代误差变化曲线');
