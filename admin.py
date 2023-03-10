import deta
import config
import os

detaB = deta.Deta(config.api_key)
db = detaB.Base("command")

while True:
    res = db.fetch()
    for compIdx in range(len(res.items)):
        print(f"{compIdx}: {res.items[compIdx]['key']}")