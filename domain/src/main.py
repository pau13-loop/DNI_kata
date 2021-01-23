class Dni():

    def __init__(self, number):
        self.number = number
        # Allowed dni numbers
        self.valid_numbers = '0123456789'
        # Length of the numbers of the Dni without a letter
        self.length_numbers_dni = 8
        # Length of the numbers of the Dni with a letter
        self.length_dni = 9
        # Table with the allowed characters for the Dni
        self.allocation_table = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D',
                             'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    def set_dni(self):
        if Dni.validate_dni_number(self) != True:
            return 'Try again please !'
        letter = AllocationTable.get_nif_letter(self)
        return self.number + letter

    def validate_dni_number(self):
        for num in self.number:
            if num in self.valid_numbers:
                continue
            else:
                return False
        if len(self.number) == self.length_numbers_dni:
            return True
        else:
            return False


class AllocationTable(Dni):

    def __init__(self, number):
        Dni.__init__(self, number)

    def get_nif_letter(self):
        letter_position = int(self.number) % 23
        letter = self.allocation_table[letter_position]
        return letter
