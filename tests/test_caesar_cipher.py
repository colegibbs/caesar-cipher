import pytest
from caesar_cipher.caesar_cipher import encrypt

def test_encrypt_all_alpha():
  actual = encrypt('message', 2)
  expected = 'oguucig'
  assert actual == expected

def test_encrypt_with_nonalpha():
  actual = encrypt()