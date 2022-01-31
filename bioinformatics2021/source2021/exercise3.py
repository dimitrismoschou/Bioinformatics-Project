import random
from Bio import SeqIO
#Φορτώνουμε τις 2 αλληλουχιες 
for seq1 in SeqIO.parse("liver.fasta", "fasta"): 
	chromo_liver = seq1.seq	
for seq2 in SeqIO.parse("brain.fasta", "fasta"):
	chromo_brain = seq2.seq
chromo_liver = len(seq1) #Βρίσκουμε το μέγεθος της πρώτης αλληλουχιάς
chromo_brain = len(seq2) #Βρίσκουμε το μέγεθος της δεύτερης αλληλουχιάς
player = 1
#Εδώ ελέγχουμε αν κέρδισε καποιος παίχτης
def check(player):
    if(chromo_brain==0 or chromo_liver==0):
        print("The winner is Player ",player)
while(True): #Το παιχνίδι παίζει μέχρι να νικήσει ένας από τους δύο παίχτες
    if(chromo_brain!=0 and chromo_liver!=0): #Αν δεν εχει μηδενισει καμια αλληλουχια μπαινει στην if
        print("The player number ",player ," plays now. \nChoose if you would like to erase from the 1.first(liver), 2.second(brain) or 3.from both sequences. "+
        "\nType 1, 2, or 3: ")
        if(chromo_brain<chromo_liver): #αν η αλληλουχια 1 ειναι μικροτερη απο την 2 τοτε ο τυχαιος αριθμος θα ειναι απο το 1 μεχρι το μεγεθος της αλληλουχιας 1
            smaller_seq=chromo_brain
        else:
            smaller_seq=chromo_liver     #αν η αλληλουχια 2 ειναι μικροτερη απο την 1 τοτε ο τυχαιος αριθμος θα ειναι απο το 1 μεχρι το μεγεθος της αλληλουχιας 2
        randomness = random.randint(1,smaller_seq)    #τυχαιος αρθμος απο το 1 μεχρι τον αριθμο που ορισαμε απο πανω
        choice= int(input()) #Ο χρηστης δινει στο προγραμμα το τι θελει να κανει
        while(True):    #Τρέχει μεχρι να δεχτει σωστο τυπο input απο τον χρηστη
            if(choice==1 or choice==2 or choice==3): #Αν η επιλογη ειναι 1 η 2 η 3 βγαινει απο την while και συνεχιζει
                break
            else:
                print("Available choices: 1, 2 or 3 !!")  #Αν η επιλογη δεν ειναι 1 η 2 η 3 εκτυπωνονται οι διαθεσιμες επιλογες 
                choice = int(input()) #Ο χρηστης δινει στο προγραμμα το τι θελει να κανει
        if(choice==1): #Αν επιλεξει την επιλογη 1
            chromo_liver-=randomness #Αφαιρουμε απο την αλληλουχια 1 τον τυχαιο αριθμο randomness
            check(player) #Ελεγχουμε μηπως τελειωσε το παιχνιδι
        elif(choice==2):#Αν επιλεξει την επιλογη 2
            chromo_brain-=randomness #Αφαιρουμε απο την αλληλουχια 2 τον τυχαιο αριθμο randomness
            check(player) #Ελεγχουμε μηπως τελειωσε το παιχνιδι
        elif(choice==3):#Αν επιλεξει την επιλογη 3
            chromo_brain-=randomness #Αφαιρουμε απο την αλληλουχια 1 τον τυχαιο αριθμο randomness και
            chromo_liver-=randomness #Αφαιρουμε απο την αλληλουχια 2 τον τυχαιο αριθμο randomness
            check(player)

        if(player==1): #Αλλαγη παιχτων
            player=2 #Αν επαιζε ο παιχτης 1 τωρα εχει σειρα ο παιχτης 2
        elif(player==2): #Αλλαγη παιχτων
            player=1 #Αν επαιζε ο παιχτης 2 τωρα εχει σειρα ο παιχτης 1
    else: #Αν δεν μπει στην if 
        break; #Βγαινει απο την while