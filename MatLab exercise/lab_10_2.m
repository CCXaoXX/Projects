syms s
ft = ilaplace(1 / (s^2 * (s^2 + 2 * s + 2)));
fprintf('ft = %s\n',ft);