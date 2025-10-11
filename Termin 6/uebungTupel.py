grenzen = (10000, 20000, 30000)
saetze = (0, 0.1, 0.2, 0.3)

jahreseinkommen = float(input('Was ist Ihr Jahreseinkommen? '))

steuersatz = saetze[-1]

for i, grenze in enumerate(grenzen):
    if jahreseinkommen < grenze:
        steuersatz = saetze[i]
        break


zu_zahlen = jahreseinkommen*steuersatz

print(f'Sie müssen {zu_zahlen}€ zahlen. Ihr Steuersatz ist {steuersatz*100}%.')