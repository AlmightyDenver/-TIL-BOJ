import collections
cnt = collections.Counter()
for colours in ['R', 'B', 'G', 'B', 'B']:
    cnt[colours] += 1
print(cnt)
# Counter({'blue': 3, 'red': 2, 'green': 1})

import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Conter(words).most_common(10)
# most common 10 words


c = Counter(a=4, b=2,c=0)
sorted(c.elements())
#['a','a','a','a','b','b']