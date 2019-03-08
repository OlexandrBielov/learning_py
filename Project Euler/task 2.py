def nextfibnum():
    global prelastnum
    a1 = prelastnum;
    global lastnum
    prelastnum = lastnum;
    lastnum = prelastnum + a1;

prelastnum = 1
lastnum = 2
sum = 0

while lastnum < 4000000:
    if lastnum%2==0:
        sum += lastnum
    nextfibnum()
print(sum)