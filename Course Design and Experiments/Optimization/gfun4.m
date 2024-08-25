% 梯度
function g = gfun4(x)
g = [4 * x(1) - 2 * x(2), 2 * x(2) - 2 * x(1) - 2]';