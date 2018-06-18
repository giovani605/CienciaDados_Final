import matplotlib.pyplot as plt
import csv

#le arquivos
saida = open("saida.csv", 'r')
csv_saida = csv.DictReader(saida)

# inicia dict
carry = {'BRONZE': 0, 'SILVER': 0, 'GOLD': 0, 'PLATINUM': 0, 'DIAMOND': 0, 'MASTER': 0, 'CHALLENGER': 0}
mid = {'BRONZE': 0, 'SILVER': 0, 'GOLD': 0, 'PLATINUM': 0, 'DIAMOND': 0, 'MASTER': 0, 'CHALLENGER': 0}
top = {'BRONZE': 0, 'SILVER': 0, 'GOLD': 0, 'PLATINUM': 0, 'DIAMOND': 0, 'MASTER': 0, 'CHALLENGER': 0}
jungle = {'BRONZE': 0, 'SILVER': 0, 'GOLD': 0, 'PLATINUM': 0, 'DIAMOND': 0, 'MASTER': 0, 'CHALLENGER': 0}
sup = {'BRONZE': 0, 'SILVER': 0, 'GOLD': 0, 'PLATINUM': 0, 'DIAMOND': 0, 'MASTER': 0, 'CHALLENGER': 0}
#inicia valores das médias
bc = 0
sc = 0
gc = 0
pc = 0
dc = 0
mc = 0
cc = 0
bs = 0
ss = 0
gs = 0
ps = 0
ds = 0
ms = 0
cs = 0
bm = 0
sm = 0
gm = 0
pm = 0
dm = 0
mm = 0
cm = 0
bj = 0
sj = 0
gj = 0
pj = 0
dj = 0
mj = 0
cj = 0
bt = 0
st = 0
gt = 0
pt = 0
dt = 0
mt = 0
ct = 0
# para cada linha do csv soma se a lane e rank correspondem
for stats in csv_saida:
    if stats['role'] == 'CARRY':
        a = carry.get(stats['tier'])
        if stats['tier'] == 'BRONZE':
            bc += 1
            carry['BRONZE'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'SILVER':
            sc += 1
            carry['SILVER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'GOLD':
            gc += 1
            carry['GOLD'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'PLATINUM':
            pc += 1
            carry['PLATINUM'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'DIAMOND':
            dc += 1
            carry['DIAMOND'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'MASTER':
            mc += 1
            carry['MASTER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'CHALLENGER':
            cc += 1
            carry['CHALLENGER'] = a + float(stats['visionScore'])
    if stats['role'] == 'JUNGLE':
        a = jungle.get(stats['tier'])
        if stats['tier'] == 'BRONZE':
            bj += 1
            jungle['BRONZE'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'SILVER':
            sj += 1
            jungle['SILVER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'GOLD':
            gj += 1
            jungle['GOLD'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'PLATINUM':
            pj += 1
            jungle['PLATINUM'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'DIAMOND':
            dj += 1
            jungle['DIAMOND'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'MASTER':
            mj += 1
            jungle['MASTER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'CHALLENGER':
            cj += 1
            jungle['CHALLENGER'] = a + float(stats['visionScore'])
    if stats['role'] == 'MIDDLE':
        a = mid.get(stats['tier'])
        if stats['tier'] == 'BRONZE':
            bm += 1
            mid['BRONZE'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'SILVER':
            sm += 1
            mid['SILVER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'GOLD':
            gm += 1
            mid['GOLD'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'PLATINUM':
            pm += 1
            mid['PLATINUM'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'DIAMOND':
            dm += 1
            mid['DIAMOND'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'MASTER':
            mm += 1
            mid['MASTER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'CHALLENGER':
            cm += 1
            mid['CHALLENGER'] = a + float(stats['visionScore'])
    if stats['role'] == 'SUPPORT':
        a = sup.get(stats['tier'])
        if stats['tier'] == 'BRONZE':
            bs += 1
            sup['BRONZE'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'SILVER':
            ss += 1
            sup['SILVER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'GOLD':
            gs += 1
            sup['GOLD'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'PLATINUM':
            ps += 1
            sup['PLATINUM'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'DIAMOND':
            ds += 1
            sup['DIAMOND'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'MASTER':
            ms += 1
            sup['MASTER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'CHALLENGER':
            cs += 1
            sup['CHALLENGER'] = a + float(stats['visionScore'])
    if stats['role'] == 'TOP':
        a = top.get(stats['tier'])
        if stats['tier'] == 'BRONZE':
            bt += 1
            top['BRONZE'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'SILVER':
            st += 1
            top['SILVER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'GOLD':
            gt += 1
            top['GOLD'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'PLATINUM':
            pt += 1
            top['PLATINUM'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'DIAMOND':
            dt += 1
            top['DIAMOND'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'MASTER':
            mt += 1
            top['MASTER'] = a + float(stats['visionScore'])
        elif stats['tier'] == 'CHALLENGER':
            ct += 1
            top['CHALLENGER'] = a + float(stats['visionScore'])

# faz a média de cada role e rank
carry['BRONZE'] = carry.get('BRONZE')/bc
carry['SILVER'] = carry.get('SILVER')/sc
carry['GOLD'] = carry.get('GOLD')/gc
carry['PLATINUM'] = carry.get('PLATINUM')/pc
carry['DIAMOND'] = carry.get('DIAMOND')/dc
carry['MASTER'] = carry.get('MASTER')/mc
carry['CHALLENGER'] = carry.get('CHALLENGER')/cc

jungle['BRONZE'] = jungle.get('BRONZE')/bj
jungle['SILVER'] = jungle.get('SILVER')/sj
jungle['GOLD'] = jungle.get('GOLD')/gj
jungle['PLATINUM'] = jungle.get('PLATINUM')/pj
jungle['DIAMOND'] = jungle.get('DIAMOND')/dj
jungle['MASTER'] = jungle.get('MASTER')/mj
jungle['CHALLENGER'] = jungle.get('CHALLENGER')/cj

mid['BRONZE'] = mid.get('BRONZE')/bm
mid['SILVER'] = mid.get('SILVER')/sm
mid['GOLD'] = mid.get('GOLD')/gm
mid['PLATINUM'] = mid.get('PLATINUM')/pm
mid['DIAMOND'] = mid.get('DIAMOND')/dm
mid['MASTER'] = mid.get('MASTER')/mm
mid['CHALLENGER'] = mid.get('CHALLENGER')/cm

sup['BRONZE'] = sup.get('BRONZE')/bs
sup['SILVER'] = sup.get('SILVER')/ss
sup['GOLD'] = sup.get('GOLD')/gs
sup['PLATINUM'] = sup.get('PLATINUM')/ps
sup['DIAMOND'] = sup.get('DIAMOND')/ds
sup['MASTER'] = sup.get('MASTER')/ms
sup['CHALLENGER'] = sup.get('CHALLENGER')/cs

top['BRONZE'] = top.get('BRONZE')/bt
top['SILVER'] = top.get('SILVER')/st
top['GOLD'] = top.get('GOLD')/gt
top['PLATINUM'] = top.get('PLATINUM')/pt
top['DIAMOND'] = top.get('DIAMOND')/dt
top['MASTER'] = top.get('MASTER')/mt
top['CHALLENGER'] = top.get('CHALLENGER')/ct

# cria subplots
fig, ax = plt.subplots()
# as keys e os values e a label de cada grafico
ax.plot(sup.keys(), sup.values(), label='Support')
ax.plot(carry.keys(), carry.values(), label='Carry')
ax.plot(mid.keys(), mid.values(), label='Mid')
ax.plot(jungle.keys(), jungle.values(), label='Jungle')
ax.plot(top.keys(), top.values(), label='Top')
# legenda do grafico
ax.legend(loc=0, shadow=True, fontsize='x-large')
# label do eixo x
plt.xlabel('Rank')
# label do eixo y
plt.ylabel('Vision score')
# titulo do grafico
plt.title('Average vision score per role per rank')
# salva
plt.savefig('visionScore_position_rank.png')
# mostra
plt.show()
