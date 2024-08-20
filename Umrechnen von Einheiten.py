# Menü Auswahl
def menu_umrechnung():
    while True:
        print("1. Umrechnung Druck Bar -> Pascal")
        print("2. Umrechnung Geschwindigkeit m/s -> km/h")
        print("3. Umrechnung Strecke Kilometer -> Meilen")
        print("4. Umrechnung Temperatur °C -> °F")
        print("5. Umrechnung Länge Zentimerter in Zoll")
        choice = input("Was soll umgerechnet werden?")
        
        if choice == '1':
            umrechnung_1()
            
        elif choice == '2':
            umrechnung_2()
            
        elif choice == '3':
            umrechnung_3()
        
        elif choice == '4':
            umrechnung_4
        
        elif choice == '5':
            umrechnung_5()
        
        elif choice =='6':
            print("Umrechner beendet")
            break
        
        else:
            print("Ungültige Eingabe. Bitte Versuchen Sie es erneut.")

def umrechnung_1():
    # Umrechnung Druck Bar in Pascal
    # Variablen: bar -> Druck in Bar, pascal -> Druck in Pascal, urf_bar_pa -> Umrechnungfaktor Bar/Pascal
    bar = float(input("Gib den Wert in Bar an, den du Umrechnen willst:"))
    urf_bar_pa = 100000
    
    # Rechnung
    pascal = bar * urf_bar_pa
    # Ergebnis ausgeben
    print(bar, "bar", "sind", pascal, "Pascal")

def umrechnung_2():
    # Umrechnung Meter pro Sekunde in Kilometer pro Stunde
    # Variabelen: m_s -> Meter pro Sekunde, km_h -> Kilometer pro Stunde, -> urf_ms_kmh -> Umrechnungsfaktor m/s in km/h
    m_s = float(input("Gib den Wert in m/s an, den du Umrechnen willst:"))
    urf_ms_kmh = 3.6
    # Rechnung
    km_h = m_s * urf_ms_kmh
    
    # Ergebnis ausgeben
    print(m_s, "Meter pro Sekunden", "sind", km_h, "Kilometer pro Stunde")
    
def umrechnung_3():
    # Umrechnung Kilometer in Meilen
    # Variabelen: km -> Strecke in Kilometern, mi -> Strecke in Meilen, urf_km_mi -> Umrechnungsfaktor Kilometer in Meilen
    km = float(input("Gib den Wert in Kilometern an, den du Umrechnen willst:"))
    urf_km_mi = 1.609
    
    # Rechnung
    mi = km / urf_km_mi
    # Ergebnis ausgeben
    print(km, "Kilometer", "sind", mi, "Meilen")

def umrechnung_4():
    # Umrechnung Grad Celsius in Grad Fahrenheit
    # Variabelen: tc -> Temperatur in Celsius, tf -> Temperatur in Fahrenheit, urf_tc_tf -> Umrechnungsfaktro Celsius in Fahrenheit +32
    tc = float(input("Gib den Wert in Grad Celsius ein, den du Umrechnen willst:"))
    urf_tc_tf = 1.8
    
    # Rechnung
    tf = tc * urf_tc_tf
    tf += 32
    # Ergebnis ausgeben
    print(tc, "Grad Celsius", "sind", tf, "Grad Fahrenheit")

def umrechnung_5():
    #Umrechnung Zentimeter in Zoll
    #Variablen: cm -> Länge in Zentimeter, zoll -> Länge in Zoll, urf_cm_zoll -> Umrechnungsfaktor Zentimeter in Zoll
    cm = float(input("Gib den Wert in Zentimeter ein, den du Umrechnen willst:"))
    urf_cm_zoll = 2.54
    #Rechnung
    zoll = cm / urf_cm_zoll
    #Ergebnis ausgeben
    print(cm, "Zentimeter", "sind", zoll, "Zoll")

menu_umrechnung()
