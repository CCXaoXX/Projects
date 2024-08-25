% a = 0
b=[1];
a1=[1 0 1];
sys1=tf(b,a1);
subplot(421);
pzmap(sys1);
% a = 1/4
a2=[1 0.5 1];
sys2=tf(b,a2);
subplot(423);
pzmap(sys2);
w = -8 * pi:0.01:8 * pi;
H2 = freqs(b,a2,w);
subplot(424);
plot(w,abs(H2)),grid on;
xlabel('\omega(rad/s)'),ylabel('|H(\omega)|');
axis([-5 5 0 2.5]);
title('a=1/4 时的幅频特性');
% a = 1
a3=[1 2 1];
sys3=tf(b,a3);
subplot(425);
pzmap(sys3);
H3=freqs(b,a3,w);
subplot(426)
plot(w,abs(H3)),grid on;
axis([-5 5 0 2.5]);
xlabel('\omega(rad/s)'),ylabel('|H(\omega)|');
title('a=1 时的幅频特性');
% a = 2
a4=[1 4 1];
sys4=tf(b,a4);
subplot(427);
pzmap(sys4);
H4=freqs(b,a4,w); 
subplot(428);
plot(w,abs(H4)),grid on;
axis([-5 5 0 2.5]);
xlabel('\omega(rad/s)'),ylabel('|H(\omega)|');
title('a=2 时的幅频特性');