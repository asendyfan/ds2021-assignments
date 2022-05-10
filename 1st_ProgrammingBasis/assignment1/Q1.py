
def main():
    """containing whole Question 1 code"""

    # Get input from user.
    name = input('your name: ')
    weight = input('your weight in kilograms (kg): ')
    height = input('your height in centimetres (cm): ')

    # Calculate BMI, the Body Mass Index (BMI).
    # turn the input value into float.
    # Formulate is kg/(m**2), so the height need to change unit.
    # Round to 2 decimal places at last.
    BMI = round(float(weight) / ((float(height)/100)**2), 2)

    # Get categorical name
    if BMI < 18.5:
        categoryName = 'underweight'
    elif BMI < 25:
        categoryName = 'healthy'
    elif BMI < 30:
        categoryName = 'overweight'
    else:
        categoryName = 'obese'

    # Get the result using join function of string.
    # BMI keep 2 decimal places
    result = ','.join([str(v) for v in [name, height, weight, "%.2f" % BMI, categoryName]])

    # write to the 'bmi.csv'
    outputFile = open('bmi.csv', 'a')
    print(result, file=outputFile)  # write result
    outputFile.close()


if __name__ == '__main__':
    main()
