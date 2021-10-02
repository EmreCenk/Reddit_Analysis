

#TODO: COMPARE DATA TO MOST COMMON WORDS IN ENGLISH

from collect_scraped_data import get_scraped_sorted_words

x, counted = get_scraped_sorted_words()
for i in range(1, len(x)):
    print(str(i) + ".", x[-i] , "-", counted[x[-i]])
y = []
how_many_to_include = 30
x = x[len(x) - how_many_to_include: ]
for k in x:
    y.append(counted[k])

import matplotlib.pyplot as plt
plt.style.use('ggplot')



x_pos = [i for i in range(len(x))]
print(x_pos)

plt.bar(x_pos, y, color='green')
plt.xlabel("Word")
plt.ylabel("Number of Times Used in Memes")
plt.title("Word Usage in Top Memes Posted in r/Memes")

plt.xticks(x_pos, x)

plt.show()

