t = 0: 0.01: 3;
ft = 2 * exp(j * (t + pi / 4));
subplot(2, 2, 1);plot(t, real(ft));title('实部');
subplot(2, 2, 2);plot(t, imag(ft));title('虚部');
subplot(2, 2, 3);plot(t, abs(ft));title('模');axis([0,3,0,2]);
subplot(2, 2, 4);plot(t, angle(ft));title('辐角');