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

# Umrechnung Kilometer in Meilen
# Variabelen: km -> Wert in Kilometern, mi -> Wert in Meilen, urf_km_mi -> Umrechnungsfaktor Kilometer in Meilen
km = float(input("Gib den Wert in Kilometern an, den du Umrechnen willst:"))
urf_km_mi = 1.609

# Rechnung
mi = km / urf_km_mi

# Ergebnis ausgeben
print(km, "Kilometer", "sind", mi, "Meilen")

# Umrechnung Grad Celsius in Grad Fahrenheit
# Variabelen: tc -> Wert in Celsius, tf -> Wert in Fahrenheit, urf_tc_tf -> Umrechnungsfaktro Celsius in Fahrenheit
tc = float(input("Gib den Wert in Grad Celsius ein, den du Umrechnen willst"))
urf_tc_tf = 1.8 + 32

# Rechnung
tf = tc * urf_tc_tf

# Ergebnis ausgeben
print(tc, "Grad Celsius", "sind", tf, "Grad Fahrenheit")