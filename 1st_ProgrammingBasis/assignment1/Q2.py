
inputFileName = input('the file name: ')
inputFile = open(inputFileName, 'r')

contents = inputFile.read()  # read all content from the file
tokens = contents.split()  # Tokens are delimited by white space('\n', ' ', '\t')

inputFile.close()   # close file


def countTokens() -> int:
    """Returns the count of all tokens in the text"""

    return len(tokens)


def countToken(particularToken: str) -> int:
    """ returns the frequency count of a particular token"""

    lowercaseParticularToken = particularToken.lower()  # Change particular token into lowercase.
    frequency = 0
    for token in tokens:  # iterate tokens in each line
        if lowercaseParticularToken == token.lower():  # compare
            frequency += 1
    return frequency


def normalisedFrequency(particularToken: str) -> float:
    """ returns the normalised frequency count of a particular token"""

    return countToken(particularToken) / countTokens()


def sentenceCount() -> float:
    """Return the number of sentences in the text"""

    sentencesNumber = contents.count('.')  # Assume that sentences are delimited by the full stop character
    return sentencesNumber


def sentencesContaining(searchContent: str) -> [str]:
    """returns a list of sentences containing a particular token, irrespective of case"""

    lowercaseSearchContent = searchContent.lower()  # change search content into lowercase

    # delete \n and \t, get sentences delimited by the full stop character
    sentences = contents\
        .replace('\n', '')\
        .replace('\t', '')\
        .split('.')

    results = []  # store searching results
    for sentence in sentences:  # iterate
        lowercaseSentence = sentence.lower()  # insensitive of case
        if lowercaseSentence.find(lowercaseSearchContent) > -1:  # find the searching content
            results.append(sentence)  # append the sentence
    return results
