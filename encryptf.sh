#!/bin/bash
echo "Welcome, I am ready to encrypt a file/folder for you"
echo "currently I have a limitation, Place me to thh same folder, where a file to be 
encrypted is present"
echo "Enter the Exact File Name with extension"
read file;
gpg -c $file
echo "I have encrypted the file successfully..."
echo "Now I will be removing the original file"
rm -rf $file

#Note: gpg -d filename.gpg > filename is what you need to implement in your decryption script. 
#You may post you script in comment if successful, if not you may ask me to write it for you.
#gpg -c : This will encrypt your file, using a passkey aka password.