def get_transaction_data(t_data,t_item,t_number:int):
    print('getting transaction number, loggin here')

    if t_number <= len(t_data):
        t_item = t_data[t_number - 1]
    else:
        t_item = None
    
    if t_item is not None:
        print("t_item logging here")

    return t_item