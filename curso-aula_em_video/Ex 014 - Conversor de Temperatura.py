tc = float(input('Informe a temeperatura em °C: '))

tf = (9/5*tc)+32
tk = tc + 273

print('{}°C correspondem a {}°F e {}K'.format(int(tc),int(tf), int(tk)))
