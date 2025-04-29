import json
from web3.utils.address import to_checksum_address

JSON_PATH   = "./json/piece_on_soneium/{}.json"
CSV_PATH    = "./out/{}.csv"
FROM_ID     = 1
TO_ID       = 3 # TODO

# load data
counter  = {}
checksum = 0
for id in range(FROM_ID, TO_ID+1):
    path = JSON_PATH.format(id)
    with open(path, 'r') as file:
        data = json.load(file)
        for addr in data['owners']:
            counter[addr] = counter.get(addr, 0) + 1
        checksum += len(data['owners'])

# checksum
if sum(counter.values()) != checksum:
    raise Exception('Checksum Failed')

# cluster
list_8888 = [] # 10 NFTs minted: 8,888 $POOP
list_888  = [] # 5-9 NFTs minted: 888 $POOP
list_88   = [] # 1-4 NFTs minted: 88 $POOP
for addr, cnt in counter.items():
    if cnt >= 10:
        list_8888.append(addr)
    elif cnt >= 5:
        list_888.append(addr)
    else:
        list_88.append(addr)

# sort
list_8888.sort()
list_888.sort()
list_88.sort()

# write to file
config = [
    [ 8888, list_8888 ],
    [ 888,  list_888  ],
    [ 88,   list_88   ],
]
for tier, addrs in config:
    dest = CSV_PATH.format(tier)
    with open(dest, "w") as f:
        for addr in addrs:
            addr = to_checksum_address(addr)
            f.write(f"{addr}\n")
    print(dest, len(addrs))
