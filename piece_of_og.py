import os, json, time
import requests

ALCHEMY_API = "https://opt-mainnet.g.alchemy.com/nft/v2/{}/getOwnersForToken?contractAddress={}&tokenId={}&pageKey=1&pageSize={}"
ALCHEMY_KEY = os.getenv('KEY_ALCHEMY_POOPZTER')
CONTRACT    = "0x32F277cEce2Ba12029E07c6C1D1eBA63F1Bb518b"
IDS         = [ 8, 9, 10 ] # TODO
PAGE_SIZE   = 5_000
OUT_PATH    = "./json/piece_of_og/{}.json"

for id in IDS:
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
