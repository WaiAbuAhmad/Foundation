def order(sentence):
  
  
  # code here
  
  if sentence =="" :
    correct_list=[]
    
    
  else :
    correct_list=[]
    split_sentence = sentence.split()  
    correct_list_length=len(split_sentence)
    for i in range(correct_list_length):
      correct_list.append(i)
    
    for word in range (len(split_sentence)) :
      
      correct_sentence=[]
      for letter in split_sentence[word]:
        
                
        it_digits = letter.isdigit()
        
        if it_digits == True :
          letter =int(letter)
          correct_list[letter-1]=split_sentence[word]
          
  sentence =  " ".join(correct_list)  
  
  return(sentence)