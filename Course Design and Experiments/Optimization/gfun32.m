% 梯度
function g = gfun32(x)
g = [8 * x(1) - 8, 2 * x(2) - 4]';