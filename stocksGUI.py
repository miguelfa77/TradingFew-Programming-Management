from graphics import *
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
matplotlib.use("TkAgg")

def chartAMZN(AMZN,maSmall, maLarge):
    
    plt.style.use('classic')

    AMZN[f'SMA-{maSmall}'] = AMZN['Adj Close'].rolling(window = maSmall).mean()
    AMZN[f'SMA-{maLarge}'] = AMZN['Adj Close'].rolling(window = maLarge).mean()
    AMZN = AMZN.iloc[maSmall:]

    longTrades = []
    shortTrades = []
    trade = 0

    for x in range(len(AMZN)):
        if AMZN[f'SMA-{maSmall}'].iloc[x] > AMZN[f'SMA-{maLarge}'].iloc[x] and trade != 1:
            longTrades.append(AMZN['Adj Close'].iloc[x])
            shortTrades.append(float('nan'))
            trade = 1
        elif AMZN[f'SMA-{maSmall}'].iloc[x] < AMZN[f'SMA-{maLarge}'].iloc[x] and trade != -1:
            shortTrades.append(AMZN['Adj Close'].iloc[x])
            longTrades.append(float('nan'))
            trade = -1
        else:
            longTrades.append(float('nan'))
            shortTrades.append(float('nan'))

    AMZN['Long Signals'] = longTrades
    AMZN['Short Signals'] = shortTrades

    plt.figure('AMZN')
    plt.xlabel('Days')
    plt.ylabel('Price in USD')
    plt.plot(AMZN['Adj Close'],label='AMZN Share Price', color='orange', linewidth=2.5, alpha=0.6) 
    plt.plot(AMZN[f'SMA-{maSmall}'],label=f'SMA-{maSmall}',linestyle = 'dashed', color='blue')
    plt.plot(AMZN[f'SMA-{maLarge}'], label=f'SMA-{maLarge}',linestyle = 'dashed', color='green')
    plt.scatter(AMZN.index, AMZN['Long Signals'], label='Long Signal', marker='^', color='green', linewidth=4)
    plt.scatter(AMZN.index, AMZN['Short Signals'], label='Short Signal', marker='v', color='red', linewidth=4)
    plt.title(label='AMZN Price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close('AMZN')

def chartAAPL(AAPL,maSmall, maLarge):

    plt.style.use('classic')

    AAPL[f'SMA-{maSmall}'] = AAPL['Adj Close'].rolling(window = maSmall).mean()
    AAPL[f'SMA-{maLarge}'] = AAPL['Adj Close'].rolling(window = maLarge).mean()
    AAPL = AAPL.iloc[maSmall:]
    
    longTrades = []
    shortTrades = []
    trade = 0

    for a in range(len(AAPL)):
        if AAPL[f'SMA-{maSmall}'].iloc[a] > AAPL[f'SMA-{maLarge}'].iloc[a] and trade != 1:
            longTrades.append(AAPL['Adj Close'].iloc[a])
            shortTrades.append(float('nan'))
            trade = 1
        elif AAPL[f'SMA-{maSmall}'].iloc[a] < AAPL[f'SMA-{maLarge}'].iloc[a] and trade != -1:
            shortTrades.append(AAPL['Adj Close'].iloc[a])
            longTrades.append(float('nan'))
            trade = -1
        else:
            longTrades.append(float('nan'))
            shortTrades.append(float('nan'))

    AAPL['Long Signals'] = longTrades
    AAPL['Short Signals'] = shortTrades
    plt.figure('AAPL')
    plt.xlabel('Days')
    plt.ylabel('Price in USD')
    plt.plot(AAPL['Adj Close'], label='AAPL Share Price', color='orange', linewidth=2.5, alpha=0.6)
    plt.plot(AAPL[f'SMA-{maSmall}'], label=f'SMA-{maSmall}',linestyle = 'dashed', color='blue')
    plt.plot(AAPL[f'SMA-{maLarge}'], label=f'SMA-{maLarge}',linestyle = 'dashed', color='green')
    plt.scatter(AAPL.index, AAPL['Long Signals'], label='Long Signal', marker='^', color='green', linewidth=4)
    plt.scatter(AAPL.index, AAPL['Short Signals'], label='Short Signal', marker='v', color='red', linewidth=4)
    plt.title(label='AAPL Price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close('AAPL')

def chartMETA(META,maSmall, maLarge):

    plt.style.use('classic')

    META[f'SMA-{maSmall}'] = META['Adj Close'].rolling(window = maSmall).mean()
    META[f'SMA-{maLarge}'] = META['Adj Close'].rolling(window = maLarge).mean()
    META = META.iloc[maSmall:]

    longTrades = []
    shortTrades = []
    trade = 0

    for m in range(len(META)):
        if META[f'SMA-{maSmall}'].iloc[m] > META[f'SMA-{maLarge}'].iloc[m] and trade != 1:
            longTrades.append(META['Adj Close'].iloc[m])
            shortTrades.append(float('nan'))
            trade = 1
        elif META[f'SMA-{maSmall}'].iloc[m] < META[f'SMA-{maLarge}'].iloc[m] and trade != -1:
            shortTrades.append(META['Adj Close'].iloc[m])
            longTrades.append(float('nan'))
            trade = -1
        else:
            longTrades.append(float('nan'))
            shortTrades.append(float('nan'))

    META['Long Signals'] = longTrades
    META['Short Signals'] = shortTrades

    plt.figure('META')
    plt.xlabel('Days')
    plt.ylabel('Price in USD')
    plt.plot(META['Adj Close'],label='META Share Price', color='orange',linewidth=2.5, alpha=0.6)
    plt.plot(META[f'SMA-{maSmall}'], label=f'SMA-{maSmall}',linestyle = 'dashed',color='blue')
    plt.plot(META[f'SMA-{maLarge}'], label=f'SMA-{maLarge}',linestyle = 'dashed',color='green')
    plt.scatter(META.index, META['Long Signals'], label='Long Signal', marker='^', color='green', linewidth=4)
    plt.scatter(META.index, META['Short Signals'], label='Short Signal', marker='v', color='red', linewidth=4)
    plt.title(label='META Price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close('META')

def chartGOOG(GOOG,maSmall, maLarge):
    
    plt.style.use('classic')

    GOOG[f'SMA-{maSmall}'] = GOOG['Adj Close'].rolling(window = maSmall).mean()
    GOOG[f'SMA-{maLarge}'] = GOOG['Adj Close'].rolling(window = maLarge).mean()
    GOOG = GOOG.iloc[maSmall:]

    longTrades = []
    shortTrades = []
    trade = 0

    for g in range(len(GOOG)):
        if GOOG[f'SMA-{maSmall}'].iloc[g] > GOOG[f'SMA-{maLarge}'].iloc[g] and trade != 1:
            longTrades.append(GOOG['Adj Close'].iloc[g])
            shortTrades.append(float('nan'))
            trade = 1
        elif GOOG[f'SMA-{maSmall}'].iloc[g] < GOOG[f'SMA-{maLarge}'].iloc[g] and trade != -1:
            shortTrades.append(GOOG['Adj Close'].iloc[g])
            longTrades.append(float('nan'))
            trade = -1
        else:
            longTrades.append(float('nan'))
            shortTrades.append(float('nan'))

    GOOG['Long Signals'] = longTrades
    GOOG['Short Signals'] = shortTrades

    plt.figure('GOOG')
    plt.xlabel('Days')
    plt.ylabel('Price in USD')
    plt.plot(GOOG['Adj Close'], label='GOOG Share Price', color='orange', linewidth=2.5, alpha=0.6)
    plt.plot(GOOG[f'SMA-{maSmall}'], label=f'SMA-{maSmall}',linestyle = 'dashed',color='blue')
    plt.plot(GOOG[f'SMA-{maLarge}'], label=f'SMA-{maLarge}',linestyle = 'dashed',color='green')
    plt.scatter(GOOG.index, GOOG['Long Signals'], label='Long Signal', marker='^', color='green', linewidth=4)
    plt.scatter(GOOG.index, GOOG['Short Signals'], label='Short Signal', marker='v', color='red', linewidth=4)
    plt.title(label='GOOG Price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close('GOOG')


def chartNFLX(NFLX,maSmall, maLarge):

    plt.style.use('classic')

    NFLX[f'SMA-{maSmall}'] = NFLX['Adj Close'].rolling(window = maSmall).mean()
    NFLX[f'SMA-{maLarge}'] = NFLX['Adj Close'].rolling(window = maLarge).mean()
    NFLX = NFLX.iloc[maSmall:]

    longTrades = []
    shortTrades = []
    trade = 0

    for n in range(len(NFLX)):
        if NFLX[f'SMA-{maSmall}'].iloc[n] > NFLX[f'SMA-{maLarge}'].iloc[n] and trade != 1:
            longTrades.append(NFLX['Adj Close'].iloc[n])
            shortTrades.append(float('nan'))
            trade = 1
        elif NFLX[f'SMA-{maSmall}'].iloc[n] < NFLX[f'SMA-{maLarge}'].iloc[n] and trade != -1:
            shortTrades.append(NFLX['Adj Close'].iloc[n])
            longTrades.append(float('nan'))
            trade = -1
        else:
            longTrades.append(float('nan'))
            shortTrades.append(float('nan'))

    NFLX['Long Signals'] = longTrades
    NFLX['Short Signals'] = shortTrades

    plt.figure('NFLX')
    plt.xlabel('Days')
    plt.ylabel('Price in USD')
    plt.plot(NFLX['Adj Close'],label='NFLX Share Price', color='orange', linewidth=2.5, alpha=0.6)
    plt.plot(NFLX[f'SMA-{maSmall}'], label=f'SMA-{maSmall}',linestyle = 'dashed', color='blue')
    plt.plot(NFLX[f'SMA-{maLarge}'], label=f'SMA-{maLarge}',linestyle = 'dashed', color='green')
    plt.scatter(NFLX.index, NFLX['Long Signals'], label='Long Signal', marker='^', color='green', linewidth=4)
    plt.scatter(NFLX.index, NFLX['Short Signals'], label='Short Signal', marker='v', color='red', linewidth=4)
    plt.title(label='NFLX Price')
    plt.legend(loc='upper left')
    plt.show()
    plt.close('NFLX')

def show(win, maSmallEntry, maLargeEntry, AMZN, NFLX, GOOG, AAPL, META):

    while True:
        pt = win.getMouse()
        if pt.getY() > 100 and pt.getY() < 140:
            if pt.getX() > 100 and pt.getX() < 300:
                maSmall = int(maSmallEntry.getText())
                maLarge = int(maLargeEntry.getText())
                chartAMZN(AMZN, maSmall, maLarge)
        elif pt.getY() > 180 and pt.getY() < 220:
            if pt.getX() > 100 and pt.getX() < 300:
                maSmall = int(maSmallEntry.getText())
                maLarge = int(maLargeEntry.getText())
                chartNFLX(NFLX, maSmall, maLarge)
        elif pt.getY() > 240 and pt.getY() < 300:
            if pt.getX() > 100 and pt.getX() < 300:
                maSmall = int(maSmallEntry.getText())
                maLarge = int(maLargeEntry.getText())
                chartGOOG(GOOG, maSmall, maLarge)
        elif pt.getY() > 320 and pt.getY() < 380:
            if pt.getX() > 100 and pt.getX() < 300:
                maSmall = int(maSmallEntry.getText())
                maLarge = int(maLargeEntry.getText())
                chartAAPL(AAPL, maSmall, maLarge)
        elif pt.getY() > 400 and pt.getY() < 460:
            if pt.getX() > 100 and pt.getX() < 300:
                maSmall = int(maSmallEntry.getText())
                maLarge = int(maLargeEntry.getText())
                chartMETA(META, maSmall, maLarge)
        
        elif pt.getY() > 0 and pt.getY() < 20:
            if pt.getX() > 380 and pt.getX() < 400:
                win.close()
                sys.exit()

def main():

# IMPORT CSV FILE AS DATAFRAME AS NAME OF COMPANY

    # dataframe list (dataframe)
    companies = ['AMZN','AAPL','META','GOOG','NFLX']

    i = 0
    for company in companies:
        companies[i] = pd.read_csv(f'{companies[i]}.csv')
        companies[i] = pd.DataFrame(companies[i])
        i += 1

# DATA SCRUBBING:

    AMZN = companies[0].dropna()
    # print(AMZN.isnull().values.any())
    AAPL = companies[1].dropna()
    META = companies[2].dropna()
    GOOG = companies[3].dropna()
    NFLX = companies[4].dropna()

    print(AMZN)

# GUI
    win = GraphWin('TradingFew', 400, 600)
    win.setBackground("black")

    title = Text(Point(200,80), "TradingFew - By Traders, For Traders.")
    title.setSize(15)
    title.setTextColor("green")
    title.draw(win)

    myImage = Image(Point(200,35), "TradingFew.gif.png")
    myImage.draw(win)

# buttons FAANG
    AMZNpt = Rectangle(Point(100,100), Point(300,140))
    AMZNpt.setOutline("green")
    AMZNpt.setFill("black")
    AMZNpt.draw(win)
    AMZNtext = Text(Point(200,120), "$AMZN")
    AMZNtext.setTextColor("green")
    AMZNtext.setSize(15)
    AMZNtext.draw(win)

    NFLXpt = Rectangle(Point(100,180), Point(300,220))
    NFLXpt.setOutline("green")
    NFLXpt.setFill("black")
    NFLXpt.draw(win)
    NFLXtext = Text(Point(200,200), "$NFLX")
    NFLXtext.setTextColor("green")
    NFLXtext.setSize(15)
    NFLXtext.draw(win)

    GOOGpt = Rectangle(Point(100,260), Point(300,300))
    GOOGpt.setOutline("green")
    GOOGpt.setFill("black")
    GOOGpt.draw(win)
    GOOGtext = Text(Point(200,280), "$GOOG")
    GOOGtext.setTextColor("green")
    GOOGtext.setSize(15)
    GOOGtext.draw(win)

    AAPLpt = Rectangle(Point(100,340), Point(300,380))
    AAPLpt.setOutline("green")
    AAPLpt.setFill("black")
    AAPLpt.draw(win)
    AAPLtext = Text(Point(200,360), "$AAPL")
    AAPLtext.setTextColor("green")
    AAPLtext.setSize(15)
    AAPLtext.draw(win)

    METApt = Rectangle(Point(100,420), Point(300,460))
    METApt.setOutline("green")
    METApt.setFill("black")
    METApt.draw(win)
    METAtext = Text(Point(200,440), "$META")
    METAtext.setTextColor("green")
    METAtext.setSize(15)
    METAtext.draw(win)

    maSmalltext = Text(Point(132, 500),"SMA 1 (10, 30, 50): ")
    maSmalltext.setTextColor("green")
    maSmalltext.setSize(15)
    maSmalltext.draw(win)
    maSmallEntry = Entry(Point(230,500), 5)
    maSmallEntry.setTextColor("black")
    maSmallEntry.draw(win)

    maLargetext = Text(Point(126, 540),"SMA 2 (60, 100, 200): ")
    maLargetext.setTextColor("green")
    maLargetext.setSize(15)
    maLargetext.draw(win)
    maLargeEntry = Entry(Point(230,540), 5)
    maLargeEntry.setTextColor("black")
    maLargeEntry.draw(win)

    exitButton = Rectangle(Point(380,0), Point(400, 20))
    exitButton.setOutline("red")
    exitButton.setFill("red")
    exitButton.draw(win)
    exitText = Text(Point(390,10), "X")
    exitText.setTextColor("white")
    exitText.setSize(10)
    exitText.draw(win)

# GUI INTERACTION
    show(win, maSmallEntry, maLargeEntry, AMZN, NFLX, GOOG, AAPL, META)


main()
