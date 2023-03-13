import csv

rec_path="Resources/budget_data.csv"

with open (rec_path, 'r') as csvfile:
# defining initial values for the variables     
    total_month=0
    total_amount=0
    prev_month=0
    #assuming that the values in "profits/losses" column are not positive( it's in rescession), it has to compare the first vlue with "-inf" rather than "0" to find the maximum.
    Lowest_amount = float("inf")
    Greatest_amount = float("-inf")
    differ_list=[]

    reader= csv.reader(csvfile , delimiter=',')
    header_row=next(csvfile)
    # calculating the increase/decrease amount between two months. prev_month is a variable to keep the previous amount in order to compare it with the next month obtained in the next loop
    for row in reader:
        total_amount+= int(row[1])
        total_month+= 1
        amount_differ=int(row[1])-prev_month
        
        if amount_differ > Greatest_amount :
            Greatest_amount =amount_differ
            Greatest_month=row[0]
            
        if amount_differ < Lowest_amount :
            Lowest_amount =amount_differ
            Lowest_month=str(row[0])
            

        differ_list.append(row[1])
        prev_month=int(row[1])

# the duration is from the first month to the last one,thus (1) should be subtracted from the "total_month" value 
    Average_Change =round((int(differ_list[-1])-int(differ_list[0]))/(total_month-1),2)

# the result will be written in a text file located in "analysis" folder and will not be shown in cmd, so its better to address it via a message!
print("The file runs successfully. Please find the results in 'analysis/output_file.txt' ")

#for the result, all the requested items are written in a txt file as bellow:
with open('analysis/output_file.txt', 'w') as outfile:
    
    outfile.write(f"Financial Analysis\n")
    outfile.write(f"----------------------------\n")
    outfile.write(f"Total Months: {total_month}\n")
    outfile.write(f"Total: $ {total_amount}\n")
    outfile.write(f"Average Change: $ {Average_Change}\n")
    outfile.write(f"Greatest Increase in Profits: {Greatest_month} ($ {Greatest_amount })\n")
    outfile.write(f"Greatest Decrease in Profits: {Lowest_month} ($ {Lowest_amount })\n")



        
    
    
