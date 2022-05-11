from caesar_cipher.corpus_import import word_list, name_list

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
  return encrypt(encrypted_text, -(key + 1))


def crack(encrypted_text):
  possible_decrypted = []
  for i in range(26):
    possible_decrypted.append(decrypt(encrypted_text, i))
  
  for possibility in possible_decrypted:
    word_count = 0
    words = possibility.split()
    for word in words:
      if word.isalpha():
        if word.lower() in word_list or word.lower() in name_list:
          word_count += 1
      else:
        alpha_word = ''
        for letter in word:
          if letter.isalpha():
            alpha_word += letter
        if alpha_word.lower() in word_list or alpha_word.lower() in name_list:
          word_count += 1
    if ((word_count / len(words)) * 100) >= 50:
      return possibility

print(crack('Rjxxflj'))