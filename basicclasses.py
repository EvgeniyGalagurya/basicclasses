class Car():
    '''We describe the brand, model, year of manufacture and price of the purchased car'''
    def __init__(self, mark, model, year, coast):
        self.mark = mark
        self.model = model
        self.year = year
        self.coast = coast

    def __str__(self):
        return f'You bought a car {self.mark} {self.model} {self.year} year of graduation for {self.coast} ' \
               f'conditional units.'
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'Car ({self.mark}, {self.model}, {self.year}, {self.coast})'
        '''More algorithmic code'''
        #return f'{self.__class__.__name__} ({self.mark}, {self.model}, {self.year}, {self.coast})'


class Owner(Car):
    '''We describe the brand, model, year of manufacture and price of the purchased car and name the owner'''
    def __init__(self, owner, mark, model, year, coast):
        super().__init__(mark, model, year, coast)
        self._owner = owner

    @property
    def owner(self):
        '''We prohibit changing the owner'''
        return self._owner

    def show_info(self):
        '''We display information about the owner and the car'''
        info = f'{self.owner} became the owner of the car {self.mark} {self.model} {self.year}' \
               f' year of production at cost {self.coast} conventional units.'
        print(info)


class Renovate(Owner):
    '''We describe the car, name its owner and describe the existing defect that needs to be repaired.
The restoration price is still fixed.'''
    def __init__(self, renovate,owner, mark, model, year, coast):
        super().__init__(owner, mark, model, year, coast)
        self.renovate = renovate
        self.price = 1500


    def show_info(self):
        '''We display information for the owner of the damaged car, with the final price of the car after repair.'''
        info = f'Mr {self.owner}, You bought a car {self.mark} {self.model} {self.year} year of production at cost ' \
               f'{self.coast} conditional units with damage {self.renovate}. The cost of restoration works is ' \
               f'{self.price} conventional units. The final cost of the car after restoration is ' \
               f'{self.coast + self.price} conventional units.'
        print(info)

if __name__ == '__main__':
    ...




