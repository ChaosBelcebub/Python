"""Actors with dictionary, WS1415

References:
 * Lecture slides at:
   http://www.informatik.uni-freiburg.de/~ki/teaching/ws1415/info1/lecture.html
 * Python documentation at:
   http://docs.python.org/3/

"""

actors = [[("salutation", "Mr."), ("givenName", "Peter"),
           ("familyName", "Dinklage"), ("birthday", "06/11/1969"),
           ("GoT", "Lannister", "Tyrion")],
          [("salutation", "Mrs."), ("givenName", "Michelle"),
           ("familyName", "Fairley"), ("birthday", "01/17/1964"),
           ("GoT", "Stark", "Catelyn")],
          [("salutation", "Mr."), ("givenName", "Nicolaj"),
           ("familyName", "Coster-Waldau"), ("birthday", "07/27/1970"),
           ("GoT", "Lannister", "Jamie")],
          [("salutation", "Ms."), ("givenName", "Maisie"),
           ("familyName", "Williams"), ("birthday", "04/17/1997"),
           ("GoT", "Stark", "Arya")],
          [("salutation", "Mrs."), ("givenName", "Emilia"),
           ("familyName", "Clarke"), ("birthday", "05/01/1987"),
           ("GoT", "Targaryen", "Daenerys")]]

# Your functions follow here
# ...


def actors_to_string(actors):
    out = ""
    for lst in actors:
        for tup in lst:
            if len(tup) == 2:
                out += tup[0] + ": " + tup[1] + "\n"
            else:
                out += tup[0] + ": " + tup[2] + " " + tup[1] + "\n"
        out += "\n"
    return out


def actors_to_gotfamilies(actors):
    out = {}
    for lst in actors:
        if lst[4][1] not in out:
            out[lst[4][1]] = {}
        out[lst[4][1]][lst[4][2]] = {}
        for tup in lst:
            if len(tup) == 2:
                out[lst[4][1]][lst[4][2]][tup[0]] = tup[1]
    return out

if __name__ == "__main__":
    # Your tests follow here after you deleted the next line:
    got = actors_to_gotfamilies(actors)
    assert got["Lannister"] == {'Jamie': {'salutation': 'Mr.',
                                          'birthday': '07/27/1970',
                                          'givenName': 'Nicolaj',
                                          'familyName': 'Coster-Waldau'},
                                'Tyrion': {'salutation': 'Mr.',
                                           'birthday': '06/11/1969',
                                           'givenName': 'Peter',
                                           'familyName': 'Dinklage'}}
    assert got["Stark"]["Arya"] == {'salutation': 'Ms.',
                                    'birthday': '04/17/1997',
                                    'givenName': 'Maisie',
                                    'familyName': 'Williams'}
    assert got["Targaryen"]["Daenerys"]["givenName"] == "Emilia"
    assert got["Lannister"]["Jamie"]["familyName"] == "Coster-Waldau"
    # Your print command for exercise 5.3b follows here:
    print("There are", len(got["Stark"]), "member of the Stark family.")
