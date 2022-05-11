# from corpus_import import word_list, name_list

def encrypt(text, shift):
  shift = shift % 27
  encrypted_text = ""
  for letter in text:
    if letter.isalpha():
      char_num = ord(letter)
      if letter.isupper() and (char_num + shift) > 90:
        char_num = ((char_num + shift) - 91) + 65
        encrypted_char = chr(char_num)
      elif letter.islower() and (char_num + shift) > 122:
        char_num = ((char_num + shift) - 123) + 97
        encrypted_char = chr(char_num)
      else:
        encrypted_char = chr(char_num + shift)
      encrypted_text += encrypted_char
    else:
      encrypted_text += letter
  return encrypted_text

  def decrypt(encrypted_text, key):
    encrypt(encrypted_text, -key)

