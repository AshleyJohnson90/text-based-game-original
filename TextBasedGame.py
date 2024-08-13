# Ashley Johnson
# instructions for the player
def show_instructions():
    print('---------------------------------------------------------------------------------------')
    print('A restaurant adventure game')
    print('You walk into the steakhouse you work at to see every table full')
    print('You must move from location to location and collect items you will need to successfully complete your day')
    print('How to get from one location to the next: enter go North, go South, go East, or go West')
    print('How to add the item at the location to your inventory: enter get "item name"')
    print('You must collect all 6 items to serve the hangry customers or else....FIRED!')
    print('---------------------------------------------------------------------------------------')


# moving between rooms
def move_rooms(current_room, direction, rooms):
    current_room = rooms[current_room][direction]
    return current_room


# getting the item into the inventory
def grab_item(current_room, direction, rooms, inventory):
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # rooms dictionary
    rooms = {
        'Hallway': {'North': 'Stove', 'East': 'Hostess Counter', 'South': 'Kitchen', 'West': 'Bathroom'},
        'Bathroom': {'East': 'Hallway', 'item': 'Apron'},
        'Kitchen': {'North': 'Hallway', 'East': 'Sink Station', 'item': 'Serving Tray'},
        'Walk-in': {'West': 'Stove', 'item': 'Salad'},
        'Hostess Counter': {'North': 'Dining Room', 'West': 'Hallway', 'item': 'Order Pad'},
        'Stove': {'South': 'Hallway', 'East': 'Walk-in', 'item': 'Steak'},
        'Sink Station': {'West': 'Kitchen', 'item': 'Plate'},
        'Dining Room': ''
    }
    x = ' '
    inventory = []
    # the room the game starts in
    current_room = 'Hallway'
    show_instructions()

    while True:
        if current_room == 'Dining Room':
            # winning scenario
            if len(inventory) == 6:
                print('Well done! That 30% tip is going in your pocket, no mis-steaks were made.'
                      'Now to clean these dishes...')
                break
            # don't have the right amount of items losing scenario
            else:
                print('You did not get all 6 items.')
                print('The customer asked to speak to your manager...time to apply for unemployment!')
                print('Try again')
                break
        # what the player sees every time the need to make a decision in every room but the dining room
        print('Your location: ' + current_room)
        print('Your inventory:', inventory)
        if current_room != 'Dining Room' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        direction = input('What are you going to do next?\n').title().split()
        print('-----------------------------------------------------------------------------------------')

        # moving between rooms
        if len(direction) >= 2 and direction[1] in rooms[current_room].keys():
            current_room = move_rooms(current_room, direction[1], rooms)
            continue
        # getting the item in the room
        elif len(direction[0]) <= 3 and direction[0] == 'Get' and ' '.join(direction[1:]) in rooms[current_room]['item']:
            print('You grab the {}'.format(rooms[current_room]['item']))
            print('-----------------------------------------------------------------------------------------')
            grab_item(current_room, direction, rooms, inventory)
            continue
        # what happens if player enters something other than direction in room dictionary or action
        else:
            print('Ooopsies you cannot do that, try another way')
            print('-----------------------------------------------------------------------------------------')
            continue


main()
