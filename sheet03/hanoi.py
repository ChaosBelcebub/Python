tower_hanoi(n, source, helper, target):
    if n > 0:
    	# Die Funktion wird rekursiv aufgerufen, jedoch werden target
    	# und helper vertauscht
        tower_hanoi(n-1, source, target, helper)
        # Die oberste Scheibe wird vom Stab "source" genommen und zum
        # "target" hinzugefügt
        if source[1]:
            disk = source[1][-1]
            print("Bewege", disk, "von", source[0], "nach", target[0])
            del source[1][-1]
            target[1] += [disk]
        # Die Funktion wird erneut rekursiv aufgerufen, jedoch wird
        # hier helper und source getauscht
        tower_hanoi(n-1, helper, source, target)

tower_hanoi(4, ["Quelle", [4, 3, 2, 1]], ["Hilf", []], ["Ziel", []])

# In welchem Ausführungsschritt wird zum ersten Mal eine Scheibe von
# einem Stab entfernt und warum erst dann?

# In Schritt 22. Die Funktion wird vorher immer rekursiv aufgerufen,
# wobei n immer um eines kleiner wird. Erst vor Zeile 22 ist n kleiner 1,
# womit das erste mal der if-block betreten wird.

# In welcher Konfiguration befinden sich die Stäbe nach exakt 100 der ins-
# gesamt 200 Ausführungsschritte und was passiert dann in den folgenden
# vier Schritten?

# Das Programm befindet sich wieder im ersten Aufruf der Funktion, auf dem Stab
# Source befindet sich nur noch die 4, auf Helper befinden sich die 3, 2 und 1.
# In den nächsten 4 Schritten wird der if-block betreten und die 4 in "source"
# wird als disk geschpeichert. Auf das Terminal wird die Ausgabe "Bewege 4 von
# Quelle nach Ziel" gedruckt und die 4 wird in Source gelöscht.