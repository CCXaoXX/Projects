dt = 0.01; t = -1: dt: 5;
f1 = uCT(t) - uCT(t-2);
f2 = (uCT(t) - uCT(t-3)) + (uCT(t-1) - uCT(t-2));
y = conv(f1, f2) * dt;n = length(y);tt = (0: n-1) * dt - 2;
plot(tt, y);