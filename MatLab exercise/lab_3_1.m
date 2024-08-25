t = -10: 0.1: 10;
y = sinc(t) .* cos(10 * pi * t);
plot(t, y);