import hashlib

def getSHA256(str: str):
    md = hashlib.sha256()
    md.update(str.encode('utf-8'))
    return md.hexdigest()

if __name__ == "__main__":
    str = 'dsjfsdfsdfjdksljflksdjlfnbvkdjfoelwknfldskjfldmflsdjfkldsfmcsl/d;nfv/cmewcmwelkfnmewknkdlsj'
    print('md5', str, getSHA256(str) == getSHA256(str), len(getSHA256(str)))

