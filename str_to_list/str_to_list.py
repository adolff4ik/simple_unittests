def str_to_list(string):
    List = string.split(' ')
    while '' in List:
        List.remove('')
    return List

if __name__ == '__main__':
    print(str_to_list(input('Enter string of words separated by spaces: ')))
