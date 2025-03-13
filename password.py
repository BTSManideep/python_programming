#akadaA@24
a=input('enter password:')
up=low=dig=sp=False
if len(a)>=8:
    for i in a:
        if i.isupper():
            up=True
        elif i.islower():
            low=True
        elif i.isdigit():
            dig=True
        elif i in ['!','@','#','$','%','^','&','*','-','_']:
            sp=True
if up and low and dig and sp:
    print('valid password...')
else:
    print('invalid password...')

        
        
        
        
    
