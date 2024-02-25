import random

def play():
    user=input(" what u r choice ? 'r' for rock ,'p' for paper,'s' for scissors\n")
    computer=random.choice(['r','p','s'])

    if user==computer:
        return 'It\'s a tie'
    if is_win(user,computer):
        return 'You won!'
    return 'you lost!'
def is_win(player,opponet):
    if(player=='r'and opponet=='s') or (player=='s' and opponet=='p')\
        or (player=='p'and opponet=='r'):
        return True
    
print(play())
    
    
