from datetime import datetime

SHELLY_UNIX = 1596491091
SHELLY_SLOT = 4924800

def getSlotFromUnixTime(ut):
    slot = ut - SHELLY_UNIX + SHELLY_SLOT
    print(f"Cardano slot is: '{slot}'")
    return slot

def getUTCEstimateFromSlot(slot):
    ts = SHELLY_UNIX + (slot - SHELLY_SLOT)
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
