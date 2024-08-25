t = 0:0.001:8;
sys = tf([1,0], [1,2,2]);
h = impulse(sys, t);
g = step(sys, t);
subplot(211);
plot(t, h);
title('冲激响应');
subplot(212);
plot(t, g);
title('阶跃响应')