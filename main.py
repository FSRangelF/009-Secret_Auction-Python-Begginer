# import art

# print(art.logo)

bids = {}
option = "yes"
while option != "no":
  name = str(input('What is your name?'))
  bid = int(input("What´s your bid?: $ "))
  option = str(input("Are there any other bidders? Type 'yes' or 'no'.")).lower()
  #print("\n"*100)
  bids[name] = bid

highest_bid = 0
winner = ""
for key in bids:
  if bids[key] > highest_bid:
    winner = key
    highest_bid = bids[key]

winner2 = max(bids, key=bids.get)

#print("\n"*100)
print(f"The winner is {winner} with a bid of ${bids[winner]}")
print(f"The winner is {winner2} with a bid of ${bids[winner2]}")
