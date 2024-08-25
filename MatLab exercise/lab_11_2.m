b = [14 0];
a = [1 0 98 0 2401];
sys = tf(b, a);
subplot(211);
pzmap(sys);
subplot(212);
impulse(b, a);
axis([0 20 -20 20]);