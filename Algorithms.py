#SHORTTEXT JOB NEXT SERVES
from fomate import tabulate
from Sort import Sort
headers=['PROCESS','Arival','Burst','Complete','TAT','Wating']
prosess=""
time=""

def Insert_Element(column=3):
      row=int(input("Enter number of rows: "))
      if column==3:
         array=[[0]*6 for _ in range(row)]
      else:
         array=[[0]*7 for _ in range(row)]
      for i in range(column):
         for j in range(row):
            if column==3:
               if i ==0:
                     array[j][i]=input(f'prosess {j+1}: ')
               elif i==1:
                     array[j][i]=int(input(f'Arrival Time {j+1}:'))
               elif i==2:
                     array[j][i]=int(input(f'Burst Time {j+1}: '))
            else:
               if i ==0:
                     array[j][i]=input(f'prosess {j+1}: ')
               elif i==1:
                     array[j][i]=int(input(f'Priority {j+1}:'))
               elif i==2:
                  array[j][i]=int(input(f'Arrival Time {j+1}: '))
               else:
                  array[j][i]=int(input(f'Burst Time {j+1}: '))
      return array

def Display(prosess,times,table,sum):
   ganttChart=[times.split()]
   print("\n___________________________________________________________\nGantt Chart :-\n")
   print(tabulate(ganttChart,("_"+prosess).split()))
   print('\n\nTable :-\n\n',tabulate(table,headers),'\n\nAverage of  W.T.=',str(sum)+'/'+str(len(table))+'='+str(sum/len(table)))
   print('___________________________________________________________')


def IsItCameInZeroTime(Table,column=1):#this function check if all prosess came in same time
   Count=0
   for i in range(len(Table)):
      Count=Count+Table [i][column]
   return Count!=0


def FirstComeFirstService():
   table=Insert_Element()
   NoTCameSameTime=IsItCameInZeroTime(table)
   if NoTCameSameTime:
      Sort.as_arrival_time(table)

   ComplitProsess=table[0][1]
   StartProsess=ComplitProsess
   global prosess
   global time
   time=str(ComplitProsess)+"  "
   sum=0
   for i in range(len(table)):
      #Complete Time
      ComplitProsess=ComplitProsess+table[i][2]
      table[i][3]=ComplitProsess
      #T.A.T.c
      table[i][4]=table[i][3]-table[i][1]
      #W.T.
      table[i][5]=table[i][4]-table[i][2]
      #Average
      sum=sum+table[i][5]

      #gentt chart
      prosess=prosess+str(table[i][0])+" "
      time=time+str(ComplitProsess)+"  "
      # print('\n'+str(table[i][0])+' start with',str(StartProsess)+' ms','& end with',str(ComplitProsess)+' ms')
      StartProsess=StartProsess+table[i][2]

   #PRINT
   Display(prosess,time,table,sum)


def ShortTextNextJob():
   table=Insert_Element()
   #check is all prosess came in same time or not
   NoTCameSameTime=IsItCameInZeroTime(table)
   CameSameTime=not NoTCameSameTime

   #sort table before calculation
   if CameSameTime:
      Sort.as_burst_time(table)
   else:
      Sort.as_arrival_time(table)

   CompleteProsess=table[0][1]
   StartProsess=CompleteProsess
   global prosess
   global time
   time=str(CompleteProsess)+"  "
   sum=0 #sumation of wating time
   i=0
   while i<len(table):
      if CompleteProsess>=table[i][1]:
         #Complete Time
         CompleteProsess=CompleteProsess+table[i][2]
         table[i][3]=CompleteProsess

         #T.A.T.
         table[i][4]=table[i][3]-table[i][1]

         #W.T.
         table[i][5]=table[i][4]-table[i][2]

         #Average
         sum=sum+table[i][5]
         
         #gentt chart
         prosess=prosess+str(table[i][0])+" "
         time=time+str(CompleteProsess)+"  "
         StartProsess=StartProsess+table[i][2]
         
         if NoTCameSameTime:
            end=0
            for k in range(i+1,len(table)):
               if (CompleteProsess>=table[k][1]): 
                  end=end+1
            Sort.as_burst_time(table,i+1,end+1)
         i=i+1
      else:
         CompleteProsess=CompleteProsess+1
   #PRINT table
   Display(prosess,time,table,sum)


def Priority():
   headers.insert(1,'Priority')
   table=Insert_Element(4)

   NoTCameSameTime=IsItCameInZeroTime(table,2)
   CameSameTime=not NoTCameSameTime #to make code more understandable

   if CameSameTime:
      Sort.as_priority(table)
   else:
      Sort.as_arrival_time(table,True)

   CompleteProsess=table[0][2]
   StartProsess=CompleteProsess
   global prosess
   global time
   idel=0
   time=str(CompleteProsess)+"  "
   sum=0
   i=0
   while i<len(table):
      if CompleteProsess>=table[i][2]:
         #Complete Time
         CompleteProsess=CompleteProsess+table[i][3]
         table[i][4]=CompleteProsess
         #T.A.T.c
         table[i][5]=table[i][4]-table[i][2]
         #W.T.
         table[i][6]=table[i][5]-table[i][3]
         #Average
         sum=sum+table[i][6]

         #gentt chart
         prosess=prosess+str(table[i][0])+" "
         time=time+str(CompleteProsess)+"  "
         StartProsess=CompleteProsess

         if NoTCameSameTime:
            end=0
            for k in range(i+1,len(table)):
               if (CompleteProsess>=table[k][2]):
                  end=end+1
            Sort.as_priority(table,i+1,end+1)
         i=i+1
      else:
         CompleteProsess=CompleteProsess+1
   #PRINT table
   Display(prosess,time,table,sum)


def RoundRobin():
   unit=int(input("Enter unit: "))
   table=Insert_Element()
   
   stack=[]
   Sort.as_arrival_time(table)
   
   for i in range(len(table)):
      stack.append(table[i][2])
   CompleteProsess=table[0][1]
   StartProsess=CompleteProsess
   global prosess
   global time
   time=str(CompleteProsess)+"  "
   i=0
   while i<len(table):
      #Complete Time
      if CompleteProsess>=table[i][1]:
         if stack[i]:
            if stack[i]>unit:
               stack[i]=stack[i]-unit
               CompleteProsess=CompleteProsess+unit
            else:
               CompleteProsess=CompleteProsess+stack[i]
               stack[i]=0
            table[i][3]=CompleteProsess

            #gentt chart
            prosess=prosess+str(table[i][0])+" "
            time=time+str(CompleteProsess)+"  "
            StartProsess=CompleteProsess
         if i==len(stack)-1 and sum(stack)!=0:
            i=0
         else:
            i=i+1
      else:
            CompleteProsess=CompleteProsess+1

   
   sumation=0
   for i in range(len(table)):
      #T.A.T.
      table[i][4]=table[i][3]-table[i][1]
      #W.T.
      table[i][5]=table[i][4]-table[i][2]
      #Average
      sumation=sumation+table[i][5]
   #PRINT Table
   Display(prosess,time,table,sumation)





try:
   user_input = 'Y'
   while user_input != 'N':
      headers=['PROCESS','Arival','Burst','Complete','TAT','Wating']
      prosess=" "
      time=""
      try:
         print("\n\n[1] First Come First Service\n[2] ShortText Next Job\n[3] Priority\n[4] Round-Robin\n")
         chose=input("Enter number of Algorithm you wanna execute: ")
         if chose=='1':
            FirstComeFirstService()
         elif chose=='2':
            ShortTextNextJob()
         elif chose=='3':
            Priority()
         elif chose=='4':
            RoundRobin()
         user_input = input("\n\nDo you want to enter again? Y/N: ").upper()
      except Exception as e:
         print(f"\nAn error occurred: {e}\nso you can try again :)")
except Exception as e:
    print(f"An error occurred: {e}")