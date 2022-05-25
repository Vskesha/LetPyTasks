class Card:
    def __init__(self, number, holder, valid_date, ccv):
        self.number = str(number)
        self.holder = str(holder)
        self.valid_date = str(valid_date)
        self.ccv = str(ccv)
        
    def get_hidden_number(self):
        return self.number[0:2] + '** **** **** ' + self.number[-4:]
        
class MasterCard(Card):
    def __str__(self):
        return f'[mastercard {self.get_hidden_number()}]'
        
class Visa(Card):
    def __str__(self):
        return f'[visa {self.get_hidden_number()}]'
        
visa = Visa(4200000000000001, 'Vs Kesha', '05/22', 345)
master = MasterCard(1234567890123456, 'Katya K', '06/23', 512)
print(visa)
print(master)