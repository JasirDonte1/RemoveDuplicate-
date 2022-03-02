'''
Create a function that takes in a string as a parameter and returns an array of
the characters from the string without any duplicate characters  

'''


def removeDuplicate(word):
    # your code goes here
    # create empty list called tempArr
    # traverse through char array
    # check if char is in tempArr
    # if not add char to tempArr
    # order list then return it. 
    tempArr = []
    array = list(word)
    for ch in array:
        if ch not in tempArr:
            tempArr.append(ch)
    tempArr.sort()
    return tempArr

if __name__ == '__main__':
    word = 'HackerRank'
    print(average(word))
