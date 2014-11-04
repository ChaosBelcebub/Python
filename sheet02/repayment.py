def repayment(amount, interest, rate):
    """gibt auf der Konsole einen Tilgungsplan aus"""

    m_rate = (rate / 12) / 100
    month = 0
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
        print(month, round(amount, 2), round(interest, 2), round(p_rate, 2),\
            round(tilgung, 2), round(new_amount, 2))
        amount = new_amount
    print("-" * 62)
    if month >= 72:
        print("Die maximale Laufzeit wurde erreicht.")
