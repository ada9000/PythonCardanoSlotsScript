# Cardano Slots Script
A very simple python script to calulate slots

# How to use
```
python -i CardanoSlots.py
```
A interactive terminal will open <br/>
Get a unix time [from here if you don't know how](https://www.unixtimestamp.com/) <br/>
Use 'getSlotFromUnixTime' to get a slot <br/>
You can check using getUTCEsitmateFromSlot <br/>
```
mySlot = getSlotFromUnixTime(<YOUR_TIME_HERE>)
getUTCEstimateFromSlot(mySlot)
```

# Notes
In the event of a hard fork in which times are affected this code will be deprecated.