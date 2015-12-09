from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
class Death(Scene):

	quips = [
		"You died.  You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "BOO!"
		return 'laser_weapon_armory'
		
class LaserWeaponArmory(Scene):

	def enter(self):
		print "BOO!"
		return 'the_bridge'
		
class TheBridge(Scene):
	
	def enter(self):
		print "BOO!"
		return 'escape_pod'
		
class EscapePod(Scene):
	
	def enter(self):
		print "BOO!"
		return 'death'
		

class Map(object):
	
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name) # .get('key') is a built-in function for dict'scene_map
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
	
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()	