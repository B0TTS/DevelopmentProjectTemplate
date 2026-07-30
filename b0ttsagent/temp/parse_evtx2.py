import Evtx.Evtx as evtx
import re, sys
from collections import Counter, defaultdict

path = r"C:\Users\Jonah\DevelopmentTemplate\Events.evtx"

# print a few samples first
with evtx.Evtx(path) as log:
    n=0
    for rec in log.records():
        xml = rec.xml()
        print(repr(xml[:600]))
        print("======")
        n+=1
        if n>=2: break