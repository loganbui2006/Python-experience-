# Python-experience-
In this Project, I will need to process the input including drink definition and order records and then give the output of of sales analysis. 
# Starbuck Receipt and Revenue Report 
## Overview 
This assignment involves creating a Python program to process Starbucks coffee orders and generate a comprehensive sales report. The program handles drink definitions, customer orders with membership tiers, and produces formatted analytics including total sales, popular drinks, top customers, and membership-based revenue breakdown.

## Core Functionality
The system processes input data containing drink definitions and customer orders, then produces a formatted sales report with:
- Total revenue calculations with membership-based discounts
- Product performance analytics identifying top-selling drinks
- Customer spending analysis ranking users by total expenditure
- Membership tier breakdown showing revenue distribution across customer segments

## Function Explanations
**1. read_drinks() -> dict**  
Purpose: Reads and stores the drink menu configuration from user input.  
Process:
- Reads the number of drink types from the first input line
- For each drink entry, parses the comma-separated format containing drink name and price
- Stores all drinks in a dictionary mapping drink names (as keys) to their prices (as float values)
- Returns the complete drink menu dictionary for use in order processing  

**2. parse_order(order_str: str, drinks: dict) -> tuple**  
Purpose: Extracts and validates individual customer order information from input strings.  
Process:
- Splits the order string by commas into individual components
- Extracts customer email address and membership tier (converting to lowercase for consistency)
- Processes the list of purchased drinks, counting occurrences of each valid drink
- Validates each drink against the available menu, ignoring any invalid drink names
- Returns a tuple containing email, membership level, and a dictionary of drink quantities    

**3. calculate_total(items: dict, drinks: dict, membership: str) -> float**
Purpose: Computes the final order total after applying membership-based discounts.
Process:
- Calculates the subtotal by summing the product of each drink's price and quantity
- Applies tier-specific discounts: 10% for gold members, 5% for silver members, no discount for regular customers
- Rounds the final amount to 2 decimal places for proper currency formatting
- Returns the discounted order total  
**4.** generate_report() -> None  
Purpose: Orchestrates the entire sales reporting process and generates the formatted output.
Process:

**a.** Data Collection Phase:  
- Calls read_drinks() to load the drink menu
- Reads the number of customer orders and processes each order line    

**b.** Order Processing Phase:
- For each order, calls parse_order() to extract order details
- Uses calculate_total() to compute individual order totals  

**c.** Aggregates data across three dimensions:  
- drink_counts: Total quantity sold per drink type
- user_spending: Cumulative spending per customer
- tier_totals: Revenue breakdown by membership tier    

**d.** Analysis & Ranking Phase:
- Implements custom sorting to identify top 2 drinks by quantity sold (with alphabetical tie-breaking)
- Implements custom sorting to identify top 2 customers by total spending (with email tie-breaking)
- Calculates overall statistics: total sales and average order value
  
**e.** Report Generation Phase:  
- Outputs all results in the specified format with proper alignment
- Formats monetary values to 2 decimal places and percentages to 1 decimal place
- Ensures consistent capitalization and spacing throughout the report

