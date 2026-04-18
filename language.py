south_india = [
    "Tamil",
    "Telugu",
    "Kannada",
    "Malayalam",
    "Tulu",
    "Konkani",
    "Kodava",
    "Beary",
    "Gondi",
    "Toda"
]

def getlanguage():
    global south_india
    return south_india

def islanguageexist(languagename):
    global south_india
    result = languagename in south_india
    return result
