from src.assign_table import assignTable


class dniProgram:

    def __init__(self, number):
        self.number = number

    # This function works to check if the number is valid to be able to get a letter or if we got a non
    # opreable value. We start a loop to check if each number inside the string is inside the string that
    # contains the value numbers in range from 0 to 10, if it's True we just still carring on with the loop.
    # Finally if all the numbers have been validated we check that the length of the string is the same that
    # the length of the numbers of an dni should have by checking the variable that is in assign_table. If it's
    # the same value we return True, if is not we return False

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

    # We check that the validation of the number of the dni is True and we can work with the value to get the
    # letter of the dni. We get the letter by the position of it in the list and we get the position with the
    # rest of the division of the number between twenty three. In case the validation has got a False result we
    # give back a False too

    def get_letter(self):
        if self.dni_validation() == True:
            letter_position = int(self.number) % 23
            return assignTable.table[letter_position]
        else:
            return False

    # This function works to return a valid dni. We just need to check that the routine of get_letter did'nt
    # return False, this means that has been a valid value and we just return the string number plus the letter
    # that we got from the function get_letter and we get a valid dni, in the opposite case we display a
    # message in the screen asking to try again to insert the number

    def get_dni(self):
        if self.get_letter() != False:
            return str(self.number) + str(self.get_letter())
        return 'Try again please !'
