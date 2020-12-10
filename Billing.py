class Billing:
    def calculateBill(days):
        day_limit = 10
        per_day_fine = 10
        
        if days > day_limit:
            no_of_fine_days = days - day_limit
            total_fine = no_of_fine_days * per_day_fine
            print("Extra days are:",no_of_fine_days," Fine is Rs.",total_fine)
        else:
            print("Thankyou for returning the book on time")
