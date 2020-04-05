import random, sys
def primary():
  #  open txt file to read quotes

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    # print random quote
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd], end="")
    
if __name__== "__main__":
    primary()
