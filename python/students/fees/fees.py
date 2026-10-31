def fees():
    fees = {
        "student_id": 101,
        "name": "Nisha",
        "course": "BA",
        "total_fees": 20000,
        "paid_fees": 10000,
        "discount": 2000,
        "payment_date": "12-10-2026",
    
    }

    # fees["remaining_fees"] 
    fees["total_fees"]
    fees["discount"]
    fees["paid_fees"]

    print("Student:", fees["name"])
    print("Total Fees:", fees["total_fees"])
    print("Paid Fees:", fees["paid_fees"])
    # print("Remaining Fees:", fees["remaining_fees"])
    print(fees)
    
    return fees
