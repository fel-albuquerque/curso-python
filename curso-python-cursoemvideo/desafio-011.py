#desafio-011

larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt

print('Sua parade tem {} x {} , e a sua area é de {} m²'.format(larg, alt, area))

tinta = area / 2

print('Para pintar a parede voce precisa de {} l de tinta'.format(tinta))
