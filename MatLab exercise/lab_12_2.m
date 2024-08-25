n = 0:25;
x = (5 / 6).^n .* sin((n .* pi) / 5);
stem(n, x, 'fill');