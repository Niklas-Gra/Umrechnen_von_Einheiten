# Umrechnung Druck Bar in Pascal
# Variablen: bar -> Wert in Bar, pascal -> Wert in Pascal, urf_bar_pa -> Umrechnungfaktor Bar/Pascal
bar = float(input("Gib den Wert in Bar an, den du Umrechnen willst:"))
urf_bar_pa = 100000

# Rechnung
pascal = bar * urf_bar_pa

# Ergebnis ausgeben
print(bar, "bar", "sind", pascal, "Pascal")

# Umrechnung Meter pro Sekunde in Kilometer pro Stunde
# Variabelen: m_s -> Meter pro Sekunde, km_h -> Kilometer pro Stunde, -> urf_ms_kmh -> Umrechnungsfaktor m/s in km/h
m_s = float(input("Gib den Wert in m/s an, den du Umrechnen willst:"))
urf_ms_kmh = 3.6

# Rechnung
km_h = m_s * urf_ms_kmh

# Ergebnis ausgeben
print(m_s, "Meter pro Sekunden", "sind", km_h, "Kilometer pro Stunde")