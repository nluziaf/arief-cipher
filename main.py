class AriefCipher:
    vowels = ["a", "e", "i", "o", "u"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
                  "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    def encode(self, string: str):
        string = string.casefold()
        string_array = [char for char in string]
        processed_array = []

        for char in string_array:
            if char in self.vowels:
                processed_array.append(self.vowels[(self.vowels.index(char)+1) % 5])
            elif char in self.consonants:
                processed_array.append(self.consonants[(self.consonants.index(char)+1) % 21])
            else:
                processed_array.append(char)

        return "".join(processed_array).upper()

    def decode(self, string: str):
        string = string.casefold()
        string_array = [char for char in string]
        processed_array = []

        for char in string_array:
            if char in self.vowels:
                processed_array.append(self.vowels[(self.vowels.index(char) - 1) % 5])
            elif char in self.consonants:
                processed_array.append(self.consonants[(self.consonants.index(char) - 1) % 21])
            else:
                processed_array.append(char)

        return "".join(processed_array).upper()


select_operation = input("Encode (e) or Decode (d)? :")
if select_operation == "d":
    any_string = input("Insert any string you would like to decode:")
    name = AriefCipher().decode(any_string)
else:
    any_string = input("Insert any string you would like to encode:")
    name = AriefCipher().encode(any_string)

print(name)
