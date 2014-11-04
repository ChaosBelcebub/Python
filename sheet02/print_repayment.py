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
    m_rate = (rate / 12) / 100
    month = 0
    print("-" * 62)
    print(" Monat  Restschuld  Ratenzahlung  Anteil  Anteil   Restschuld")
    print("        (alt)                     Zinsen  Tilgung  (neu)")
    print("-" * 62)
    while amount > 0 and month < 72:
        p_rate = amount * m_rate
        tilgung = interest - p_rate
        if tilgung < amount:
            new_amount = amount - tilgung
        else:
            tilgung = amount
            interest = amount + p_rate
            new_amount = amount - tilgung
        month += 1
        print("%6.0f" %month, "%11.2f" %amount, "%13.2f" %interest, "%7.2f" %p_rate, "%8.2f" %tilgung, "%11.2f" %new_amount)
        amount = new_amount
    print("-" * 62)
    if month >= 72:
        print("Die maximale Laufzeit wurde erreicht.")
