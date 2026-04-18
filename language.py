west_india = [
    "Gujarati",
    "Marathi",
    "Konkani",
    "Hindi",
    "Marwari",
    "Malvi",
    "Bhili",
    "Kutchi"
]

def getlanguage():
    global west_india
    return west_india

def islanguageexist(languagename):
    global west_india
    result = languagename in west_india
    return result
