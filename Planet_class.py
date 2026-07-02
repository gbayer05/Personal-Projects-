#Gentry Bayer 
# 7/1/2026 
# This was a lab activity from the workshop in freecode camp. This is another user friendly and beginner project. 
#This demonstrates classes and how they work. 
class Planet:
    def __init__(self, name, planet_type, star):
        # Check that all arguments are strings
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        # Check that none of the strings are empty
        if name == '' or planet_type == '' or star == '':
            raise ValueError('name, planet_type, and star must be non-empty strings')

        # Assign attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star
#Methods returning f string statements. 
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}....'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


# Create three Planet objects
planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Mars', 'Terrestrial', 'Sun')
planet_3 = Planet('Jupiter', 'Gas Giant', 'Sun')

# Print the planets
print(planet_1)
print(planet_2)
print(planet_3)

# Print the orbit messages
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
