def checkStringPallindrom(txt):
    if len(txt)<1:
        print("Empty String")
        return False
    elif len(txt)==1:
        return True
    else:
        str = txt[::-1]
        return True if str.lower()==txt.lower() else False
    
print(checkStringPallindrom("amaama"))