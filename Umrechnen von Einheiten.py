# Umrechnung Druck Bar in Pascal
# Variablen: bar -> Wert in Bar, pascal -> Wert in Pascal, urf_bar_pa -> Umrechnungfaktor Bar/Pascal
bar = float(input("Gib den Wert in Bar an, den du Umrechnen willst:"))
urf_bar_pa = 100000

# Rechnung
pascal = bar * urf_bar_pa

# Ergebnis ausgeben
print(bar, "bar", "sind", pascal, "Pascal")
