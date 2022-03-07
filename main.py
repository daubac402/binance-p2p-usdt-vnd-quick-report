import requests
import json

data = {
    "asset": "USDT",
    "fiat": "VND",
    "merchantCheck": False,
    "page": 1,
    # "payTypes": [],
    # "publisherType": None,
    "rows": 10,
    "tradeType": "BUY",
}

r = requests.post(
    "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search",
    json=data,
)
# print(r.text)
result = json.loads(r.text)

print(
    "1 %s to %s, min %s: %s"
    % (
        data["asset"],
        data["fiat"],
        data["tradeType"],
        "{:,.0f}".format(float(result["data"][0]["adv"]["price"])),
    )
)
for item in result["data"]:
    print(
        "%s | %s - %s | %s (%s orders, %s%% rate)"
        % (
            "{:,.0f}".format(float(item["adv"]["price"])),
            "{: >14,.0f}".format(float(item["adv"]["minSingleTransAmount"])),
            "{: >14,.0f}".format(float(item["adv"]["maxSingleTransAmount"])),
            item["advertiser"]["nickName"],
            "{:,}".format(item["advertiser"]["monthOrderCount"]),
            "{:,.2f}".format(100 * float(item["advertiser"]["monthFinishRate"])),
        )
    )
