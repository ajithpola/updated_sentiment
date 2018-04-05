import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from tkinter import messagebox
import os
import csv

parag=[]
para=[]

def func(opinion):

#    parag=str(opinion)
    #parag = "What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid"
#    para=parag.lower()

    with open(opinion, 'r+') as myfile:
        data=myfile.read().replace('\n', '')

    para=data.lower()

    sentense = word_tokenize(para)
    word_features = []

    for i,j in nltk.pos_tag(sentense):
        if j in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
            word_features.append(i)


#print(word_features)
    pos=0
    neg=0
    sum=0
    searchfile = open("./negative.txt", "r")
    mylist = searchfile.readlines()
    for line in mylist:
        for wf in word_features:
            if wf == line.strip():
                #print(wf)
                neg=neg+1

    searchfile.close()

    searchfile = open("./postive.txt", "r")
    mylist = searchfile.readlines()
    for line in mylist:
        for wf in word_features:
            if wf == line.strip():
           # print(wf)
             pos=pos+1

    searchfile.close()
    sum=pos+neg
    posper=pos*100//sum
    negper=neg*100//sum

    file=open("bow_pos.txt","a")
    file.write(os.path.splitext(os.path.basename(opinion))[0]+":"+str(posper)+'\n')
    file.close()

    file1=open("bow_neg.txt","a")
    file1.write(os.path.splitext(os.path.basename(opinion))[0]+":"+str(negper)+"\n")
    file1.close()

    if(neg>pos):
        print("negative")
        messagebox.showinfo("result", "NEGATIVE ")
    else:
        print("positive")
        messagebox.showinfo("result", "POSITIVE")