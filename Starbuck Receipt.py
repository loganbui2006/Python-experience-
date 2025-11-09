def read_drinks():
    menu = {}
    types = int(input())
    for i in range(types):
        drink, price = input().strip().split(',')
        menu[drink] = float(price)
    return menu

def parse_order(order_str, drinks):
    parts = order_str.strip().split(',')
    email = parts[1]
    membership = parts[2].lower()
    item_counts = {}
    
    for item in parts[3:]:
        item_lower = item.lower()
        if item_lower in drinks:
            if item_lower in item_counts:
                item_counts[item_lower] += 1
            else:
                item_counts[item_lower] = 1
                
    return (email, membership, item_counts)

def calculate_total(items, drinks, membership):
    subtotal = 0.0
    for drink in items:
        subtotal += drinks[drink] * items[drink]
    if membership == 'gold':
        subtotal *= 0.9
    elif membership == 'silver':
        subtotal *= 0.95
    return round(subtotal, 2)

def generate_report():
    drinks = read_drinks()
    num_orders = int(input())
    
    all_orders = []
    drink_counts = {}
    user_spending = {}
    tier_totals = {'gold':0.0, 'silver':0.0, 'none':0.0}
    
    for _ in range(num_orders):
        order = input().strip()
        email, membership, items = parse_order(order, drinks)
        total = calculate_total(items, drinks, membership)
        
        all_orders.append((email, membership, total))
        
        # Update drink counts
        for drink in items:
            if drink in drink_counts:
                drink_counts[drink] += items[drink]
            else:
                drink_counts[drink] = items[drink]
        
        # Update user spending
        if email in user_spending:
            user_spending[email] += total
        else:
            user_spending[email] = total
        
        # Update tier totals
        tier_totals[membership] += total
    
    total_sales = sum(tier_totals.values())
    avg_order = total_sales / num_orders if num_orders > 0 else 0.0
    
    
    drink_list = []
    for drink in drink_counts:
        drink_list.append((drink, drink_counts[drink]))
    
    # Sort drinks by quantity (descending) then name (ascending)
    for i in range(len(drink_list)):
        for j in range(i+1, len(drink_list)):
            if (drink_list[i][1] < drink_list[j][1]) or \
               (drink_list[i][1] == drink_list[j][1] and drink_list[i][0] > drink_list[j][0]):
                drink_list[i], drink_list[j] = drink_list[j], drink_list[i]
    top_drinks = drink_list[:2]
    
  
    user_list = []
    for email in user_spending:
        user_list.append((email, user_spending[email]))
    
    # Sort users by spending (descending) then email (ascending)
    d = len(user_list)
    for i in range(d):
        for j in range(i+1, d):
            if (user_list[i][1] < user_list[j][1]) or \
               (user_list[i][1] == user_list[j][1] and user_list[i][0] > user_list[j][0]):
                user_list[i], user_list[j] = user_list[j], user_list[i]
    top_users = user_list[:2]
    

    print("==== Starbucks Sales Report ====")
    print("Total Sales: ${:.2f}".format(total_sales))
    print("Average Order Value: ${:.2f}".format(avg_order))
    print()
    
    print("Top 2 Drinks by Quantity:")
    for i in range(len(top_drinks)):
        drink = top_drinks[i][0]
        count = top_drinks[i][1]
        print("  {}. {:<15} {} sold".format(i+1, drink, count))
    
    print()
    print("Top 2 Users by Spending:")
    a = len(top_users)
    for i in range(a):
        email = top_users[i][0]
        total = top_users[i][1]
        membership = ""
        for order in all_orders:
            if order[0] == email:
                membership = order[1]
                break
        print("  {}. {:<15} ({})    ${:.2f}".format(i+1, email, membership, total))
    
    print()
    print("Membership Tier Sales:")
    for tier in ['gold', 'silver', 'none']:
        sales = tier_totals[tier]
        percent = (sales / total_sales * 100) if total_sales > 0 else 0.0
        print("  - {}: ${:.2f} ({:.1f}%)".format(tier.capitalize(), sales, percent))

if __name__ == "__main__":
    generate_report()
