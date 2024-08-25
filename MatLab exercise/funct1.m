function f = funct1(t)
f = (t+1).*(uCT(t+2)-uCT(t+1))+1.*(uCT(t+1)-uCT(t))+2.*(uCT(t)-uCT(t-1))+(2-t).*(uCT(t-1)-uCT(t-2))