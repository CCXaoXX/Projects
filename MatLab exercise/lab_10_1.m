syms t
L = laplace((1 + 3 * t + 5 * t^2) * exp(-2 * t));
fprintf('L = %s\n',L);