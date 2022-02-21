import random
values = [" " for x in range(9)]
values_guide = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
valuesI = [0,1,2,3,4,5,6,7,8]
values_index = []
player1 = []
player2 = []
by = ''
pla1inp = 0
play1Sc = 0
play2Sc = 0
name1 = ''
name2 = ''
aa = 'no'  # already assigned
ndam = 'yes'  # second assignment
ntvld1 = ''
ntvld2 = ''
tempwin = ''
tempPlayer = ''
current_input = 0
ra = False

def form_indicate(vg):
    print()
    print('        |        |')
    print('        |        |')
    print(f'    {vg[0]}   |   {vg[1]}    |   {vg[2]}    ')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {vg[3]}   |   {vg[4]}    |   {vg[5]}    ')
    print('        |        |')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {vg[6]}   |   {vg[7]}    |   {vg[8]}    ')
    print('        |        |')
    print()


def form(gameindex):
    print()
    print('        |        |')
    print('        |        |')
    print(f'    {gameindex[0]}   |   {gameindex[1]}    |   {gameindex[2]}    ')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {gameindex[3]}   |   {gameindex[4]}    |   {gameindex[5]}    ')
    print('        |        |')
    print(' _______|________|_______')
    print('        |        |')
    print(f'    {gameindex[6]}   |   {gameindex[7]}    |   {gameindex[8]}    ')
    print('        |        |')
    print()


possibleV = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def beginning():
    # if ttp > 1:
    #     print(f"""{name1.upper()}, Choose your character as Player 1:
    #         1. X
    #         2. O""")
    # else:
    #     print(f"""Choose your character as Player 1:
    #         1. X
    #         2. O""")
    # cinp = input('Your Choice: ')
    # while cinp != 1 or cinp != 2:
    #     try:
    #         cinp = int(cinp)
    #         if cinp == 1:
    #             return 'X'
    #         elif cinp == 2:
    #             return 'O'
    #         else:
    #             print(f'{cinp} is not a valid input')
    #             cinp = input('Your Choice: ')
    #             # raise Exception('Invalid Number!')
    #     except ValueError:
    #         print(f'{cinp} is not a valid input!')
    #         cinp = input('Your Choice: ')
		return 'X'



def robot():
	global ra
	# try:
	if (values[0] == 'X' and values[1] == 'X' and values[2]== ' '):
		rv = 2
	elif (values[0] == 'X' and values[2] == 'X' and values[1]== ' '):
		rv = 1
	elif (values[2] == 'X' and values[1] == 'X' and values[0]== ' '):
		rv = 0
	
	elif (values[4] == 'X' and values[3] == 'X' and values[5]== ' '):
		rv = 5
	elif (values[5] == 'X' and values[4] == 'X' and values[3]== ' '):
		rv = 3
	elif (values[3] == 'X' and values[5] == 'X' and values[4]== ' '):
		rv = 4
	
	elif (values[6] == 'X' and values[7] == 'X' and values[8]== ' '):
		rv = 8
	elif (values[7] == 'X' and values[8] == 'X' and values[6]== ' '):
		rv = 6
	elif (values[8] == 'X' and values[6] == 'X' and values[7]== ' '):
		rv = 7
	
	elif (values[0] == 'X' and values[4] == 'X' and values[8]== ' '):
		rv = 8
	elif (values[4] == 'X' and values[8] == 'X' and values[0]== ' '):
		rv = 0
	elif (values[0] == 'X' and values[8] == 'X' and values[4]== ' '):
		rv = 4
	
		
	elif (values[2] == 'X' and values[4] == 'X' and values[6]== ' '):
		rv = 6
	elif (values[4] == 'X' and values[6] == 'X' and values[2]== ' '):
		rv = 2
	elif (values[6] == 'X' and values[2] == 'X' and values[4]== ' '):
		rv = 4
	
	elif (values[0] == 'X' and values[3] == 'X' and values[6]== ' '):
		rv = 6
	elif (values[3] == 'X' and values[6] == 'X' and values[0]== ' '):
		rv = 0
	elif (values[6] == 'X' and values[0] == 'X' and values[3]== ' '):
		rv = 3
	
	elif (values[4] == 'X' and values[1] == 'X' and values[7]== ' '):
		rv = 7
	elif (values[7] == 'X' and values[4] == 'X' and values[1]== ' '):
		rv = 1
	elif (values[1] == 'X' and values[7] == 'X' and values[4]== ' '):
		rv = 4
	
	elif (values[5] == 'X' and values[2] == 'X' and values[8]== ' '):
		rv = 8
	elif (values[2] == 'X' and values[8] == 'X' and values[5]== ' '):
		rv = 5
	elif (values[8] == 'X' and values[5] == 'X' and values[2]== ' '):
		rv = 2
	else:
		rv = random.choice(valuesI)	
		
	values.pop(rv)
	values.insert(rv, 'O')
	player2.append(rv)
	values_index.append(rv)
	valuesI.remove(rv)
	# except Exception as e:
	# 	print(e)
		# rv = random.choice(values)
		# print(rv)

	
	# print(player1)
	# print(values)
	form(values)
	
def checkMatchPlay1(ch=2):
    global play1Sc, play2Sc, aa, ttp, tempPlayer
    co = 0
    if ' ' not in values:
        print('It\'s a draw!')
        return False
    for li in possibleV:
        for k in range(3):
            if li[k] in player1:
                co += 1
                if co == 3:
                    tempPlayer = name1.upper()
                    if tempPlayer == name1.upper():
                        play2Sc += 1
                        tempPlayer = name2.upper()
                    # else:
                        # play2Sc += 1
                    if ttpBey == 1:
                        print(f'Player{ch} \'X\' win this macth')
                    else:
                        print(f'{tempPlayer} win this match')
                        aa = 'no'


                    return False
        else:
            co = 0
    return True


def checkMatchRobot():
	global play1Sc, play2Sc, aa, ttp, tempPlayer
	co = 0
	if ' ' not in values:
		print('It\'s a draw!')
		return False
	for li in possibleV:
			for k in range(3):
					if li[k] in player2:
							co += 1
							if co == 3:
									tempPlayer = 'Robot'
									print(f'{tempPlayer} win this match')
										


									return False
			else:
					co = 0
	return True




def gameProcessPlayer1(ch='1'):
	global values_index, by, aa, ttp, ntvld1, pla1inp, current_input
	if ttpBey > 1:
		ttp += 1
	elif ttp == 1:
		pla1inp = input(f'Player{ch} \'X\': ')
	elif ttp > 1 or ttpBey > 1:
		if aa == 'yes':
					pla1inp = input(f'{name2.upper()} \'X\': ')
					aa = 'no'
					ttp -= 1
					ntvld1 = name2.upper()
		else:
			pla1inp = input(f'{name1.upper()} \'X\': ')
			aa = 'yes'
			ttp -= 1
			ntvld1 = name1.upper()

	try:
			pla1inp = int(pla1inp)
			current_input = pla1inp
		
			if ttp == 1:
					if (pla1inp - 1) in values_index:
							if (pla1inp - 1) in player1:
									by = 'you'
							else:
									by = 'player2'
							print(f'Sorry, place is already reserved by {by}!')
							pla1inp = int(input(f'Player{ch} \'X\': '))
			elif ttp > 1 or ttpBey > 1:
					if (pla1inp - 1) in values_index:
							if (pla1inp - 1) in player1:
									by = 'you'
							else:
									by = ntvld1
							print(f'Sorry, place is already reserved by {by}!')
							pla1inp = int(input(f'Player{ch} \'X\': '))

			while (pla1inp - 1) not in player1:
					if (values[pla1inp - 1] == ' ') and ((pla1inp - 1) not in values_index):
							values.pop(pla1inp - 1)
							values.insert(pla1inp - 1, 'X')
							player1.append(pla1inp - 1)
							values_index.append(pla1inp - 1)
							valuesI.remove(pla1inp-1)

					else:
							if (pla1inp - 1) in player1:
									by = 'you'
							else:
									by = ntvld1
							print(f'Sorry, place is already reserved by {by}!')
							pla1inp = int(input(f'Player1 \'X\': '))

			form(values)

	except IndexError:
			print(f'Error: Index {pla1inp} is out of range!')
			gameProcessPlayer1()
	except ValueError:
			print(f'Error: {pla1inp} is not a number!')
			if aa == 'yes':
					aa = 'no'
			elif aa == 'no':
					aa = 'yes'
			gameProcessPlayer1()



run = True
ttp = 1 # int(input('Times to play: '))
ttpBey = ttp
# uc = beginning()
uc = ''
if ttp > 1:
    name1 = input('Name of player 1: ')
    tempPlayer = name1
    name2 = input('Name of player 2: ')

    uc = beginning()
    form_indicate(values_guide)
elif ttp == 1:
    uc = beginning()
    form_indicate(values_guide)

run = True
while run:
    if uc == 'X':
        gameProcessPlayer1()
        if not checkMatchPlay1(1):
            # play1Sc += 1
            ttp -= 1
            
            if ttp > 0:

                uc = beginning()
                form_indicate(values_guide)
                continue
            else:
                break
            # run = False
            # break

        robot()
        if not checkMatchRobot():
            # play2Sc += 1
            ttp -= 1
            tempPlayer = 1
            if ttp > 0:

                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False
    elif uc == 'O':
        gameProcessPlayer1('1')
        # play2Sc += 1
        if not checkMatchRobot()():
            ttp -= 1
            if ttp > 0:
                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False
            # break

        gameProcessPlayer1('2')
        if not checkMatchPlay1():
            # play1Sc += 1
            ttp -= 1
            if ttp > 0:

                uc = beginning()
                form_indicate(values_guide)

                continue
            else:
                break
            # run = False






