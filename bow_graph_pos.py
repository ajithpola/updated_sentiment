import matplotlib.pyplot as plt

def graph():
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    file=open("bow_pos.txt","r")
    data=file.read()
    data=data.split("\n")
    labeldata = [x[:x.index(':')] if ':' in x else x for x in data]

    intdata=[x[x.index(':')+1:] if ':' in x else x for x in data]
#data = map(lambda s: s.strip(), data)
    intdata[:] = [line.rstrip(':') for line in intdata]

    file.close()
    sizes=[]
    labels=[]
    print(intdata)
    print(labeldata)
    for i in range(len(intdata)-1):
        sizes.append(intdata[i])
        labels.append(labeldata[i])


    print(sizes)
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,labels=labels,autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
