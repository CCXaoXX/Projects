% Hesse矩阵
function He = Hess(x)
n = length(x);
He = zeros(n ,n);
He = [48 * x(1)^2 - 16 * x(2) + 6, -16 * x(1);
        -16 * x(1), 8];