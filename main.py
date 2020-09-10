def getGradePoint(g1):
  gradep=0;
  if(g1=="A"):
    gradep=4.0
  elif(g1=="A-"):
    gradep=3.67
  elif(g1=="B+"):
    gradep=3.33
  elif(g1=="B"):
    gradep=3.0
  elif(g1=="B-"):
    gradep=2.67
  elif(g1=="C+"):
    gradep=2.33
  elif(g1=="C"):
    gradep=2.0
  elif(g1=="D"):
    gradep=1.0
  else:
    gradep=0.0
  
  return gradep;

def run():
  grade1=(input("Enter your course 1 letter grade: "))
  credit1=float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(grade1)}")

  grade2=(input("Enter your course 2 letter grade: "))
  credit2=float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(grade2)}")

  grade3=(input("Enter your course 3 letter grade: "))
  credit3=float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(grade3)}")

  finalgrade=(((getGradePoint(grade1)*(credit1)))+(getGradePoint(grade2)*(credit2))+(getGradePoint(grade3)*(credit3)))/(credit1+credit2+credit3)

  print(f"Your GPA is: {finalgrade}")

  
if __name__ == "__main__":
  run()

  
