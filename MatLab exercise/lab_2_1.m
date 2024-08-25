t = -1:0.01:5;
ft_1 = (t >= 0);
ft_2 = (t >= 2);
y = (1 + cos(pi * t)) .* (ft_1 - ft_2);
plot(t, y);
