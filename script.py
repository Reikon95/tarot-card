tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

tarot.pop(13)
spread['past'] = 'Death'


print(spread)

tarot.pop(22)
spread['present'] = 'The Fool'


print(spread)

tarot.pop(10)
spread['future'] = 'Wheel of Fortune'

print(spread)

for job, value in spread.items():
  
  print('Your ' + job + ' is the ' + value + ' card.')
  
