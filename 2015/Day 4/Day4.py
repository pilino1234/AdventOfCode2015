import hashlib
from itertools import count

def md5hash(key, number):
    input = key + str(number)
    md5 = hashlib.md5()
    md5.update(bytes(input, "utf-8"))
    return md5.hexdigest()

def find_0s(key, zeros):
    for i in count():
        hash = str(md5hash(key, i))
        if hash.startswith("0" * zeros):
            return i

if __name__ == "__main__":
    print(md5hash("abcdef", 609043))
    print(find_0s("abcdef", 5))
    
    print(md5hash("pqrstuv", 1048970))
    print(find_0s("pqrstuv", 5))

    print(find_0s("bgvyzdsv", 5))
    
    print(find_0s("bgvyzdsv", 6))
    
    
    
