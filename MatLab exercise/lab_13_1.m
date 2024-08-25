a = [3 4 1];
b = [1 1];
n = -5:10;
x = impDT(n);
y = filter(b, a, x);
stem(n ,y, 'fill');