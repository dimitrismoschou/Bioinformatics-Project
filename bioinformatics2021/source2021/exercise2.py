from numpy import log as ln
dual_states=('A','B') #Δυο καταστασεις (Α,Β)


possibility_a = [['A','G','T','C'],[0.4,0.4,0.1,0.1]] #Η πιθανοτητα να εκπεμψει πουρινες και πυριμιδινες στην κατασταση A
possibility_b=[['T','C','A','G'],[0.3,0.3,0.2,0.2]] #Η πιθανοτητα να εκπεμψει πουρινες και πυριμιδινες στην κατασταση Β

goal=('G','G','C','T')  #Η ζητουμενη αλληλουχια

pos_a_to_a_and_b=[0.9,0.1] #Η πιθανοτητα να συνεχισει απο την Α κατασταση στην Α και στην Β
pos_b_to_a_and_b=[0.1,0.9] #Η πιθανοτητα να συνεχισει απο την Β κατασταση στην Β και στην Α

initial_pos=[0.5,0.5]  ##Η αρχικη πιθανοτητα να ξεκινησει απο το Α και το Β


def viterbi_algo(possibility_a,pos_a_to_a_and_b,goal,initial_pos,possibility_b,from_b_to_b_and_a,dual_states):
    temp_a=[]   #Αποθηκευονται οι τιμες της Α καταστασης απο τον viterbi αλγοριθμο
    temp_b=[]   #Αποθηκευονται οι τιμες της Β καταστασης απο τον viterbi αλγοριθμο
    flag=True
    temp1=False
    temp2=False
    start=False
    log_num=0
    i=0
    best_path=[]
    while(flag):    #Οσο το flag παραμενει true η while θα τρεχει 
        for j in range(0,len(goal)):    #Μπαινει σε μια for με μεγεθος οση ειναι η ζητουμενη αλληλουχια(goal)
            if(start==False):   #Εαν το start ειναι false σημαινει οτι βρισκομαστε στην πρωτη κατασταση με ζητουμενο το G
                if(possibility_a[0][j]==goal[i]):       #Εαν το possibility_a[0][j] ισουται με το ζητουμενο
                    temp_a.append(initial_pos[0]*possibility_a[1][j]) #τοτε η temp_a παιρνει την αρχικη πιθανοτητα του A και την πολλαπλασιαζει με την πιθανοτητα του ζητουμενου νουκλεοτιδιου
                    temp1=True
                if(possibility_b[0][j]==goal[i]):
                    temp_b.append(initial_pos[1]*possibility_b[1][j]) ##τοτε η temp_b παιρνει την αρχικη πιθανοτητα του Β και την πολλαπλασιαζει με την πιθανοτητα του ζητουμενου νουκλεοτιδιου
                    temp2=True
                if(temp1 and temp2): #Εαν το temp1 και το temp2 ειναι true τοτε εχουμε βρει το πρωτο ζητουμενο(goal[0])
                    start=True #Το start γινεται True οποτε το προγραμμα δεν μπαινει ξανα στην αρχικη if
                    i+=1
                    if(temp_a[0]>temp_b[0]):    #Εαν το temp_a που βρηκαμε ειναι μεγαλυτερο απο το temp_b που βρηκαμε τοτε 
                        best_path.append(dual_states[0]) #Το best_path παιρνει την πρωτη κατασταση
                        log_num+= ln(temp_a[0])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num
                    elif(temp_a[0]<temp_b[0]):  #Αλλιως το best_path παιρνει την δευτερη κατασταση
                        best_path.append(dual_states[1])
                        log_num+= ln(temp_b[0])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num
                    break       #Αφου βρει ποιο ειναι μεγαλυτερο κανει break απο την for και ξεκιναει για τις υπολοιπες καταστασεις αφου το start γινεται True στην σειρα 36
            if(start and temp1 and temp2):  #Εαν και τα τρια flag ειναι true ψαχνουμε τις υπολοιπες καταστασεις
                temp1=False     #Κανουμε το temp1 και το temp2 False ωστε να τα χρησιμοποιησουμε ξανα στον υπολοιπο κωδικα
                temp2=False 
            if(start==True):    #Εαν το start ειναι True
                if(possibility_a[0][j]==goal[i] and best_path[i-1]=='A'):   #Εαν το νουκλεοτιδιο της possibility_a  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την πρωτη κατασταση(Α)
                    temp_a.append(round(pos_a_to_a_and_b[0]*possibility_a[1][j]*temp_a[i-1],10))   #Η temp_a παιρνει την πιθανοτητα να παει απο το Α στο Α πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_a της προηγουμενης καταστασης
                    temp1=True
                elif(possibility_a[0][j]==goal[i] and best_path[i-1]=='B'):     #Αλλιως εαν το νουκλεοτιδιο της possibility_a  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την δευτερη κατασταση(Β)
                    temp_a.append(round(pos_b_to_a_and_b[0]*possibility_a[1][j]*temp_b[i-1],10))   #Η temp_a παιρνει την πιθανοτητα να παει απο το Β στο Α πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_b της προηγουμενης καταστασης
                    temp1=True                      
                if(possibility_b[0][j]==goal[i] and best_path[i-1]=='A'):   #Εαν το νουκλεοτιδιο της possibility_b  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την πρωτη κατασταση(Α)
                    temp_b.append(round(pos_a_to_a_and_b[1]*possibility_b[1][j]*temp_a[i-1],10))   #Η temp_b παιρνει την πιθανοτητα να παει απο το Α στο Β πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_a της προηγουμενης καταστασης
                    temp2=True
                elif(possibility_b[0][j]==goal[i] and best_path[i-1]=='B'): #Αλλιως εαν το νουκλεοτιδιο της possibility_b  ισουται με το ζητουμενο νουκλεοτιδιο και το best_path ισουται με την δευτερη κατασταση(Β)
                    temp_b.append(round(pos_b_to_a_and_b[1]*possibility_b[1][j]*temp_b[i-1],10))   #Η temp_b παιρνει την πιθανοτητα να παει απο το Β στο Β πολλαπλασιαζοντας την με την πιθανοτητα
                                                                                            #του ζητουμενου νουκλεοτιδιου και το temp_b της προηγουμενης καταστασης
                    temp2=True
                if(temp1==True and temp2==True):    #Εαν το temp1 και το temp2 ειναι True
                    if(temp_a[i]>temp_b[i]):        #Εαν το temp_a ειναι μεγαλυτερο του temp_b 
                        best_path.append(dual_states[0]) #Τοτε το best_path παιρνει την πρωτη κατασταση
                        log_num+= ln(temp_a[i])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num 
                    else:
                        best_path.append(dual_states[1]) #Αλλιως το best_path παιρνει την δευτερη κατασταση
                        log_num+= ln(temp_b[i])             #Μετατρεπει τις αριθμιτικες τιμες σε λογαριθμικες και τις προσθετει σε μια μεταβλητη log_num 
                    i+=1
            if(i==4 and len(best_path)==4): #Εαν το i εχει γινει 4 και το best_path εχει 4 τιμες τοτε
                flag=False  #Το flag γινεται false και οταν τελειωσει η while βγαινει απο αυτην
                for i in range(0,len(best_path)):        #Με μια for εκτυπωνει τις τιμες της Α και της Β καταστασης καθως και το μονοπατι με την μεγαλυτερη πιθανοτητα
                    print('A is: ',temp_a[i],'and B is: ',temp_b[i])
                print('The best path is: ',best_path,'and the rounded sum of the logarithms for best_path is: ',round(log_num,4))  #Εκτυπωνει το καλυτερο μονοπατι και το αθροισμα των λογαριθμικο αθροισμα 
                break   #Αφου εχουν εκτπωθει ολα κανει break, βγαινει απο την for και αφου το flag εχει γινει False τελειωνει και η while
                        
viterbi_algo(possibility_a,pos_a_to_a_and_b,goal,initial_pos,possibility_b,pos_b_to_a_and_b,dual_states)  #Καλειται η viterbi_algo
