print("\n-----2015 AoC Day Two-------")
#Load Data
file = open(r'2015Day2\Input.txt')
contents = file.read()
frame = contents.splitlines()
#Init Variable
totalPaper = 0
totalRibbon = 0

def measurePaper(dimensions):
    l,w,h = dimensions
    l = int(l)
    w = int(w)
    h = int(h)
    dimensions2 = (l,w,h)
    sides = (l*w,w*h,h*l)
    paper = sum(sides)*2 + min(sides)
    ribbon = 2*((sum(dimensions2))-max(dimensions2))+ l*w*h 
    return(paper,ribbon)
    

for item in frame:
    item =item.split('x')
    paper,ribbon = measurePaper(item)
    totalPaper += paper
    totalRibbon += ribbon
    
print(f'Elves need {totalPaper} square inches of paper')
print(f'Elves need {totalRibbon} square inches of paper')
