from aiohttp.helpers import validate_etag_value
from dask.array import left_shift


def input_num():
    value = input("Please input a number between 0 to 8")
    try:
        value = int(value)
        if value >= 0 and value <= 8:
            return value
        else:
            print("Please input a number between 0 to 8")
            return input_num()
    except ValueError:
        print("Please input a number between 0 to 8")
        return input_num()


def parentheses_generate(number,print_item=None):
    value=number
    if print_item is None:
        print_item=[]

    if value>0:
        if value==1:
            print_item=["()"]
            return print_item
        else:
            previous=parentheses_generate(value-1,print_item)
            new_list=[]
            for item in previous:
            #left
                new_list.append(f"{item}()")
            #right
                new_list.append(f"(){item}")
            #middle
                new_list.append(f"({item})")

            print_item=list(set(new_list))

            return print_item


number=input_num()
results=parentheses_generate(number)
print(results)
