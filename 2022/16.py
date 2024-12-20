import aocd

data = '''\
Valve TB has flow rate=20; tunnel leads to valve DN
Valve SY has flow rate=0; tunnels lead to valves OJ, RZ
Valve EH has flow rate=0; tunnels lead to valves OL, GH
Valve ZE has flow rate=0; tunnels lead to valves WZ, WE
Valve RZ has flow rate=0; tunnels lead to valves GM, SY
Valve FN has flow rate=0; tunnels lead to valves YP, DN
Valve GH has flow rate=12; tunnels lead to valves EH, PV, BH, WY, DW
Valve YL has flow rate=0; tunnels lead to valves GM, YZ
Valve IA has flow rate=0; tunnels lead to valves AA, GM
Valve WK has flow rate=0; tunnels lead to valves HJ, AA
Valve HK has flow rate=0; tunnels lead to valves AA, OJ
Valve WG has flow rate=0; tunnels lead to valves YP, EK
Valve XU has flow rate=0; tunnels lead to valves EX, SK
Valve BH has flow rate=0; tunnels lead to valves GH, DL
Valve OI has flow rate=0; tunnels lead to valves EZ, OV
Valve WE has flow rate=5; tunnels lead to valves ZE, YZ, BF, EZ, HJ
Valve AC has flow rate=0; tunnels lead to valves OJ, OV
Valve EI has flow rate=18; tunnels lead to valves OD, GS, XZ, WY, QU
Valve CP has flow rate=0; tunnels lead to valves GS, AA
Valve WZ has flow rate=0; tunnels lead to valves ZE, OJ
Valve EZ has flow rate=0; tunnels lead to valves OI, WE
Valve LI has flow rate=0; tunnels lead to valves WJ, OV
Valve WJ has flow rate=0; tunnels lead to valves LI, YP
Valve AQ has flow rate=0; tunnels lead to valves PF, EX
Valve DW has flow rate=0; tunnels lead to valves EK, GH
Valve OA has flow rate=25; tunnels lead to valves OL, PN, OD
Valve ZV has flow rate=0; tunnels lead to valves GM, OV
Valve CH has flow rate=0; tunnels lead to valves QU, EX
Valve CG has flow rate=0; tunnels lead to valves PN, EK
Valve EX has flow rate=19; tunnels lead to valves AQ, XU, CH, BF
Valve DN has flow rate=0; tunnels lead to valves TB, FN
Valve QU has flow rate=0; tunnels lead to valves EI, CH
Valve QA has flow rate=0; tunnels lead to valves ZO, PU
Valve DL has flow rate=0; tunnels lead to valves OJ, BH
Valve BF has flow rate=0; tunnels lead to valves WE, EX
Valve OJ has flow rate=4; tunnels lead to valves SY, WZ, AC, DL, HK
Valve MN has flow rate=0; tunnels lead to valves AA, OV
Valve WY has flow rate=0; tunnels lead to valves EI, GH
Valve PF has flow rate=21; tunnel leads to valve AQ
Valve EK has flow rate=10; tunnels lead to valves DW, WG, CG, XZ
Valve GA has flow rate=0; tunnels lead to valves KB, YP
Valve BW has flow rate=0; tunnels lead to valves AL, GD
Valve YZ has flow rate=0; tunnels lead to valves WE, YL
Valve VG has flow rate=0; tunnels lead to valves PV, GD
Valve OD has flow rate=0; tunnels lead to valves OA, EI
Valve GM has flow rate=13; tunnels lead to valves YL, RZ, SK, ZV, IA
Valve YP has flow rate=22; tunnels lead to valves GA, AL, WJ, WG, FN
Valve SK has flow rate=0; tunnels lead to valves GM, XU
Valve PN has flow rate=0; tunnels lead to valves OA, CG
Valve AA has flow rate=0; tunnels lead to valves CP, WK, MN, HK, IA
Valve AL has flow rate=0; tunnels lead to valves BW, YP
Valve OV has flow rate=7; tunnels lead to valves AC, OI, LI, ZV, MN
Valve ZO has flow rate=23; tunnel leads to valve QA
Valve HJ has flow rate=0; tunnels lead to valves WE, WK
Valve KB has flow rate=0; tunnels lead to valves GA, PU
Valve OL has flow rate=0; tunnels lead to valves OA, EH
Valve PV has flow rate=0; tunnels lead to valves GH, VG
Valve PU has flow rate=24; tunnels lead to valves KB, QA
Valve GD has flow rate=17; tunnels lead to valves VG, BW
Valve GS has flow rate=0; tunnels lead to valves CP, EI
Valve XZ has flow rate=0; tunnels lead to valves EI, EK'''

data = """\
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""
#data = aocd.get_data(year=2022, day=16)
leadto = {}
flowrate = {}

for line in data.splitlines():
    valve = line.split(' has')[0].split(' ')[1]
    flowrate[valve] = int(line.split(';')[0].split('=')[1])
    leadto[valve] = [s.replace(",", "") for s in line.split('valve')[-1].split(' ') if len(s) >=2]

print(leadto)
print(flowrate)

def solve(valve, open_valves, flow, t, released):
    if t == 30:
#        print(t,open_valves)
        yield released, open_valves, flow
    else:
        released += 2*flow
        if valve not in open_valves[:-1]:
            flow += flowrate[valve]
        for valve in leadto[valve]:
            yield from solve(valve, open_valves+[valve], flow, t+2, released)
        

        
        
m=-1
for released, open_valves,flow in solve('AA', [], 0,0,0):
    if m < released:
        m = released
        print(released, open_valves, flow)
print('done')
