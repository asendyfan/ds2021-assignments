
from datetime import timedelta

# inputFileName = input('the file name: ')
inputFile = open('marathon.txt', 'r')

# get all lines from the file, and delete enter symbol \n
lines = [line.replace('\n', '') for line in inputFile.readlines()]

rows: [str] = lines[1:]  # get each row exclude header
inputFile.close()  # close file


def lineCount() -> int:
    """Return the number of lines in file"""

    return len(rows)


def getCountryByRow(row: str) -> str:
    """Return country"""

    # after Skimming the txt, the easy way to get the data is delimited by ":", and then delimited by white space
    part3 = row.split(':')[2]
    countryParts = part3.split()[1:]
    return ' '.join(countryParts)


def runnerCountry(name: str) -> str:
    """Return the country that the runner name is representing"""

    for row in rows:
        rowSplit = row.split()
        playerName = rowSplit[0] + ' ' + rowSplit[1]  # Combine the first name and the last name
        if name == playerName:
            return getCountryByRow(row)


def countryInformation(countryName: str) -> [str]:
    """Return a list containing all rows containing information about runners from that country"""

    rowsSearchByCountry = []  # store the search result
    for row in rows:
        countryInRow = getCountryByRow(row)
        if countryName == countryInRow:
            rowsSearchByCountry.append(row)  # append the result
    return rowsSearchByCountry


def averageTime():
    """Return the average time that runners complete the London Marathon"""
    sumTime = timedelta(0)
    for row in rows:
        splitBySymbol = row.split(':')
        hour = float(splitBySymbol[0][-2:])  # get hour
        minute = float(splitBySymbol[1])  # get minute
        second = float(splitBySymbol[2][:2])  # get second
        sumTime += timedelta(hours=hour, minutes=minute, seconds=second)  # summarise time
    return str((sumTime / len(rows)))  # get averge time
