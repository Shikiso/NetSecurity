#include <iostream>
#include <bitset>
#include <string>

int main(int argc, char *argv[]){
  std::string text = "cat";  

  std::bitset<8> x = std::bitset<8>(text[1]);

  std::string binary;
  
  int key_position = 0;
  for (int i = 0; i < text.length(); i++){
    std::bitset<8> text_binary = std::bitset<8>(text[i]);
    std::bitset<8> key_binary = std::bitset<8>('V');
  
    std::bitset<8> final_binary;
    for (int j=0; j<8; j++){
      if (text_binary[j] == 1 || key_binary[j] == 1){
        final_binary[j] = 1;
      }
      else{
        final_binary[j] = 0;
      }
    }
    binary = binary + final_binary.to_string() + " ";
  }

  // The binary will be sent and decoded using the same key
  std::cout << "Message: " << text << std::endl;
  std::cout << "Encoded binary: " << binary << std::endl;
  
  return 0;
}
