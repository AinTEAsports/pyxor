import os
import hashlib
from dataclasses import dataclass


@dataclass(frozen=True)
class File:
    __filename : str
    
    def __post_init__(self) -> None :
        if not os.path.exists(self.__filename) or not os.path.isfile(self.__filename):
            raise FileNotFoundError(f"file '{self.__filename}' not found")

    
    def __is_encrypted(self) -> bool :
        try:
            with open(self.__filename, 'r', encoding="utf-8") as f:
                f.read()
            return False
        except UnicodeDecodeError:
            return True
        
    
    def __get_decrypted_filename(self) -> str :
        encrypted_filename = f"{self.__filename}.xor"

    
    def xor_crypt(self, password : str, output_name : str = "", replace_file : bool = True) -> None :
        if not output_name:
            if replace_file:
                output_name = self.__filename
            else:
                output_name = f"{self.__filename}.copy"

        
        hashed_password = hashlib.sha256(password.encode('utf-8')).digest()
        
        with open(self.__filename, 'rb') as f:
            with open(f"{self.__filename}.copy", 'wb') as f2:
                i = 0

                while f.peek():
                    c = ord(f.read(1))
                    j = i % len(hashed_password)
                    b = bytes([c^hashed_password[j]])
                    f2.write(b)

                    i += 1

        os.remove(self.__filename)
        os.rename(f"{self.__filename}.copy", output_name)


    def get_filename(self) -> str :
        return self.__filename



if __name__ == "__main__":
    print("Do you know the difference between a dog and your mom ? No ?")
    print("Bro WTF you don't know the difference between your mom and a dog, go apologize to her NOW")
