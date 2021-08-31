google

def get_LS_id(template):
    lsid = str(template)
    lsid = lsid.split(':')
    lsid = lsid[1]
    lsid = lsid[:-1]
    return lsid
