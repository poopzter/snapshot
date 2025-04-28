import os, json, time
import requests

ALCHEMY_API = "https://soneium-mainnet.g.alchemy.com/nft/v2/{}/getOwnersForToken?contractAddress={}&tokenId={}&pageKey=1&pageSize={}"
ALCHEMY_KEY = os.getenv('KEY_ALCHEMY_POOPZTER')
CONTRACT    = "0xA9213211Ac66aFB650C3b501bdD538013A35442f"
FROM_ID     = 1
TO_ID       = 3
PAGE_SIZE   = 5_000
OUT_PATH    = "./json/piece_on_soneium/{}.json"

for id in range(FROM_ID, TO_ID+1):
    # craft url
    url = ALCHEMY_API.format(ALCHEMY_KEY, CONTRACT, id, PAGE_SIZE)

    # fetch data
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # dump to file
    dest = OUT_PATH.format(id)
    with open(dest, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    print(dest, len(data['owners']))

    # a bit delay
    time.sleep(1)
