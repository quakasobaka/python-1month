class DelNull:
    def __init__(self, firstnumber, secondnumber):
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber

    @staticmethod
    def devidenull(firstnumber, secondnumber):
        try:
            return(firstnumber / secondnumber)
        except:
            return (f'Деление на ноль невозможно')

div = DelNull(100, 5)
print(DelNull.devidenull(10, 0))
print(DelNull.devidenull(100, 0.001))