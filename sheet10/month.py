import re

def find_dates(text):
    """Find every Date in text and return a list of dictionarys

    Args:
      text (string): the text to search in

    Return:
      list: List of dictionarys

    """
    output = []
    listAll = []
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
              "August", "September", "Oktober", "November", "Dezember"]
    listAll = re.findall(\
        r"[1-3]?[0-9]\. ?[A-Za-zä]+ [0-9]{4}, [1-2]?[0-9]:[0-9]{2} Uhr", text)
    for date in listAll:
        dictionary = {}
        dictionary['day'] = int(re.findall(r"[1-3]?[0-9]", date)[0])
        dictionary['year'] = int(re.findall(r"[0-9]{4}", date)[0])
        dictionary['month'] = months.index(re.findall(r"[A-Za-zä]+", date)[0])\
                              + 1
        dictionary['hour'] = int(re.findall(r"[1-2]?[0-9](?=:)", date)[0])
        dictionary['minute'] = int(re.findall(r"(?<=:)[0-9]{2}", date)[0])
        output.append(dictionary)
    return output
        
def find_dates_test():
    assert find_dates("Dies ist ein Testdatum: 10. März 2014, 9:05 Uhr") ==\
           [{'month': 3, 'minute': 5, 'day': 10, 'hour': 9, 'year': 2014}]
    assert find_dates("Dies ist ein Testdatum: 10. März 2014, 9:05 Uhr Aber "\
                      + "auch dies ist ein Testdatum: 2.April 1999, 18:22 Uhr")\
                      == [{'month': 3, 'minute': 5, 'day': 10, 'hour': 9,
                           'year': 2014}, {'month': 4, 'minute': 22, 'day':
                                             2, 'hour': 18, 'year': 1999}]
    assert find_dates("Hier befinden sich keine Daten!") == []
    assert find_dates("Um 8:32 Uhr am 12. Juni stehen hier immer noch keine!")\
                      == []
