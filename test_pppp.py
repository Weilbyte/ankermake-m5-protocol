import logging as log
import time
from libflagship.ppppapi import AnkerPPPPAsyncApi, PPPPState
from libflagship.pppp import Duid

log.basicConfig(level=log.DEBUG)

api = AnkerPPPPAsyncApi.open_broadcast('0.0.0.0')
api.duid = Duid.from_string('USPRAKM-036055-GVPMU')
api.connect_lan_search()
for _ in range(5):
    api.poll(2.0)
    if api.state == PPPPState.Connected:
        break
print("FINAL STATE:", api.state)
