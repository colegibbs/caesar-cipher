import pytest
from caesar_cipher.caesar_cipher import encrypt

def test_encrypt_all_alpha():
  actual = encrypt('message', 2)
  expected = 'oguucig'
  assert actual == expected

def test_encrypt_with_nonalpha():
  actual = encrypt('message$', 5)
  expected = 'rjxxflj$'
  assert actual == expected

def test_encrypt_with_capital():
  actual = encrypt('Message', 5)
  expected = 'Rjxxflj'
  assert actual == expected

def test_encrypt_with_large_shift():
  actual = encrypt('message', 29)
  expected = 'oguucig'
  assert actual == expected

def test_encrypt_with_sentence():
  actual = encrypt('This is my message.', 5)
  expected = 'Ymnx nx rd rjxxflj.'
  assert actual == expected