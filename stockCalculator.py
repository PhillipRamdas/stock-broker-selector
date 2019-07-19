#Tejpal Ramdas and Richard Wong; 7/18/19; FinTechFocus Wells Fargo

#Display stock info nd provide info on returns based on user input

# csv file for data, parse for dictionaries
stockBrokers = {
    "TD": {"minDeposit":0,"FeePerTrade" : 6.95, "FeePerShare" : 0}, 
    "Cobra Trading" : {"minDeposit": 30000 ,"FeePerTrade" : 0, "FeePerShare" : 0.004}
   
}
stocks= {
    "AMD": {"currPrice": 33.06, "yearChange": 16.21},
    "GOOGL": {"currPrice": 1143.61, "yearChange": 1212.91}
}
choices = {}

def strStocks():
    s = "Stock choices: "
    for i in stocks:
        s += i + ", "
    return s

def countShares():
    count = 0
    for stock in choices:
        count += choices[stock]
    return count

def promptStockInput():
    stock = input("Which stock would you like to invest in? ")
    print(stock + " is $" + str(stocks[stock]["currPrice"]) + " per share")
    shares = input("How many shares would you like? ")
    return stock, shares

def overMin():
    total = 0
    brokers=[]
    for stock in choices:
        total += stocks[stock]["currPrice"]* choices[stock]
    for broker in stockBrokers:
        if stockBrokers[broker]["minDeposit"] <= total:
            brokers.append(broker)
    return brokers

def bestPossibleStockBroker(brokers):
    for broker in brokers:
        #Initializes lowestCost to number of trades times fee per trade + number of stocks traded times fee per stock traded
        lowestCost = len(choices)*stockBrokers[brokers[0]]["FeePerTrade"] + countShares()*stockBrokers[brokers[0]]["FeePerShare"]
        for broker in brokers:
            if (lowestCost > len(choices)*stockBrokers[broker]["FeePerTrade"] + countShares()*stockBrokers[broker]["FeePerShare"]):
                lowestCost = len(choices)*stockBrokers[broker]["FeePerTrade"] + countShares()*stockBrokers[broker]["FeePerShare"]
                lowestCostBroker = broker
        return broker , lowestCost

def main():
    moreStocks = True
    while (moreStocks):
        stock, shares = promptStockInput()
        choices[stock] = int(shares)
        moreStocks = input("Would you like add more stocks? (yes/no) ")
        if moreStocks.lower() == "yes":
            moreStocks = True
        else:
            moreStocks = False
    lowestbroker = bestPossibleStockBroker(overMin())
    print("You should choose " + lowestbroker[0] + "as your stock broker because it only costs you $" + str(lowestbroker[1]) + " for your initial trade.")

if(__name__=="__main__"):
    main()