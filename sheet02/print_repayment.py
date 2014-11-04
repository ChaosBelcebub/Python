def print_repayment(amount, interest, rate):
    """gibt auf der Konsole einen Tilgungsplan aus"""
    print("=" * 62)
    print("Tilgungsplan (alle Beträge in €)")
    print("=" * 62)
    print("\n")
    print("Kredit über: €", "%.2f" %amount)
    print("Zinssatz:   ", "%.2f" %rate, "% p.a.")
    print("Monatsrate:  €", "%.2f" %interest)
    print("\n")
    """ Berechnet die Monatliche Zinssatz """
    m_rate = (rate / 12) / 100
    """ Setzt die Anzahl der Monate """
    month = 0
    print("-" * 62)
    print(" Monat  Restschuld  Ratenzahlung  Anteil  Anteil   Restschuld")
    print("        (alt)                     Zinsen  Tilgung  (neu)")
    print("-" * 62)
    while amount > 0 and month < 72:
        """ Berechnet den Anteil der Zinsen """
        p_rate = amount * m_rate
        """ Berechnet den Anteil der Tilgung """
        tilgung = interest - p_rate
        """ Normalerweise ist die Tilgung kleiner als die Restschuld """
        if tilgung < amount:
            new_amount = amount - tilgung
        """ Fals das nicht der Fall ist muss anderst vorgegangen werden """
        else:
            tilgung = amount
            interest = amount + p_rate
            new_amount = amount - tilgung
        """ Zählt die Monate """
        month += 1
        """ Druckt das Ergebnis """
        print("%6.0f" %month, "%11.2f" %amount, "%13.2f" %interest, "%7.2f" %p_rate, "%8.2f" %tilgung, "%11.2f" %new_amount)
        amount = new_amount
    print("-" * 62)
    if month >= 72:
        print("Die maximale Laufzeit wurde erreicht.")
