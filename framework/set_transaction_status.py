def set_transaction_status(se, be, t_number,r_number):
    if se is None and be is None:
        print("success")
    elif be is not None:
        print("bre status")
    else:
        print("se status")

    t_number += 1
    r_number = 0
    
    return t_number, r_number