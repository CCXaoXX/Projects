syms t;
Fw = str2sym('exp(-4*w^2)');
ft = ifourier(Fw,t);
ezplot(ft);