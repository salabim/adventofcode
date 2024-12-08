import aocd
from collections import defaultdict
from pprint import pprint

lines='''\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.splitlines()

#lines = aocd.get_data(year=2023, day=5).splitlines()
t=''
maps=[]
for line in lines:
    if t=='':
        t=line
        if line[:6]=='seeds:':
            seeds=list(map(int,line[6:].split()))
            print(seeds)
        else:
            maps.append([])
    else:
        if line=='':
            t=''
        else:
            maps[-1].append(list(map(int,line.split())))

result=1e30
for seed in seeds:
    for i in range(len(maps)):
        for xlate in maps[i]:
            dest,source,length=xlate
            if source <= seed <source+length:
                seed+=(dest-source)
                break
    result=min(result,seed)
    
print('part 1=',result)
#323142486
result=1e30
for start,n in zip(seeds[::2], seeds[1::2]):
    print('...')
    for seed in range(start,start+n):
        for i in range(len(maps)):
            for xlate in maps[i]:
                dest,source,length=xlate
                if source <= seed <source+length:
                    seed+=(dest-source)
                    break
        result=min(result,seed)        
print('part 2=',result)
    



