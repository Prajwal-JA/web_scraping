import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    # r>s, s>p, p>rp
    if is_win(user, computer):
        return 'you won'

    return 'you lost'

def is_win(player, opponenet):
    # return true if player wins
    # r>s, s>p, p>r
    if (player == 'r' and opponenet == 's') or (player == 's' and opponenet == 'p') \
    or (player == p and opponenet == r ):
        return True

print (play())
