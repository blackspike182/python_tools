
# coding: utf-8

# # Excercises for Day 4: Sequences
# 
# [4.1 Strings](#4.1)
# 
# [4.2 Lists](#4.2)
# 
# [4.3 Dictionaries](#4.3)
# 
# [4.4 The _collections_ module](#4.4)

# ## 4.1 Strings
# <a id='4.1'></a>

# ### 4.1.1
# Define a function that splits a text into sentences (on ".", "!", "?", etc.)


def text_to_sentances(text):
    sentances = []
    for punct in ".?":
        text = text.strip().replace(punct, "!")
    for sentance in text.split("!"):
        sentances.append(sentance.strip())
    return sentances


# Define a function that splits sentences into words, and strips punctuation marks (",", ";", etc.) from edges of words.


def to_words(sentance):
    words = sentance.split()
    stripped_words = []
    for word in words:
        stripped_words.append(word.strip(",;:()"))
    return stripped_words


# Use the last two functions in one that takes a filename as its argument and returns the text in the file as a list of lists. Test it on the file "data/sample_text.txt"


def process(f):
    out = []
    text = open(f).read()
    for sentance in text_to_sentances(text):
        words = to_words(sentance)
        out.append(words)
    return out



process("data/sample_text.txt")[0][:3]


# ### 4.1.2
# Use the functions defined in __4.1.1__ and define a function that goes through a text and replaces all proper names (capitalized words not at the beginning of a sentence) with "Joe". Print the first few sentences to test your solution.

def joefy(l):
    out = []
    for i in l:
        for j in i:
            if i.index(j) != 0 and j.istitle():
                out.append("Joe")
            else:
                out.append(j)
    return out


" ".join(joefy(process("data/sample_text.txt"))[:20])


# ### 4.1.3
# Load the sample text using your function from __4.1.1__ and create a game where the user is shown a half of a word in a small context (e.g. "_Many solu\*\*\*\*\* were suggested_") and has to guess the full word (don't worry about randomization, your solution can come up with the same questions every time).


def game(f):
    for i in process(f):
        for j in i:
            if i.index(j) == 4:
                word = i[4]
                print(word)
                print( word[:(len(word)-1)/2] + "*" * len(word[len(word)/2:]))
            else:
                print(j)
                
                
game("data/sample_text.txt")


# ## 4.2 Lists
# <a id='4.2'></a>

# ### 4.2.1
# Define a function that takes as its input a list of $n$ lists of $n$ numbers (a square matrix) and decides if it is symmetric (i.e. $A[i,j] == A[j,i]$ for all $i, j$).


m = [[11,22,33],
     [22,55,66],
     [33,66,99]]

def symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

symmetric(m)


# ### 4.2.2
# Define a function that takes a list containing lists of equal length (i.e. a table of size $n\times k$) and "transposes" it, creating a table of size $k\times n$.


m = [[1,2,3],
     [4,5,6]]

def transpose(matrix):
    out = []
    for i in range(len(matrix[0])):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i])
        out.append(line)
    return out



transpose(m)


# ### 4.2.3
# Redo 4.2.2 using nested list comprehension!


def nested_transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

nested_transpose(m)


# ### 4.2.4

# Define a function that takes a list and string, then returns all elements that start with the string, along with their indices in the list.

# In[212]:

def func(l,s):
    return [x for x in l if x.startswith(s)]

l = ["abc", "abd", "axf", "abt"]
func(l,"ab")


# ## 4.3 Dictionaries
# <a id='4.3'></a>

# ### 4.3.1
# Use a dictionary to count words in our sample text (use your text processing functions!). Then print the most common words, along with their frequencies!


d = {}
p = process("data/sample_text.txt")[0]
for i in p:
    if i in d:
        d[i] +=1
    else:
        d[i] = 0
        
sorted(d.items(), key=lambda x:x[1], reverse=True)


# ### 4.3.2

# Define function that performs the factorial operation ($n!$) but caches all results so that each call requires the least possible number of multiplications.


get_ipython().run_cell_magic(u'time', u'', u'def fact(n):\n    d = {}\n    for i in range(n):\n        if i == 0:\n            d[i] = 1\n        else:\n            d[i] = d[i-1]*i\n    return d[n-1]\n    \nfact(500)')


# ### 4.3.3
# Read the dataset in "data/movies.tsv" and store it in a dictionary whose keys are genres and the values are list of tuples of title and year


f = open("data/movies.tsv")
lines = []
d = {}
for i in f.read().split("\n"):
    words = []
    for j in i.split("\t"):
        words.append(j)
    lines.append(words)


for title, year, genre in lines[:-1]:
    if genre not in d:
        d[genre] = [(title, year)]
    else:
        
        d[genre].append([title,year]) 
#print(d)
f.close()



def process_data(fn):
    data = {}
    f = open(fn)
    for line in f:
        title, year, genres = line.strip().split("\t")
        title = title.strip()
        year = int(year)
        genres = genres.split(",")
        
        for genre in genres:
            if genre not in data:
                data[genre] = []
            data[genre].append((title, year))          
    return data



# In[284]:

data = process_data("data/movies.tsv")

data


# ### 4.3.4
# Process the movies dataset (the original file or the dictionary built in __4.3.3__) and build a dictionary that indexes movies by the first letter of the title. Then create a small interface for querying (using the input function)

# In[ ]:




# ### 4.3.5
# Build an incremental search of movie titles: users should be able to narrow the set of movies with every character they type. You may create deeply nested dictionaries beforehand or process the data on-the-fly.

# In[ ]:




# ## 4.4 The _collections_ module
# <a id='4.4'></a>

# ### 4.4.1
# Modify the word counter in __4.3.1__ so that it uses a defaultdict.

# In[ ]:




# ### 4.4.2
# Modify the word counter in __4.4.1__ so that it uses a Counter.

# In[ ]:




# ### 4.4.3
# Define a function that queries users for their last name, first name, year of birth, and hobby, and populates an OrderedDict whose keys are the last names and values are dictionaries with four keys each. If a second person with the same last name is encountered, both should now have keys of the form "lastname_firstname". If the same person is encountered multiple times, his/her data should be updated. Then test the solution of someone else and ask her to test yours.

# In[ ]:




# ### 4.4.4
# Convert the database built in __4.4.3__ into a list of namedtuples.

# In[ ]:



