def read_drinks():
    """Reads drink menu from input and returns dictionary mapping drink names to prices."""
    menu = {}
    try:
        types = int(input().strip())
        for i in range(types):
            drink_data = input().strip().split(',')
            if len(drink_data) == 2:
                drink, price = drink_data
                menu[drink.lower()] = float(price)
    except ValueError:
        print("Error: Invalid input format for drinks")
    return menu

def parse_order(order_str, drinks):
    """Parses order string and returns email, membership, and item counts."""
    parts = order_str.strip().split(',')
    if len(parts) < 4:
        return None
    
    email = parts[1]
    membership = parts[2].lower()
    item_counts = {}
    
    for item in parts[3:]:
        item_lower = item.lower()
        if item_lower in drinks:
            item_counts[item_lower] = item_counts.get(item_lower, 0) + 1
                
    return (email, membership, item_counts)

def calculate_total(items, drinks, membership):
    """Calculates total order cost with membership discounts."""
    subtotal = 0.0
    for drink, quantity in items.items():
        subtotal += drinks[drink] * quantity
    
    discount_multipliers = {'gold': 0.9, 'silver': 0.95, 'none': 1.0}
    multiplier = discount_multipliers.get(membership, 1.0)
    
    return round(subtotal * multiplier, 2)

def generate_report():
    """Main function to generate Starbucks sales report."""
    drinks = read_drinks()
    if not drinks:
        print("Error: No drinks defined")
        return
    
    try:
        num_orders = int(input().strip())
    except ValueError:
        print("Error: Invalid number of orders")
        return
    
    all_orders = []
    drink_counts = {}
    user_spending = {}
    tier_totals = {'gold': 0.0, 'silver': 0.0, 'none': 0.0}
    user_memberships = {}
    
    for _ in range(num_orders):
        try:
            order = input().strip()
            if not order:
                continue
                
            order_data = parse_order(order, drinks)
            if order_data is None:
                continue
                
            email, membership, items = order_data
            
            if not items:
                continue
                
            total = calculate_total(items, drinks, membership)
            
            all_orders.append((email, membership, total, items))
            user_memberships[email] = membership
            
            for drink, quantity in items.items():
                drink_counts[drink] = drink_counts.get(drink, 0) + quantity
            
            user_spending[email] = user_spending.get(email, 0.0) + total
            tier_totals[membership] += total
            
        except Exception as e:
            continue
    
    if not all_orders:
        print("No valid orders to process")
        return
    
    total_sales = sum(tier_totals.values())
    avg_order = total_sales / len(all_orders)
    
    # Sort drinks by quantity descending, then name ascending
    drink_list = sorted(drink_counts.items(), key=lambda x: (-x[1], x[0]))
    top_drinks = drink_list[:2]
    
    # Sort users by spending descending, then email ascending
    user_list = sorted(user_spending.items(), key=lambda x: (-x[1], x[0]))
    top_users = user_list[:2]
    
    print("==== Starbucks Sales Report ====")
    print(f"Total Sales: ${total_sales:.2f}")
    print(f"Average Order Value: ${avg_order:.2f}")
    print()
    
    print("Top 2 Drinks by Quantity:")
    for i, (drink, count) in enumerate(top_drinks, 1):
        print(f"  {i}. {drink:<15} {count} sold")
    
    print()
    print("Top 2 Users by Spending:")
    for i, (email, total) in enumerate(top_users, 1):
        membership = user_memberships.get(email, 'none')
        print(f"  {i}. {email:<15} ({membership})    ${total:.2f}")
    
    print()
    print("Membership Tier Sales:")
    for tier in ['gold', 'silver', 'none']:
        sales = tier_totals[tier]
        percentage = (sales / total_sales * 100) if total_sales > 0 else 0.0
        print(f"  - {tier.capitalize()}: ${sales:.2f} ({percentage:.1f}%)")

if __name__ == "__main__":
    generate_report()
