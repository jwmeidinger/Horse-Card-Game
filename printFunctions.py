

# --- Art ---
horseArt1 = ''' 
            ,~  
          ~/(\  
  ~ _____~/ / ` 
~~~( )___( /    
  /.'     \|\   
'|        /  \  
________________
         '''

horseArt2 = ''' 
            ,~  
          ~/(\  
  ~ _____~/ / ` 
~~~( )___( /    
  /.'     / \   
'|       /   \\  
________________
         '''

horseArt3 = ''' 
            ,~  
          ~/(\  
  ~ _____~/ / ` 
~~~( )___( |    
  /|/_  _`/|    
    \    /      
________________
         '''

horseArt4 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___( /    
   |\!_ _`/\    
     `   /      
________________
         '''

horseArt5 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___( /_   
   |\!_ _`/ /   
    \           
________________
         '''

horseArt6 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___( /_   
    \!_  _\| |  
      \         
________________
         '''

horseArt7 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___( /_   
    \!_  _| \   
      \         
________________
         '''
horseArt8 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___( /_   
   |/_    \| \  
    \     '     
________________
         '''

horseArt9 = ''' 
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___(_/_   
  /.'|_    / \  
   \\            
________________
         '''

horseArt10 = '''
             ,~ 
           ~/(\ 
  ~ _____~/ /  `
~~~( )___(_/_   
  /.'      \ |  
  \/        \   
________________
         '''

horseArt11 = '''
            ,~  
          ~/(\  
  ~ _____~/ / ` 
~~~( )___( /_   
  /.'     \| \  
'|        /     
________________
         ''' 
raceSpace = '''
                
                
                
                
                
                
________________
            '''
diamondArt = '''
     /\\
   .'  `.
  '      `.
<          >
 `.      .'
   `.  .'
     \/
         ''' 
          
clubArt = '''
     .-~~-.
    {      }
 .-~-.    .-~-.
{              }
 `.__.'||`.__.'
       ||
      '--`
         ''' 

heartArt = '''
 .-~~~.  .~~~-.
{      \/      }
 `.          .'
   `.      .'
     `.  .'
       \/
         ''' 

spadeArt = '''
       /\\
     .'  `.
  .'        `.
 {            }
  -...-||-...-
       ||
      '--`
         ''' 

# --- Functions ---

## This function is used to switch between the art
def switch(x):
    return {
        0  : raceSpace,
        1  : horseArt1,
        2  : horseArt2,
        3  : horseArt3,
        4  : horseArt4,
        5  : horseArt5,
        6  : horseArt6,
        7  : horseArt7,
        8  : horseArt8,
        9  : horseArt9,
        10 : horseArt10,
        11 : horseArt11,
    }[x]

def printHorses(horse1Score, horse2Score, horse3Score, horse4Score, count):

    horseArt = switch(count)
    ## Each horse has it's own race lane and art
    art1 = (raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,horseArt,diamondArt)
    art2 = (raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,horseArt,clubArt)
    art3 = (raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,horseArt,heartArt)
    art4 = (raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,raceSpace,horseArt,spadeArt)

    ## Joining the spaces and art together to make one string.
    stringOutput1 = art1[horse1Score:]
    finalString1 = '\n'.join(' '.join(pair) for pair in zip(*(s.split('\n') for s in stringOutput1)))

    stringOutput2 = art2[horse2Score:]
    finalString2 = '\n'.join(' '.join(pair) for pair in zip(*(s.split('\n') for s in stringOutput2)))

    stringOutput3 = art3[horse3Score:]
    finalString3 = '\n'.join(' '.join(pair) for pair in zip(*(s.split('\n') for s in stringOutput3)))

    stringOutput4 = art4[horse4Score:]
    finalString4 = '\n'.join(' '.join(pair) for pair in zip(*(s.split('\n') for s in stringOutput4)))
    
    return finalString1, finalString2, finalString3, finalString4
