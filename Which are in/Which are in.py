#Given two arrays of strings a1 and a2 return a sorted array r in
#lexicographical order of the strings of a1 which are substrings of
#strings of a2.

array1 = ["arp", "live", "strong"]
array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

out = []

#loop through items in array1
for item1 in array1:
    #loop through items in array2
    for item2 in array2:
        #if item in already in out, skip (only want uniques)
        if item2 in out:
            break
        #else, if item1 is in item2, add to out and skip searching
        elif item1 in item2:
            out.append(item1)
            break

return sorted(out)
