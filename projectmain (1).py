import time
import random

options="yes"
Ticket_No=random.randint(0,200)
Category=[]
unit_cost=[]
total_qty=[]
total_cost=[]

LogoDate=time.strftime("%d/%m/%y",time.localtime(time.time()))
present_month_year=time.strftime("%m/%Y",time.localtime(time.time()))
Logoclock=time.strftime("%r",time.localtime(time.time()))
Datetime=time.strftime("%d/%m/%Y %H:%M:%S",time.localtime(time.time()))

print('*'*80)
print(LogoDate+"\t\t"+"Welcome To MoviBook"+"\t"+' '+Logoclock)
print('*'*80)
print("\t\t\t\t\t\t\t\t"+'Done By KAUSHIK')
print(' ')

def price_detail():
   print('')
   print("Price Details:")
   print(' ')
   print('Ticket Category Price')
   print('-'*30)
   print('Adult      100Rs')
   print('Child       20Rs')
   print('Senior      50Rs')
   print(' ')






def calculation():
   ticket_type=int(input("How many categories ticket do you want yo purchase?(1-3)"))
   if ticket_type>3 or ticket_type==0:
       print('Invalid type re-enter')
       print('')
       ticket_type=int(input("How many categories ticket do you want yo purchase?(1-3)"))
   print(' ')
   for i in range(ticket_type):
        choose_category=input('Choose a category as A for Adult/C for child/s \ for Senior:')
        if choose_category=='A':
                Adult_qty=int(input("How many adult tickets do you want to purchase? "))
                print(' ')
                Total_adult_price=Adult_qty*100
                CatType='Adult'
                Category.append(CatType)
                cost=100
                unit_cost.append(cost)
                total_qty.append(Adult_qty)
                total_cost.append(Total_adult_price)
        elif choose_category=='C':
                child_qty=int(input("How many child tickets do you want to purchase? "))
                print(' ')
                Total_child_price=child_qty*20
                CatType='Child'
                Category.append(CatType)
                cost=20
                unit_cost.append(cost)
                total_qty.append(child_qty)
                total_cost.append(Total_child_price)

        elif choose_category=='S':
                senior_qty=int(input("How many Senior tickets do you want to purchase? "))
                print(' ')
                Total_senior_price=senior_qty*50
                CatType='Senior'
                Category.append(CatType)
                cost=50
                unit_cost.append(cost)
                total_qty.append(senior_qty)
                total_cost.append(Total_senior_price)
        else:
                print(' ')
                print('Please choose a valid category.') 
                print(' ')

def card_detail():
    print(' ')
    print('Bill Details:')
    print(' ')
    print("Ticket Category",' \t',"Unit Cost",'\t\t',"Qty",'\t\t',"Total Cost")
    
    subtotal=0   
    for i in range(len(Category)):
       print(Category[i],'\t\t',unit_cost[i],'\t\t',total_qty[i],'\t\t',total_cost[i])
       subtotal=int(total_cost[i])+subtotal
       
    print('\t\t\t\t','-'*8)
    print('\t\t\t\t','Subtotal: ',str(subtotal),'Rs')
    print(' ')
    Tax_price=subtotal*0.18
    print('\t\t\t\t','Tax Amount(18%): ',str(Tax_price),'Rs')
    print('\t\t\t\t','-'*8)    
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total Pay amount:',str(Total),'Rs')
            
def ticket_receipt():
    print(' ')
    print('*'*18)
    print("Ticket No:",Ticket_No,"\t\t\t\t\t",'Date:',Datetime)
    print('*'*18)
    print("Ticket Category",'\t',"Unit Cost",'\t\t',"Qty",'\t\t',"Total Cost")  
    print(' ') 
    
    subtotal=0   
    for i in range(len(Category)):
       print(Category[i],'\t\t',unit_cost[i],'\t\t',total_qty[i],'\t\t',total_cost[i])
       subtotal=int(total_cost[i])+subtotal
       
    print('\t\t\t\t','-'*8)
    print('\t\t\t\t','Subtotal: ',str(subtotal),'Rs')
    print(' ')
    Tax_price=subtotal*0.18
    print('\t\t\t\t','Tax Amount(18%): ',str(Tax_price),'Rs')
    print('\t\t\t\t','-'*8)    
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total Pay amount:',str(Total),'Rs')


def data_write_file(Category,total_qty,unit_cost,total_cost):
    with open('transaction.txt','w') as f:
    
        f.write('*****************\n')
        f.write("Ticket No: %d\n"%Ticket_No)
        f.write(Datetime)
        f.write('\n')
        f.write('*****************\n')
        f.write('\n')

        for i in range(len(Category)):
            f.write('Category: ')
            f.write('%s\n'%Category[i])
            f.write('Qty: ')
            f.write('%d\n'%total_qty[i])
            f.write('Unit Cost: ')
            f.write('%d\n'%unit_cost[i])
            f.write('Total cost: ')
            f.write('%d\n'%total_cost[i])
            f.write('\n') 
    
    
        f.write('*****************\n')
        subtotal=0
        for i in range(len(total_cost)):
            subtotal=total_cost[i]+subtotal
        f.write("TotalCost(in Rs) %.f\n"%subtotal)
        Tax_price=subtotal*0.18
        Total=Tax_price+subtotal
        f.write("TotalCost with Tax(in Rs) %.f\n"%Total)
        f.write('*****************\n')
        f.close()

def purchase_ticket():
    print('The ticket categories are Adult,Child and Senior')
    print(' ')
    show_price=input('Do you want to know the price against categories? y/n')

    print(' ')
    if show_price in 'Y' or show_price in 'y':
       price_detail()
    elif show_price in 'N' or show_price in 'n':
       print("Let's purschase tickets")
       print(' ')
    else:
       print("Sorry your answer is not valid.")
       show_price=input('Do you want to know the price against categories? y/n')
       print(' ')
    
    calculation()
    print(' ')
    card_detail()
    print("Please enter your credit card details to proceed payment")
    print(' ')
    print('Credit card details: ')
    print('-'*20)

    Card_number=input('Enter your credit card number')
    if len(Card_number)<14 or len(Card_number)>14:
       print(' ')
       print('Invalid credit card number!! Try again')
       Card_number=input('Enter your credit card number') 
    print(' ')
    Exipary_date=input('Enter valid expiry date')
    if Exipary_date<=present_month_year:
        print('Invalid expiry date!! Try again')
        print(' ')
        Exipary_date=input('Enter valid expiry date')
        print(' ')
    print('Thank you for information.we are processing your payment.....')
    print(' ')
    print('You have successfully purchases the tickets.')
    print(' ')
    ticket_receipt()
    print(' ')
    print('Thank you for purschasing!!!!')
    data_write_file(Category,total_qty,unit_cost,total_cost)

while options in("yes","y","Y","Yes"):
      print("Selecting Options:")
      print("1.Show Price Details")
      print("2.Purchase Tickets")
      print("3.Exit")
      print('\n')
      choice=input("Enter a input")
      if choice=='1':
         price_detail()
         Buy_ticket=input("Do you want to purchase tickets ? y/n")
         print(' ') 
         if Buy_ticket in("y","Y"):
             purchase_ticket()
      elif choice=='2':
         purchase_ticket()
         
      elif choice=='3':
         print("Thanking you for visiting us!!!!")
         break
      else:
         print("Choose a valid option.")
         options='yes'               
      
      
