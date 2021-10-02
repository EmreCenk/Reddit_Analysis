



from collect_scraped_data import get_scraped_sorted_words

a = get_scraped_sorted_words()
print(a)

"""
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = ['a', 'b', 'c', 'd', 'e', 'f']
y = [1, 2, 3, 4, 5, 6]

x_pos = [i for i in range(len(x))]
print(x_pos)

plt.bar(x_pos, y, color='green')
plt.xlabel("Word")
plt.ylabel("Number of Times Used in Memes")
plt.title("Word Usage in Top Memes Posted in r/Memes")

plt.xticks(x_pos, x)

plt.show()

"""