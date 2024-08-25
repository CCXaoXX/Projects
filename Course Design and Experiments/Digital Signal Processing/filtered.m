% IIR滤波器设计  
% 目的：设计一个采样频率为1000Hz、通带截止频率为50Hz、阻带截止频率为100Hz的低通滤波器，并要求通带最大衰减为1dB，阻带最小衰减为60dB。  
  
clc;clear;close all;  
  
% 1. 产生信号（频率为10Hz和100Hz的正弦波叠加）  
Fs=1000; % 采样频率1000Hz  
t=0:1/Fs:1;  
s10=sin(20*pi*t); % 产生10Hz正弦波  
s100=sin(200*pi*t); % 产生100Hz正弦波  
s=s10+s100; % 信号叠加  
  
figure(1); % 画图  
subplot(2,1,1);plot(s);grid;  
title('原始信号');  
  
% 2. FFT分析信号频谱  
len = 512;  
y=fft(s,len);  % 对信号做len点FFT变换  
f=Fs*(0:len/2 - 1)/len;  
  
subplot(2,1,2);plot(f,abs(y(1:len/2)));grid;  
title('原始信号频谱')  
xlabel('Hz');ylabel('幅值');  
  
% 3. IIR滤波器设计  
N=0; % 阶数  
Fp=50; % 通带截止频率50Hz  
Fc=100; % 阻带截止频率100Hz  
Rp=1; % 通带波纹最大衰减为1dB  
Rs=60; % 阻带衰减为60dB  
  
% 3.0 计算最小滤波器阶数  
na=sqrt(10^(0.1*Rp)-1);  
ea=sqrt(10^(0.1*Rs)-1);  
N=ceil(log10(ea/na)/log10(Fc/Fp));  
  
% 3.1 巴特沃斯滤波器  
Wn=Fp*2/Fs;  
[Bb Ba]=butter(N,Wn,'low'); % 调用MATLAB butter函数快速设计滤波器  
[BH,BW]=freqz(Bb,Ba); % 绘制频率响应曲线  
Bf=filter(Bb,Ba,s); % 进行低通滤波  
By=fft(Bf,len);  % 对信号f1做len点FFT变换  
  
figure(2); % 画图  
subplot(2,1,1);plot(t,s10,'blue',t,Bf,'red');grid;  
legend('10Hz原始信号','巴特沃斯滤波器滤波后');  
subplot(2,1,2);plot(f,abs(By(1:len/2)));grid;  
title('巴特沃斯低通滤波后信号频谱');  
xlabel('Hz');ylabel('幅值');  