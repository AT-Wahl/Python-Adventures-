from sys import exit
from textwrap import dedent
import os

	
class User(object):
		
	def __init__(self, name):
		self.name = name
		self.items = []
		self.eyesight = False
	
	def display_items(self):
		if len(self.items) > 0:
			print("Here are your items:")
			for item in self.items:
				print (str(item))
		else:
			print("You have no items")
		print("")
	
	def add_item(self, item):
		self.items.append(item)

class Room(object):

	map_drawing = [
	" ____________________________________________________________ ",
	"|        |  FIREPLACE   |                                    |",
	"|        |______________|                                 \   ",
	"|                                           MAIN ENTRANCE  \  ",
	"|_____                                ______            ____\ ",
	"|     |                              |      |          |     |",
	"|     |                              |      |          |     |",
	"|     |                              |      |          |     |",
	"|BIG  |                              |      |          |     |",
	"|SOFA |       LIVING ROOM            |      |          |     |",
	"|     |                              |      |          |     |",
	"|     |                              |      | KITCHEN  |     |",
	"|     |                              |      |          |     |",
	"|_____|                              |      |          |     |",
	"|             ___________            |      |          |     |",
	"|            | LIL SOFA  |           |      |          |     |",
	"   /         |___________|           |______|          |     |",
	"  /                                                    |     |",
	" /                                            /      \ |     |",
	"/________________________             _______/        \|_____|",
	"|                       /            |                       |",
	"|                      /             |         PANTRY        |",
	"|                     /              |                       |",
	"|                    /               |_______________________|",
	"|                        |           |                       |",
	"|                        |           |                       |",
	"|    ODIN'S LAIR         |           |                       |",
	"|                        |   MAIN    |        BATHROOM       |",
	"|                        |  HALLWAY     /                    |",
	"|                        |             /                     |",
	"|                        |            /                      |",
	"|________________________|           /_______________________|",
	"|                       /            \                       |",
	"|                      /              \                      |",
	"|                     /                \                     |",
	"|                    /                  \                    |",
	"|                        |           |                       |",
	"|                        |           |                       |",
	"|       OFFICE           |           |      QUITO'S LAIR     |",
	"|                        |           |                       |",
	"|                        |           |                       |",
	"|                        |           |                       |",
	"|                        |           |                       |",
	"|________________________|___________|_______________________|",
	]

	def __init__(self):
		#self.items = []
		#self.actions = []
		pass
	
	def enter(self):
		pass
		
	def display_actions(self, action_list):
		print('1. Display Map')
		print('2. Show Items')
		for item in action_list:
			print(str(item))
	
	def input_error(self):
		print('Input not understood. Please input a number. Only a number. Nothing else. This is a very basic program\n')
	
	def print_map(self):
		for line in Room.map_drawing:
			print(line)
		
	def take_item(self, item_list, item):
		position = item_list.index(item)
		item_list.pop(position)
		return item_list
	
	def death(self, reason):
		deaths= {
			'fear': dedent("""
			You run away in fear and leave with your life. 
			Probably a smart choice, though you always wonder if you could have done more...
			"""),
			'fireplace': dedent("""
			You light the fireplace, which hasn\'t been cleaned in years. 
			Smoke fills the room and you suffocate. Oof
			"""),
			'fridge': dedent("""
			You go to open the fridge again, but without the carrots to counterbalance its weight, 
			you end up accidentally pulling it on top of you. You are crushed, literally and figuratively.
			"""),
			'toilet': dedent("""
			You drink the toilet water. It is incredibly gross. 
			I have no idea why you did that, you weren\'t even thirsty. 
			You die instantaneously.
			"""),
			'quito_attack': dedent("""
			You attack the beast with no weapons. This seems like a bad idea.
			Although he weighs only 2 lbs he makes quick work of you with sharp claws and an insatiable bloodlust.
			Better luck next time
			"""),
			'quito_attack_knife': dedent("""
			You reach into your items and pull out your knife. It is sharp.
			You lunge at the beast and make contact! 
			Looking closer however you see you actually see you ended up stabbing a pillow.
			Before you can take your knife you the 2 lb monster claws you to ribbons.
			Better luck next time.
			"""),
			'placate_no_items': dedent("""
			You decide the best way to deal with the monster is listening to the wise beast's advice
			Instead of violence, you choose a more peaceful option.
			You whistle at the monster and try to give him some belly scratches.
			The beast doesn't seem to enjoy this much. He's seems more hungry than anything.
			Before you realize somethings wrong, the 2 lb monster feast upon your flesh for sustinance.
			This does not work out well for you.
			Better luck next time.
			"""),
			'placate_one_item': dedent("""
			You decide the best way to deal with the monster is listening to the wise beast's advice
			Instead of violence, you choose a more peaceful option.
			You've acquired some items in your journey and pull them out, hoping the beast will appreciate them.
			However, you don't have enough items of interest to keep his attention.
			He gets bored quickly, and decides he's hungry. For you.
			Better luck next time.
			""")
		}
		death = deaths.get(reason)
		print(death)		
		exit(1)
	
	def victory(self):
		print(dedent("""
		You decide the best way to deal with the monster is listening to the wise beast's advice
		Instead of violence, you choose a more peaceful option.
		You've acquired some items in your journey and pull them out, hoping the beast will appreciate them.
		With the ball of yarn, tuna, and catnip, you create the most enticing toy anyone has ever seen.
		The beast appreciates this. No one's been this nice to him in a long time.
		He begins to purr. 
		Strangely enough, the lights start to turn back on.
		You look outside and see the clouds start to dissapear. Birds start to sing.
		You've done it. You've cleared the evil. Congrats
		"""))
		print(dedent("""
		___          ___  __   ________   __________   _______   ________  ___    ___
		\  \        /  / |  | |   _____| |___    ___| |  ___  | |   __   | \  \  /  /
		 \  \      /  /  |  | |  |           |  |     | |   | | |  |__|  |  \  \/  / 
		  \  \    /  /   |  | |  |           |  |     | |   | | |   _   _|   \    /  
		   \  \  /  /    |  | |  |           |  |     | |   | | |  | \  \     |  |   
		    \  \/  /     |  | |  |_____      |  |     | |___| | |  |  \  \    |  |   
		     \____/      |__| |________|     |__|     |_______| |__|   \__\   |__|    
			 """))
		exit(1)

class MainEntrance(Room):
	
	enter_counter = 0
	items = []
	actions =['3. Go to the living room', '4. Go to the kitchen', '5. Run away']
	
	def enter(self, user):
		
		if MainEntrance.enter_counter == 0:
		
			print(dedent("""
			You enter the House of Doom. There is little light in the house, and some rooms are not lit at all.
			Strangely enough it was sunny today, but as you look outside the door before closing it behind you, 
			you now notice clouds have filled the afternoon sky. Every fiber of your being tells you to leave this place,
			but instead you close the door behind you and proceed.
			Your quest here is to find the terror that has taken over the house and do whatever must be done to rid the house of evil.
			Good luck
			"""))
		
			MainEntrance.enter_counter += 1
			
		print("You are in the main entrance room. What would you like to do?\n")
		self.display_actions(MainEntrance.actions)
		
		action = input(">")
		os.system('cls')
		
		if action == "1":
		
			self.print_map()
			
			return 'main_entrance'

		elif action == "2": 
		
			user.display_items()
			
			return 'main_entrance'
			
		elif action == "3":
			
			return 'living_room'
			
		if action == "4":
		
			return 'kitchen'
			
		if action == "5":
			
			self.death('fear')
	
		else:
			self.input_error()
			
			return 'main_entrance'
	
class LivingRoom(Room):

	enter_counter = 0
	items = ['catnip']
	actions = ['3. Go to the kitchen', '4. Go to the main hallway', '5. Light the fireplace', '6. Search the sofas']

	def enter(self, user):

		if LivingRoom.enter_counter == 0:
		
			print(dedent("""
			You enter the living room. Based on the stories you've heard about this place , it would be more appropriate to call it the \"dying room\". Heh.
			You look around you and see a very dirty Fireplace and two sofas. It smells like it hasn't been cleaned in here for quite some time, and based on 
			what you know about the previous residents, that doesn't really surprise you.
			"""))
			LivingRoom.enter_counter += 1
		
		print("You are in the living room. What would you like to do?\n")
		self.display_actions(LivingRoom.actions)
		
		action = input(">")
		os.system('cls')
		
		if action == "1":
		
			self.print_map()
			
			return 'living_room'

		elif action == "2": 
		
			user.display_items()
			
			return 'living_room'
			
		elif action == "3":
		
			return 'kitchen'

		elif action == "4": 
		
			return 'main_hallway'		
	
		elif action == "5":
		
			self.death('fireplace')
	
		elif action == "6":
			
			try: 
			
				self.take_item(LivingRoom.items, 'catnip')
				
				print(dedent("""
				You've found a strange bag of green leaves. Oregeno perhaps?
				No, doesn't quite match the smell...
				You add it to your inventory
				"""))
				user.add_item('catnip')
				return 'living_room'		
			
			except:
			
				print("There doesn't seem to be anything else here\n")
				
				return 'living_room'
			
		else:	
			self.input_error()
			
			return 'living_room'

class Kitchen(Room):

	carrot_counter = 0
	enter_counter = 0
	items = ['key']
	actions = ['3. Go to the living room', '4. Go to the main hallway', '5. Check the pantry', '6. Open the fridge']

	def enter(self, user):

		if Kitchen.enter_counter == 0:
		
			print(dedent("""
			You walk into the kitchen and see the usual kitchen appliances, but not in their usual places. 
			The appliances are demolished and pieces are scattered everywhere... what in God's name happened here?
			You do however notice the fridge still seems intact and running, along with a some items in the pantry
			"""))
			Kitchen.enter_counter += 1
		
		print("You are in the kitchen. What would you like to do?\n")
		self.display_actions(Kitchen.actions)
		
		action = input(">")
		os.system('cls')

		if action == "1":
		
			self.print_map()
			
			return 'kitchen'

		elif action == "2": 
		
			user.display_items()
			
			return 'kitchen'
			
		elif action == "3":
		
			return 'living_room'
		
		elif action == "4":
		
			return 'main_hallway'
			
		elif action == "5":
		
			try:
				self.take_item(Kitchen.items, 'key')
				
				print(dedent("""
				You search around the pantry and don't find much, especially not any food.
				You do however see a key. You're sure this will come in handy.
				You add it to your inventory.
				"""))
				user.add_item('key')
				
				return 'kitchen'
		
			except:
				
				print("There's nothing left in the pantry for you. Stop checking it you weirdo.\n")
				
				return 'kitchen'
		
		elif action == '6':
			
			if Kitchen.carrot_counter == 0:
				
				print(dedent("""
				There isn't anything in the fridge besides a bag of carrots. 
				You take the carrots out and place them on the counter.
				The fridge shakes a little when you close it. I wonder why...
				"""))
				
				Kitchen.carrot_counter += 1
				
				Kitchen.actions.append('7. Eat the carrots')
				return 'kitchen'
				
			else:
				
				self.death('fridge')
				
		elif action == '7' and len(Kitchen.actions) == 5:
		
			print(dedent("""
			You feast on the carrots. Amazingly your eyesight improves dramatically.
			You start seeing better in the dark than you have ever been able to.
			"""))
			
			user.eyesight = True
			Kitchen.actions.pop(-1)
			return 'kitchen'			
		
		else:
			self.input_error()
			
			return 'kitchen'			
		
class MainHallway(Room):

	enter_counter = 0
	items = []
	actions = ['3. Go to the kitchen', '4. Go to the living room', '5. Go to Odin\'s lair', '6. Go to the bathroom', '7. Go to the office', '8. Go to Quito\'s lair']

	def enter(self, user):
	
		if MainHallway.enter_counter == 0:
		
			print(dedent("""
			You travel to the main hallway. It's fairly dark in here, 
			but you're able to make out 4 distinct doors. 
			"""))
			MainHallway.enter_counter += 1
		
		print("You are in the main hallway. What would you like to do?\n")
		self.display_actions(MainHallway.actions)
		
		action = input(">")
		os.system('cls')
		
		if action == "1":
		
			self.print_map()
			
			return 'main_hallway'

		elif action == "2": 
		
			user.display_items()
			
			return 'main_hallway'
			
		elif action == "3":
            
			return 'kitchen'
			
		elif action == "4":
		
			return 'living_room'
			
		elif action == "5":
		
			return 'odins_lair'

		elif action == "6":
			
			return 'bathroom'
			
		elif action == "7":
		
			return 'office'
            
		elif action == "8":
		
			return 'quitos_lair'
			
		else:
			self.input_error()
			return 'main_hallway'

class Bathroom(Room):
	
	enter_counter = 0
	items = ['']
	actions = ['3. Go to the main hallway', '4. Drink the toilet water', '5. Look at yourself in the mirror']
	
	def enter(self, user):

		if Bathroom.enter_counter == 0:
		
			print(dedent("""
			You enter the bathroom and look around. The toilet, tub, and sink all look full of grime.
			As you turn on the light switch, one sole light flickers. It is suuuuuuper creepy in here.
			"""))
			Bathroom.enter_counter += 1
		
		print("You are in the bathroom. What would you like to do?\n")
		self.display_actions(Bathroom.actions)
		
		
		action = input(">")
		os.system('cls')

		if action == "1":
		
			self.print_map()
			
			return 'bathroom'

		elif action == "2": 
		
			user.display_items()
			
			return 'bathroom'
			
		elif action == "3":
		
			return 'main_hallway'
			
		elif action == "4":
		
			self.death('toilet')
			
		elif action == '5':
		
			print(dedent("""
			You look at yourself in the mirror. You begin to look back on your life in retrospect:
			What choices had you made that lead you to this position?
			Had you been satisfied with you life accomplishments?
			Did you leave the stove top on?
			With all these thoughts swimming through your head, one thing is abundantly clear...
			You really need a haircut
			"""))
			
			return 'bathroom'
			
		else:
		
			self.input_error()
			
			return 'bathroom'


		
		
class OdinsLair(Room):

	enter_counter = 0
	items = ['tuna']
	actions = ['3. Go to the main hallway', '4. Approach the beast', '5. Search under the bed']

	def enter(self, user):

		if user.eyesight == False:
		
			print(dedent("""
			It is too dark in here to see, and there are no light switches.
			You will need to find an external light source, or somehow get the ability to see in the dark...
			For now you go back to the main hallway.
			"""))
		
			return 'main_hallway'
		else:
		
			if OdinsLair.enter_counter == 0:
		
				print(dedent("""
				You\'ve entered Odin\'s lair. It is dark in here, but thanks to your new 
				and improved eyesight you're able to make out what is in the room.
				You see a cage, with a strange animal in it. He looks haggard and unkempt, but nice enough.
				There is also one sole bed in the corner. You imagine those sheets haven't been washed in quite some time.
				"""))
				OdinsLair.enter_counter += 1
			
			print("You are in Odin\'s lair. What would you like to do?\n")
			self.display_actions(OdinsLair.actions)
			
			action = input(">")

			os.system('cls')

			if action == "1":
			
				self.print_map()
				
				return 'odins_lair'

			elif action == "2": 
			
				user.display_items()
				
				return 'odins_lair'
				
			elif action == "3":
			
				return 'main_hallway'
				
			elif action == "4":
				
				print(dedent("""
				You approach the beast
				
				You: Hello...
				Odin: *No response. No Movement*
				You: Hello!
				Odin: *Grunts* Hello.
				You: Are you the evil I seek? Are you what I must destroy?
				Odin: *Chuckles* I am no evil. Merely a victim. A victim of circumstance.
				You: Where might I find this evil then?
				Odin: He is everywhere. And he is nowhere.
				You: That's really not helpful...
				Odin: I do not suggest you seek him out. I suggest you run and leave with your life.
				You: I'm afraid that's not an option.
				Odin: Hrm. Well if you must continue I leave you with this: Do not try and fight the evil
					  for he is too strong. You must sooth his anger. Do this with a creation of which 
					  he cannot resist.
				You: How do I do th-
				Odin: Sorry, but I am tired. I must rest. Good luck brave soul.
				"""))
				
				return 'odins_lair'

			elif action == "5":
			
				try:
					self.take_item(OdinsLair.items, 'tuna')
				
					print(dedent("""
					You look under the bed for something useful. You notice a strange packet just within arms reach.
					You grab it and take a look. It's a packet of tuna. 
					"Huh, odd thing to be under a bed" you think to yourself.
					You add it to your inventory.
					"""))
					user.add_item('tuna')
					
					return 'odins_lair'
			
				except:
					
					print("All that's left under here are cobwebs\n")
					
					return 'odins_lair'
					
			else:
			
				self.input_error()
			
				return 'odins_lair'			

class Office(Room):

	enter_counter = 0
	items = ['knife', 'ball of yarn']
	actions = ['3. Go to the main hallway', '4. Turn on the computer', '5. Open the safe']

	def enter(self, user):

		if Office.enter_counter == 0:
		
			print(dedent("""
			You enter the office. There is one desk. One computer. One open closet.
			In the closet you notice a safe.
			Based on the state of the rest of the house, it's actually fairly clean in here.
			"""))
			Office.enter_counter += 1
		
		print("You are in the office. What would you like to do?\n")
		self.display_actions(Office.actions)
		
		
		action = input(">")

		os.system('cls')

		if action == "1":
		
			self.print_map()
			
			return 'office'

		elif action == "2": 
		
			user.display_items()
			
			return 'office'
			
		elif action == "3":
		
			return 'main_hallway'
			
		elif action == "4":
		
			print(dedent("""
			You go to turn on the computer. Incredibly, it still works.
			You are met with the sign in screen. You don't know the password, but
			take a shot at it:
			"""))
			
			i = input("> ")
			
			print(f"\nOddly enough {i} was the correct password! How strange...")
			
			print(dedent("""
			You search around the computer's file system for a while.
			You notice the game Tetris is downloaded on the computer.
			You decide to fire it up. It's been a while since you've played,
			but you play and play and play. And play. Hours and days and months
			go by. You play tetris til your eyes dry out. Finally you pull yourself
			from the screen. "No more Tetris for a while" you think to yourself. 
			"""))

			
			return 'office'
		
		elif action == "5" and len(Office.actions) == 3:
		
			if ('key' in user.items) and ('knife' in Office.items):
			
				self.take_item(Office.items, 'knife')
				self.take_item(Office.items, 'ball of yarn')
				user.add_item('knife')
				user.add_item('ball of yarn')
				
				print(dedent("""
				You use your key to open the safe. Inside are 3 things:
				A knife
				A ball of yarn
				A note
				
				You put the knife and ball of yarn in your inventory.
				
				On the note, you see the letters "R U N".
				You really wish that you could read.
				"""))
			
			elif ('key' in user.items):
				
				print("You've already emptied the safe\n")
				
			
			else:
			
				print(dedent("""
				You don't have the necessary items to open the safe.
				You regret not attending the safe cracking seminar in college.
				"""))
				
			return 'office'
			
		else:
		
			self.input_error()
			return 'office'

class QuitosLair(Room):

	enter_counter = 0
	items = ['']
	actions = ['3. Go to the main hallway', '4. Slay the monster', '5. Placate the monster']

	def enter(self, user):

		if user.eyesight == False:
		
			print(dedent("""
			It is too dark in here to see, and there are no light switches.
			You will need to find an external light source, or somehow get the ability to see in the dark...
			For now you go back to the main hallway.
			"""))
		
			return 'main_hallway'
		else:
		
			if QuitosLair.enter_counter == 0:
		
				print(dedent("""
				You\'ve entered Quito's lair. As your eyes adjust to the darkness, you see it.
				The monster. The evil. The terror that has plagued this house.
				It peers at you through the darkness. You can see it's eyes glaring. 
				It feels as though hes looking directly into your soul. You feel uneasy.
				You must act quickly. Time is of the essence, and your life depends on it.
				"""))
				QuitosLair.enter_counter += 1
			
			print("You are in Quitos\'s lair. What would you like to do?\n")
			self.display_actions(QuitosLair.actions)
			
			action = input(">")

			os.system('cls')

			if action == "1":
			
				self.print_map()
				
				return 'quitos_lair'

			elif action == "2": 
			
				user.display_items()
				
				return 'quitos_lair'
				
			elif action == "3":
			
				return 'main_hallway'
				
			elif action == "4":
			
				if 'knife' in user.items:
				
					self.death('quito_attack_knife')
				
				else:

					self.death('quito_attack')
					
			elif action == "5":
				
				if ('catnip' in user.items) and ('tuna' in user.items) and ('ball of yarn' in user.items):
				
					self.victory()
					
				elif ('catnip' in user.items) or ('tuna' in user.items) or ('ball of yarn' in user.items):
				
					self.death('placate_one_item')
					
				else:
				
					self.death('placate_no_items')
				
			else:
			
				self.input_error()
				
				return 'quitos_lair'
				
class Map(object):
	
	scenes = {
		'main_entrance': MainEntrance(),
		'living_room': LivingRoom(),
		'kitchen': Kitchen(),
		'main_hallway': MainHallway(),
		'bathroom': Bathroom(),
		'odins_lair': OdinsLair(),
		'office': Office(),
		'quitos_lair': QuitosLair()
		}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		next_scene_value = Map.scenes.get(scene_name)
		return next_scene_value
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)



def main():

	os.system('cls')

	print("Welcome to your next great adventure!")
	name = input("What is your name brave adventurer?\n>")
	
	os.system('cls')
	
	print(f"Welcome {name}. Be prepared for your journey\n")
	
	player = User(str(name))

	play_map = Map('main_entrance')
	
	current_scene = play_map.opening_scene()
	last_scene = ' '
	
	while current_scene != last_scene:
		next_scene_name = current_scene.enter(player)
		current_scene = play_map.next_scene(next_scene_name)
	
	
if __name__ == "__main__":
	main()