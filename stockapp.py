f=open("P:\\AI_Learn\\Hello\\stocks.csv","r")
out=open("P:\\AI_Learn\\Hello\\output.csv","w")
for i in f:
    row=i.split(',')
    if row[0]=="Company Name":
        out.write(row[0]+","+"PE Ratio"+"," + "PB Ratio" + "\n")
    else:
        m=round(int(row[1])/int(row[2]),2)
        n = round(int(row[1]) / int(row[3]), 2)
        out.write(row[0]+ "," +str(m)+","+str(n)+"\n")
f.close()
print(__name__)