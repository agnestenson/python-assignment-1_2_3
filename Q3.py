# Q3: Online Shopping Discount Eligibility

# 1. Accept the order amount and membership status
# replace(",", "") lets the user type amounts like 1,00,001 as well
amount_text = input("Enter the order amount (in Rs): ")
order_amount = float(amount_text.replace(",", ""))

# 2. Handle membership without case sensitivity (YES, Yes, yes, ...)
membership = input("Are you a member? (yes/no): ").strip().lower()

# 3. Boolean expressions for validation
is_member = membership == "yes"
valid_membership_input = membership == "yes" or membership == "no"
invalid_amount = order_amount < 0 or order_amount > 100000

# 4. Decide the discount percentage using the business rules
if not valid_membership_input:
    print("Invalid membership status. Please enter 'yes' or 'no'.")
elif invalid_amount:
    print("Order amount:", order_amount)
    print("Eligibility status: Invalid order (amount must be between 0 and 1,00,000).")
else:
    if order_amount >= 5000:
        discount_percent = 15
        status = "Eligible for 15% discount (order of Rs 5,000 or more)"
    elif is_member and order_amount >= 2000:
        discount_percent = 10
        status = "Eligible for 10% member discount"
    else:
        discount_percent = 0
        status = "Not eligible for any discount"

    # 5. Calculate and display the results
    discount_amount = order_amount * discount_percent / 100
    final_amount = order_amount - discount_amount

    print("Original amount   : Rs", order_amount)
    print("Discount amount   : Rs", discount_amount)
    print("Final payable     : Rs", final_amount)
    print("Eligibility status:", status)
