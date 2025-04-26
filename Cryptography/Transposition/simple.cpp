#include <iostream>
#include <string>

int main(int agrc, char *argv[]){
  // For this example im using a string with 8 bytes to make the code easier
  std::string text = "hello123";

  // New index positions for each character in string
  // So index char at index 0 will become char at index 4 
  int key_pattern[8] = {4,8,1,5,7,2,6,3};

  std::string ciphertext = text;
  for (int i=0; i<text.length(); i++){
    ciphertext[i] = text[key_pattern[i]-1];
  }
  
  std::cout << "Original: " << text << std::endl;
  std::cout << "Cipher text: " << ciphertext << std::endl;

  return 0;
}
