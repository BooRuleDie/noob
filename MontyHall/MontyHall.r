iteration = 100000

Gcounter = 0 # goat counter
Fcounter = 0 # ferrari counter

for(val in 1:iteration){

Boxes =	sample(c('G','F','G')) # Shuffling vector

RandomChoice = sample(1:3,1) # Creating player's choice

if(Boxes[RandomChoice] == 'F'){
	Fcounter = Fcounter + 1
} else {
	Gcounter = Gcounter + 1
	}

}
sprintf("In first %g games, player hasn't changed his answer after host offered him another door.",iteration)
sprintf("%s times goat and %s times ferrari has been selected.", Gcounter, Fcounter)
sprintf("Success rate is %s%%", (Fcounter/iteration)*100)

Gcounter = 0 # goat counter
Fcounter = 0 # ferrari counter

for (val in 1:iteration){

Boxes =	sample(c('G','F','G')) # Shuffling vector

RandomChoice = sample(1:3,1) # Creating player's choice

# If player choose G, since host is going to eliminate other goat and player always change his answer
# with a 100% possibility, he will choose ferrari.

# and since player always change his answers, he can't choose ferrari if first selected box is F.

if(Boxes[RandomChoice] == 'G'){
	Fcounter = Fcounter + 1
} else {
	Gcounter = Gcounter + 1
	}
}
""
"=================================================================================="
""
sprintf("In next %g games, player changed his answer everytime after host offered him another door.",iteration)
sprintf("%s times goat and %s times ferrari has been selected.", Gcounter, Fcounter)
sprintf("Success rate is %s%%", (Fcounter/iteration)*100)