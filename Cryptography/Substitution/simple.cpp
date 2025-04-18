#include <iostream>
#include <string>

/*
 * Substitute one value for another, for exmaple replacing one letter in
 * the alphabet for one 3 letters down. e.g A -> D
 * This is going to be a simple version using the exmaple given above
*/

int main(int argc, char **argv){
	std::string text = "Hello, World!";

	char new_char;
	char final_cipher_text[text.length()];

	for (int i=0; i<text.length(); i++){ // Looping through each character in string
		new_char = (char)(text[i]+3); // Adding 3 to the ascii value of the character
		final_cipher_text[i] = new_char;	
	}
	
	std::cout << "Original text: " << text << std::endl;
	std::cout << "Ciphertext: " << final_cipher_text << std::endl;

	return 0;
}
