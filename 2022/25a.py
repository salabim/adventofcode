import aocd


def from_snafu(n):
    return sum( {'2':2, '1':1, '0':0, '-':-1, '=': -2}[c] * (5**i) for i, c in enumerate(n[::-1]))
def from_snafu(n):
    return sum( ('=-012'.index(c)-2)* (5**i) for i, c in enumerate(n[::-1]))


def to_snafu(n1):
    return ''.join(['012=-'[n %5] for i in range(100) if ((n:=n1 if i==0 else (n - [0,0,0,-2,-1][n%5]) // 5))>0][::-1])
                    
lines = aocd.get_data(year=2022, day=25).splitlines()
print(to_snafu(sum(from_snafu(line) for line in lines)))
print(to_snafu(sum(sum( {'2':2, '1':1, '0':0, '-':-1, '=': -2}[c] * (5**i) for i, c in enumerate(line[::-1])) for line in lines)))
print(''.join(['012=-'[n % 5] for i in range(1000) if ((n:=sum(sum( ('=-012'.index(c)-2) * (5**i) for i, c in enumerate(line[::-1])) for line in aocd.get_data(year=2022, day=25).splitlines()) if i==0 else (n - [0,0,0,-2,-1][n%5]) // 5))>0][::-1]))
print('2=0-2-1-0=20-01-2-20')
