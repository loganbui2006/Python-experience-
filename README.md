# Python-experience-
Project/ Problem set that I used to complete and approach the problem. 
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
read_drinks() -> dict
**Purpose:** Reads and stores the drink menu configuration from user input.
**Process:**
- Reads the number of drink types from the first input line
- For each drink entry, parses the comma-separated format containing drink name and price
- Stores all drinks in a dictionary mapping drink names (as keys) to their prices (as float values)
- Returns the complete drink menu dictionary for use in order processing
