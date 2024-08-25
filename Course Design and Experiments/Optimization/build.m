function [A,b]=build(n)
% 构造A，b
A=zeros(n,n);
b=zeros(n,1);
for i=1:n
    b(i)=2;
end
b(1)=3;
b(n)=3;
for i=1:n
    A(i,i)=4;
end
for j=1:n-1
    A(j,j+1)=-1;
end
for j=2:n
    A(j,j-1)=-1;
end