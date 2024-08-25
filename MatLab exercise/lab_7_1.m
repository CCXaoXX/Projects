ft=str2sym('sin(pi*t)/(pi*t)');
Fw=simplify(fourier(ft));
subplot(211)
fplot(abs(Fw)),grid on
title('幅度谱')
phase=atan(imag(Fw)/real(Fw));
subplot(212)
fplot(phase),grid on
title('相位谱')