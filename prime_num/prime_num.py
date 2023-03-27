def num_checker(num):
    try:
        float(num)
    except: return 'Enter num, please'

    return '.' in str(num)

if __name__ == '__main__':
    print(num_checker(input('Enter num: ')))