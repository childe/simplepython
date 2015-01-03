d = {
    "liujia": 28,
    "zn": 29
}

try:
    age = d['trh']
except IOError as e:
    print "Exception occured"
    print type(e), str(e)
except KeyError as e:
    print "Exception occured"
    print type(e), str(e)
else:
    print "Other type of Exception occured"
finally:
    print "print this no matter what happend"
