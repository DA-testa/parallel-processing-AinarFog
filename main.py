# python3

def parallel_processing(n, m, data):
  step=m.split(" ")
  tests=[True]*int(n[0])
  for i in range(len(step)):
    try:
      step[i]=int(step[i])
    except:
      step.pop(i)
      
  output = []
  for i in range(len(step)):
    if (True in tests):
      for j in range(len(data)):
        if(tests[j]==True):
          output.append(str(j)+" "+str(data[j]))
          data[j]=data[j]+step[i]
          tests[j]=False
          break
    else:
      tests=[True]*int(n[0])
      for j in range(len(data)):
        if(tests[j]==True):
          output.append(str(j)+" "+str(data[j]))
          data[j]=data[j]+step[i]
          tests[j]=False
          break

  return output

  
def listprint(list):
  for i in range(len(list)):
    print(list[i])

    
def main():
  n =str(input("Enter thread count: "))
  m =str(input("Enter job count: "))
  data =[0]*int(n[0])
  
  result = parallel_processing(n,m,data)
  listprint(result)
  
if __name__ == "__main__":
    main()
