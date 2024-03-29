import pytest
from caesar_cipher.caesar_cipher import encrypt, decrypt, crack


####### encrypt test #######


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


def test_encrypt_with_micro_Z():
  actual = encrypt('Z', 2)
  expected = 'B'
  assert actual == expected


####### decrypt test #######


def test_decrypt_sentence():
  actual = decrypt('Ymnx nx rd rjxxflj.', 5)
  expected = 'This is my message.'
  assert actual == expected


def test_decrypt_all_alpha():
  actual = decrypt('oguucig', 2)
  expected = 'message'
  assert actual == expected


def test_decrypt_with_nonalpha():
  actual = decrypt('rjxxflj$', 5)
  expected = 'message$'
  assert actual == expected


def test_decrypt_with_capital():
  actual = decrypt('Rjxxflj', 5)
  expected = 'Message'
  assert actual == expected


def test_decrypt_with_large_shift():
  actual = decrypt('oguucig', 29)
  expected = 'message'
  assert actual == expected


def test_decrypt_with_micro_B():
  actual = decrypt('B', 2)
  expected = 'Z'
  assert actual == expected


####### decrypt test #######


def test_crack_with_sentence():
  actual = crack('Ymnx nx rd rjxxflj.')
  expected = 'This is my message.'
  assert actual == expected


def test_crack_all_alpha():
  actual = crack('oguucig')
  expected = 'message'
  assert actual == expected


def test_crack_with_nonalpha():
  actual = crack('rjxxflj$')
  expected = 'message$'
  assert actual == expected


def test_crack_with_capital():
  actual = crack('Rjxxflj')
  expected = 'Message'
  assert actual == expected


def test_crack_with_large_shift():
  actual = crack('oguucig')
  expected = 'message'
  assert actual == expected

def test_required_crack():
  encrypted = encrypt("It was the best of times, it was the worst of times.", 6)
  actual = crack(encrypted)
  expected = "It was the best of times, it was the worst of times."
  assert actual == expected