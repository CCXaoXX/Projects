ts = 0; te = 8; dt = 0.001;
sys = tf([1,3],[1,4,4]);
t = ts:dt:te;
f = exp(-t) .* uCT(t);
y = lsim(sys, f, t);
plot(t, y);