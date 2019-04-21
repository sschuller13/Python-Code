#Sam Schuller
#Lab 6

#Q1
def show_functions():
    print '************************'
    print '1. Generate overall state for all prducts (total #, avg #, min, and max'
    print '2. Calculate the amount for a given product'
    print '3. Update the amount for a given product'
    print '************************'
    print ' '
    choice = int(input('These are the system functions: Choose 1, 2, or 3'))
return choice

def gen_stats(stock_dict):
    mini= min(stock_dict)
    maxi= max(stock_dict)
    avg= sum(stock_dict)/(stock_dict.count)
    total= sum(stock_dict)
    return total
    return avg
    return maxi
    return mini

print total
print avg
print maxi
print mini
def check_stock(stock_dict, prodName):
    product = raw_input('Enter the product you are checking')
    
return product

def update_stock(stock_dict, prodName, number):
    
    return number

List={product1:12,product2:8,product3:19,product4:4}
def main():
    continue = 1:
    while continue:
        if choice == 1:
            print '',gen_stats(List)
            raw= int(input('contine? 1 for yes, 0 for no'))
            if raw = 0:
                continue=0
        elif choice == 2:
            print '',check_stock(List,prodName)
            raw= int(input('contine? 1 for yes, 0 for no'))
            if raw = 0:
                continue=0
        elif choice == 3:
            print '',update_stock(List, prodName, number)
            raw= int(input('contine? 1 for yes, 0 for no'))
            if raw = 0:
                continue=0

if __name__ = __main__:
    main()
    
    
    
