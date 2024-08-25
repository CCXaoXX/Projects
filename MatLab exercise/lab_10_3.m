syms s;
f = ilaplace((4 * s^2 + 4 * s + 4) / (s^4 + 3 * s^3 + 2 * s^2));
fprintf('f = (%s) * u(t)\n',f);