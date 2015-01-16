import re


def find_dates(text):
    """Find every Date in text and return a list of dictionarys

    Args:
      text (string): the text to search in

    Return:
      list: List of dictionarys

    """
    output = []
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
              "August", "September", "Oktober", "November", "Dezember"]
    listAll = re.findall(
        r"([1-3]?[0-9])\. ?([A-Za-zä]+) ([0-9]{4}), ([1-2]?[0-9]):([0-9]{2}) "
        + "Uhr", text)
    for day, month, year, hour, minute in listAll:
        if month not in months:
            continue
        dictionary = {'day': int(day), 'month': months.index(month) + 1,
                      'year': int(year), 'hour': int(hour),
                      'minute': int(minute)}
        output.append(dictionary)
    return output


def test_find_dates():
    assert find_dates("Dies ist ein Testdatum: 10. März 2014, 9:05 "
                      + "Uhr") == [{'month': 3, 'minute': 5, 'day': 10,
                                    'hour': 9, 'year': 2014}]
    assert find_dates("Dies ist ein Testdatum: 10. März 2014, 9:05 Uhr Aber "
                      + "auch dies ist ein Testdatum: 2.April 1999, 18:22 " +
                      "Uhr") == [{'month': 3, 'minute': 5, 'day': 10,
                                  'hour': 9, 'year': 2014},
                                 {'month': 4, 'minute': 22, 'day': 2,
                                  'hour': 18, 'year': 1999}]
    assert find_dates("Hier befinden sich keine Daten!") == []
    assert find_dates("Um 8:32 Uhr am 12. Juni stehen hier immer noch" +
                      "keine!") == []
