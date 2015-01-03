try:
    import simplejson as json
except:
    import json
print  json

try:
    n = 1/0
except:
    n = 0xffffffff
print n

d ={
    "liujia":28,
    "zn":29
}
try:
    print d['trh']
except:
    print None
