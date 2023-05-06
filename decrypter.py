import matplotlib.pyplot as plt
import numpy as np
import string
import re
import json

class Decrypter:
  def __init__(self):
    self.__letter_frequencies = self.__read_json('./letter_frequencies.json')
    self.__alphabet = string.ascii_uppercase

  def get_key(self, cipher, language):
    sanitized_cipher = re.sub(r'\W+', '', cipher).upper()
    cipher_len = len(cipher)

    key_size = self.__get_key_size(sanitized_cipher)
    closets = self.__create_closets_matrix(sanitized_cipher, key_size)
    idx_of_frequencies = self._generate_idx_of_frequencies(closets)
    alphabet_idx_of_frequencies = [float(s) / 100 for s in list(self.__letter_frequencies[language].values()) ]

    key = self.__frequency_analysis(idx_of_frequencies, alphabet_idx_of_frequencies)
    key = self.__find_repeated_substring(key)

    return key

  # Private methods 

  def __frequency_analysis(self, idx_of_frequencies, alphabet_idx_of_frequencies):
    key_shift_values = []
    max_dot_product = -1
    nb_of_shifts = 0

    for i in range(0, len(idx_of_frequencies)):
      # For each closet, get the index of frequencies and calculate the dot product with the alphabet index of frequencies
      closet_idx_of_freq = list(idx_of_frequencies[i].values())

      for j in range(0, len(alphabet_idx_of_frequencies)):
        curr_shift_dot_prod = np.dot(alphabet_idx_of_frequencies, closet_idx_of_freq)
        # Shift array to the right
        closet_idx_of_freq = closet_idx_of_freq[1:] + [closet_idx_of_freq[0]]

        if curr_shift_dot_prod > max_dot_product:
          max_dot_product = curr_shift_dot_prod
          nb_of_shifts = j
      
      key_shift_values.append(nb_of_shifts)
      max_dot_product = -1
      nb_of_shifts = 0

    return ''.join([self.__alphabet[i] for i in key_shift_values])

  def __create_closets_matrix(self, cipher, offset):
    result = []
    for i in range(offset):
        result.append([cipher[j] for j in range(i, len(cipher), offset)])
    return result

  def _generate_idx_of_frequencies(self, closets):
    key_size = len(closets)
    result = [{}] * key_size
    alphabet_size = len(self.__alphabet)
    idx_of_frequencies = {}
    
    for j in range(0, key_size):
      for i in range(0, alphabet_size):
        curr_letter = self.__alphabet[i]
        idx_of_frequencies[curr_letter] = (closets[j].count(curr_letter)) / len(closets[j])
      result[j] = idx_of_frequencies
      idx_of_frequencies = {}

    return result

  def __get_key_size(self, cipher):
    # Estimate key length based on index of coincidence method.
    cipher_len = len(cipher)
    max_key_size = min(cipher_len, 20)
    key_size_matchings = [0] * max_key_size
    left = ""
    right = ""
    matches = []
  
    for i in range(1, cipher_len):
      left = cipher[i:cipher_len]
      right = cipher[0:cipher_len-i]
      matches.append(self.__count_matches(left, right))
    
    first_cluster = matches[0:max_key_size]
    local_max = sorted(first_cluster, reverse=True)[0]
    key_size = first_cluster.index(local_max) + 1

    return key_size
    
  def __count_matches(self, str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i].isalpha() and str1[i].upper() == str2[i].upper():
          count += 1
    return count

  def __read_json(self, file_name):
    with open(file_name, 'r') as f:
      return json.load(f)
  def __find_repeated_substring(self, s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return s[:i]
    return s
