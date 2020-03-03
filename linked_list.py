a = "abcabcbb"

length = 0
prev = ""
subs = set()
subs_lens = set()
for item in a:
    if item in subs:
        subs = set(item)
        subs_lens.add(length)
        length = 1
    else:
        length += 1
        subs.add(item)
    prev = item

print(max(subs_lens))
