a = ["lemon", "lennon", "lenin", "leon"]

for word in a:
    print word

for i in range(0,10):
    print i

for i in range(0,1000):
    print "this is loop number", str(i)

names = ["Juan Jose", "Mathura", "Chino", "Yuli", "Jen"]

for name in names:
    print name

    #how about an if statement

for name in names:
    if name.startswith("J"):
        print "This is the friend whose name starts with a J"

for name in names:
    if name.startswith("J") or name.endswith("o")
        print "This is the friend whose name starts with a J"
