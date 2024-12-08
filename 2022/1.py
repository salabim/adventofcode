with open("1.txt", "r") as file:
    lines = map(str.strip, file.readlines())
    
elves = [0]
for line in lines:
    if line:
        elves[-1] += int(line)
    else:
        elves.append(0)
elves.sort()
print(elves[-1])
print(sum(elves[-3:]))



print(sorted((sum(map(int, l)) for l in (elve.split() for elve in open("1.txt", "r").read().split("\n\n"))))[-1])    
print(sum(sorted((sum(map(int, l)) for l in (elve.split() for elve in open("1.txt", "r").read().split("\n\n"))))[-3:]))    
