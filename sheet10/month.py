import re

def find_dates(text):
    """Find every Date in text

    Args:
      text (string): the text to search in

    """
    output = []
    listAll = []
    months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
              "August", "September", "Oktober", "November", "Dezember"]
    listAll = re.findall(\
        r"[0-3]?[0-9]\. [A-Za-zä]+ [0-9]{4}, [1-2]?[0-9]:[0-9][0-9] Uhr", text)
    for date in listAll:
        dictionary = {}
        dictionary['day'] = re.findall(r"[0-3]?[0-9]", date)[0]
        dictionary['year'] = re.findall(r"[0-9]{4}", date)[0]
        dictionary['month'] = months.index(re.findall(r"[A-Za-zä]+", date)[0])\
                              + 1
        output.append(dictionary)
    return output
        
    
