#include <iostream>
#include <string>
#include <cstring>

int get_index(std::string text, char character){
  for (int i=0; i<text.length(); i++){
    if (text[i] == character){
      return i;
    }
  }
  return -1;
}

int main(int argc, char *argv[]){
  std::string text = "hello world"; 

  
  const std::string plain_text = "abcdefghijklmnopqrstuvwxyz";
  std::string substitution_cyphers[text.length()] = {"abcdefghijklmnopqrstuvwxyz"};
  std::string substitution_cipher = plain_text;
  std::string ciphertext = text;

  // Creating multiple substitution cyphers
  for (int i=0; i<text.length(); i++){     // Create substitution cipher
    // ------------------------------------
    // Creating a new index to place character
    for (int index=0; index<plain_text.length(); index++){
      int new_index = index - 3;
      if (new_index < 0){ // Making sure index is inside string
        new_index = new_index + plain_text.length();
      }
      
      substitution_cipher[new_index] = substitution_cyphers[i][index];
    }
    substitution_cyphers[i+1] = substitution_cipher; // Adding cipher to array
  }

  // Encrypting string
  for (int i=0; i<text.length(); i++){ // looping through each character in text
    char new_char = text[i]; // getting current character
    int character_index = get_index(substitution_cyphers[0], text[i]); // starting character index at first substitution cipher

    for (int j=0; j<i+1; j++){ // Looping through ciphers
      new_char = substitution_cyphers[j+1][character_index]; // getting what the new character
      int character_index = get_index(substitution_cyphers[j+1], new_char); // changing the index to the new substitution cipher
    }
    ciphertext[i] = new_char;
  }

  std::cout << "Original: " << text << std::endl;
  std::cout << "Ciphertext: " << ciphertext << std::endl;
  return 0;
}
