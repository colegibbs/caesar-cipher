# from corpus_import import word_list, name_list

def encrypt(text, shift):
  shift = shift % 27
  words = text.split()
  encrypted_text = ""
  for word in words:
    for letter in word:
      if word.isalpha():
        char_num = ord(letter)
        encrypted_char = chr(char_num + shift)
        encrypted_text += encrypted_char
      else:
        encrypted_text += letter
  return encrypted_text
