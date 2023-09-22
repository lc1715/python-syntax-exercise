def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    
    num = start 

    if num <= stop:                
        while num <= stop:
            print(num)
            num = num + 1
    else:
        while num >= stop:       
            print(num)
            num = num - 1 




    