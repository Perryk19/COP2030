def histogram(fin):
  hist = dict()
  # Read every line in fin
  for line in fin:
    # Split() the line into a list of words and convert words to lower case
    words = line.lower().split()
    # Process every word in the list
    for word in words:
      freq = hist.get(word, None)
      # Check if each word is in the dictionary
      if freq == None:
        hist[word] = 1
      # If not, add it
      else:
        hist[word] = freq + 1
  return hist


def printHistogram(hist):
  print("Word Count")
  print("----------------")
  for word in hist:
    print(f"{word:<12}{hist[word]:2d}")
fin = open("Myra.txt")
print('Reading file Myra.txt...')

hist = histogram(fin)
printHistogram(hist)
