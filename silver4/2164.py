import sys
from collections import deque


N=int(sys.stdin.readline())
cards=[i for i in range(1, N+1)]
deck=deque(cards)

while(len(deck)>1):
    deck.popleft()
    card=deck.popleft()
    deck.append(card)

print(deck[0])

