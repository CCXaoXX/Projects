b = [1 0 0];
a = [1 -4 8];
sys = tf(b, a);
pzmap(sys);