# import pygal Library
import pygal
import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
# Create a World Map
worldmap = pygal.maps.world.World()
# Set The Title of the Map
worldmap.title = 'Countries'
# Adding The Countries
worldmap.add('Random Data', {
        'aq': 10,
        'cd': 30,
        'de': 40,
        'eg': 50,
        'ga': 45,
        'hk': 23,
        'in': 70,
        'jp': 54,
        'nz': 41,
        'kz': 32,
        'us': 66
})
# Save Into The File
worldmap.render_to_file('abc.svg')

print("Success")
