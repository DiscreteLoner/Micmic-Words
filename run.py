"""
Codecademy Pro
Learn Python
Final Project
Markov Chain Text Generator
28 October 2018
"""

"""
import necessary code (including fetch_data module and 
a slightly modified Codecademy Markov Chain generator module)
"""
import fetch_data
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

# link to work reference
books_catalog = {
"Dead Men Tell No Tale" : "https://www.gutenberg.org/files/1703/1703-h/1703-h.htm", 
"No Hero" : "https://www.gutenberg.org/files/11153/11153-h/11153-h.htm"
}

print ("Hello, welcome to E. W. Hornung quote generator.")

num_quote = ""
book = ""

while book != "A" and book != "B":
  print ("")
  print ("Which book do you want to micmic?")
  print ("A = Dead Men Tell No Tale")
  print ("B = No Hero")
  book = raw_input("I choose: ")

while num_quote != "1" and num_quote != "2" and num_quote != "3" and num_quote != "4" and num_quote != "5":
  print ("")
  print ("How many passages would you like to generate(1-5)")
  num_quote = raw_input("?: ")

num_quote = int(num_quote)

length = 0
while length < 3 or length > 100: 
  try:	
    print ("")
    print ("Words per passage (minimum of 3, maximum of 100):")
    length = raw_input("?: ")
    length = int(length)
  except ValueError:
    print ("")
    print ("Sorry, that's not a valid length.")
    print ("")
    print ("Please, try again!")
    length = 0

print ("")
print ("Accessing works... ")
for link in books_catalog:
  if book == "A":
    print ("Dead Men Tell No Tale")
    mc.add_string(fetch_data.fetch_web_data("https://www.gutenberg.org/files/1703/1703-h/1703-h.htm"))
  else:
    print ("No Hero")
    mc.add_string(fetch_data.fetch_web_data("https://www.gutenberg.org/files/11153/11153-h/11153-h.htm"))

"""
generate text from the Markov Chain and 
convert output to the required format
"""
for current in range(num_quote):
  while True:
    try:
      temporary = mc.generate_text(length)
      formatted = " ".join(temporary)
      print ("Passage #" + str(current+1) + ": " + formatted)
      print
      break
    except UnicodeEncodeError:
      pass