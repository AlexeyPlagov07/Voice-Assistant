from googlesearch import search
query = "hello"
for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)