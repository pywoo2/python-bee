"""
Write a function that implements the Caesar cipher encryption and decryption.

The Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of positions down the alphabet. For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.

Your task is to implement two functions:

1. caesar_encrypt(text, shift):
   - This function should take a string 'text' and an integer 'shift' as input.
   - It should return the encrypted text where each letter is shifted 'shift' positions down the alphabet.
   - The function should preserve the case of the original text.
   - Non-alphabetic characters should remain unchanged.

2. caesar_decrypt(encrypted_text, shift):
   - This function should take an encrypted string 'encrypted_text' and an integer 'shift' as input.
   - It should return the decrypted text by shifting each letter back by 'shift' positions.
   - The function should preserve the case of the encrypted text.
   - Non-alphabetic characters should remain unchanged.

Example:
Input: text = "Hello, World!", shift = 3
Encrypted: "Khoor, Zruog!"
Decrypted: "Hello, World!"

Note:
- The shift value can be any integer (positive, negative, or zero).
- If the shift moves past 'Z' or 'z', it should wrap around to the beginning of the alphabet.
- Your implementation should handle uppercase and lowercase letters separately.
- Assume that the input will always be a string for the text and an integer for the shift.

"""