# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.SupranationalWorld()

# set the title of map
worldmap.title = 'Continents'

# adding the continents
worldmap.add('Africa', ['africa'])
worldmap.add('North america', ['north_america'])
worldmap.add('Oceania', ['oceania'])
worldmap.add('South america', ['south_america'])
worldmap.add('Asia', ['asia'])
worldmap.add('Europe', ['europe'])
worldmap.add('Antarctica', ['antarctic'])

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")
