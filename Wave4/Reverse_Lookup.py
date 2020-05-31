def reverseLookup(data, value):
  
  keys = []
  
  for key in data:
      if data[key] == value:
        keys.append(key)
 
  return keys

def main():

  esEn = {"el" : "the", "la" : "the", "hola" : "hello", "adiós" : "goodbye", "gracias" : "thank you"}

  # Returns multiple keys
  print("The spanish word for 'the' are: ", reverseLookup(esEn, "the"))
  print("Expected words:","El (for masculine) and La (for feminine)")
  print()
  # Returns one keys
  print("The spanish word for 'hello' is: ", reverseLookup(esEn, "hello"))
  print("Expected word:","Hola")
  print()
  print("The spanish word for 'goodbye' is: ", reverseLookup(esEn, "goodbye"))
  print("Expected word:","Adiós")
  print()
  print("The spanish word for 'thank you' is: ", reverseLookup(esEn, "thank you"))
  print("Expected word:", "Gracias")
  print()
  # Returns no keys
  print("The spanish word for 'fgsk' is: ", reverseLookup(esEn, "fgsk"))
  print("Expected word:", "Unkown")
  
if __name__ == "__main__":
  main()