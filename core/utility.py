import hashlib

def getPassHash(credential : str) -> str:

    hashObj = hashlib.new("sha256")
    hashObj.update(credential.encode("utf-8"))
    tkn = hashObj.hexdigest()
    return tkn
