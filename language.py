north_india = [
    "Hindi",
    "Punjabi",
    "Urdu",
    "Bhojpuri",
    "Haryanvi",
    "Rajasthani",
    "Kashmiri",
    "Dogri",
    "Maithili",
    "Awadhi",
    "Kannauji"
]

def getlanguage():
    global north_india
    return north_india

def islanguageexist(languagename):
    global north_india
    result = languagename in north_india
    return result
