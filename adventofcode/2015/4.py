import sys 
import hashlib 

input = sys.argv[1]

num = 0

while True:
    test = f"{input}{num}"
    data = test.encode('utf-8')
    md5_hash = hashlib.md5(data).hexdigest()
    
    if md5_hash.startswith("000000"):
        print(f"solution: {num}")
        break
    else:
        num += 1

