east_india = [
    "Bengali",
    "Odia",
    "Assamese",
    "Maithili",
    "Santali",
    "Bodo",
    "Angika",
    "Chakma"
]

def getlanguage():
    global east_india
    return east_india

def islanguageexist(languagename):
    global east_india
    result = languagename in east_india
    return result
