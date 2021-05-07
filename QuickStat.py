import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import scipy.stats

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print("please input the file name")
fileName = input()
df = pd.read_csv("./dataStore/"+fileName)





def hypTest(df, headtitle, typeOfTest, hypothesis):
    if(typeOfTest == "confIntProportion"):
        sampleP = df[headtitle].mean()
        countN = df[headtitle].count()
        sEOM = math.sqrt(sampleP*(1-sampleP)/countN)
        bottomRange = sampleP-2*sEOM
        topRange = sampleP+2*sEOM
        print("there is a 95% probability that the true value of "+ headtitle+" is between "+str(bottomRange)+" and "+str(topRange))

    if(typeOfTest == "mean"):
        sampleM = df[headtitle].mean()
        countN = df[headtitle].count()
        varSamp = df[headtitle].var()*countN/(countN-1)
        stErr = (varSamp)/(math.sqrt(countN))
        degFree = countN-1
        tStat = abs((sampleM-hypothesis)/(stErr))
        prob = 2*scipy.stats.t.sf(tStat, df=degFree)   
        print("the probability of the sample "+ headtitle +" mean being equal to the true mean is "+str(prob))

while True:
    print("please enter command: enter help for help")
    useInput = input()

    if(useInput == "help"):
        print("end finishes the program \n hypTest performs hypothesis testing using t-tests or confidence intervals \n corrMatricx prints a correlation matrix \n showCorrMatrix creates a visualization for the correlation matrix \n properties prints the metadata of the data \n getData gets a user-inputted amount of data \n plotData plots a scatter plot between user-inputted headers \n EDA performs an exploratory data analysis \n testNull tests a column to find the amount of null values \n findUniqueValues tests a column to find the amount of unique values \n distribution provides a visualization of the distribution of data")

    if(useInput == "hypTest"):
        print("please enter header title")
        headTitle = input()
        print("please enter test type: currently supporting mean and confIntProportion")
        testType = input()

        hypothesis = 0
        if(testType == "mean"):
            print("please enter the hypothesis for the mean")
            hypothesis = input()

        hypTest(df, headTitle, testType, hypothesis)

    if(useInput == "end"):
        break

    if(useInput == "corrMatrix"):
        print("The correlation matrix of the data is as follows:")
        corrMatrix = df.corr()
        print(corrMatrix)

    if(useInput == "showCorrMatrix"):
        
        corrMatrix = df.corr()
        plt.matshow(corrMatrix)
        plt.xticks(range(len(corrMatrix.columns)), corrMatrix.columns, rotation=90);
        plt.yticks(range(len(corrMatrix.columns)), corrMatrix.columns);
        cb = plt.colorbar()
        cb.ax.tick_params(labelsize=14)
        plt.title("correlation matrix for data" , fontsize = 15)
        plt.show()


    if(useInput == "properties"):
        print("The properties of the data is as follows:")
        dataDescribe = df.describe()
        print(dataDescribe)

    if(useInput == "getData"):
        print("please input how many lines of data wanted")
        numOfLines = input()
        dataHead = df.head(int(numOfLines))
        print("The data is as follows:")
        print(dataHead)

    if(useInput == "plotData"):
        print("please input the header of the independent variable")
        independent = input()
        print("please input the header of the dependent variable")
        dependent = input()
        ax1 = df.plot.scatter(x=independent,
                      y=dependent,
                      c='DarkBlue')
        plt.title("Relationship between "+independent+" and "+dependent, fontsize = 15)
        plt.show()

    if(useInput == "EDA"):
        print("Column amount:")
        columnNum = len(df.columns)
        print(columnNum)

        print("Types of columns:")
        columnTypes = list(df.columns.values)
        print(columnTypes)

        print("Amount of observations:")
        rowNum = len(df)
        print(rowNum)

        print("Data types of columns:")
        datType = df.dtypes
        print(datType)

        hasEmpty = df.isnull().values.any()
        print("It is "+str(hasEmpty)+" that there are missing values in the dataset")

    if(useInput == "testNull"):
        hasEmpty = df.isnull().values.any()
        if(hasEmpty):
            print("Select the header to test")
            selectHead = input()
            amountNull = df[selectHead].isnull().sum()
            print("the amount of null values is "+amountNull)
        else:
            print("there are no null values in this dataset")
            
    if(useInput == "findUniqueValues"):
        print("Select the column name to test:")
        columnName = input()
        amountUnique = len(df[columnName].unique())
        print("There are "+str(amountUnique)+" unique values of data")

    if(useInput == "distribution"):
        print("please input which distribution is wanted")
        columnType = input()
        if(columnType == "all"):
            df.hist()
            plt.show()
        else:
            plt.title("Distribution of "+str(columnType)+" dataset")
            df[columnType].hist()
            plt.show()
