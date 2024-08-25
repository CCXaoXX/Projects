% Hesse矩阵
function He = Hess32(x)
n = length(x);
He = zeros(n ,n);
He = [8, 0;
        0, 2];