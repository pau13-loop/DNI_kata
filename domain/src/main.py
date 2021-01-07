from src.assign_table import assignTable


class dniProgram():

    def __init__(self, number):
        self.number = number

    def dni_validation(self):
        for num in self.number:
            if num in assignTable.number:
                continue
            else:
                return False
        if len(self.number) == assignTable.length_numbers_dni:
            return True
        else:
            return False

    def get_letter(self):
        if self.dni_validation() == True:
            letter_position = int(self.number) % 23
            return assignTable.table[letter_position]
        else:
            return False

    def get_dni(self):
        if self.get_letter() != False:
            return str(self.number) + str(self.get_letter())
        return 'Try again please !'
