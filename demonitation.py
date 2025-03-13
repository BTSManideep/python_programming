#demonitation
amount=int(input('enter amount:'))
print('number of five hundred notes:',amount//500)
rem=amount%500
print('number of hundred notes:',rem//100)
rem=rem%100
print('number of fifty notes:',rem//50)
rem=rem%50
print('number of ten notes:',rem//10)
rem=rem%10
print('remaining change:',rem)



