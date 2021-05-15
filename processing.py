# use this python file to check the KeyID and map it to something.
def verify(KeyID):
    if KeyID == 13: # enter pressed
        print("in")
        result = '<ENTER>\n'
    elif KeyID == 8:
        result = '<BackSpace>'
    elif KeyID == 9:
        result = '<Tab>'
    else:
        result = chr(KeyID)
    return result