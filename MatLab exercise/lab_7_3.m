dt=0.01;
t=-2:dt:2;
ft=(t+2).*(uCT(t+2)-uCT(t+1))+uCT(t+1)-uCT(t-1)+(t-2).*(uCT(t-2)-uCT(t-1));
n=2000;
k=-n:n;
w=pi*k/(n*dt);
f=dt*ft*exp(-1j*t'*w);
f=abs(f);
plot(w,f),grid on
axis([-10 10 -1 4])
title('幅度谱');