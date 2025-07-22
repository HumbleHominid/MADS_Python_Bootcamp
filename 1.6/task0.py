sales_revenue = [
    32000,
    45000,
    38000,
    50000,
    47000,
    52000,
    61000,
    49000,
    53000,
    60000,
    58000,
    62000,
]

print(f"March sales revenue: {sales_revenue[2]:,}")
print(f"Total sales revenue for Q3: {sum(sales_revenue[6:9]):,}")
max_sales = max(sales_revenue)
min_sales = min(sales_revenue)
print(f"Maximum sales revenue: {max_sales:,}")
print(f"Minimum sales revenue: {min_sales:,}")
print(f"50,000 does{'' if 50000 in sales_revenue else ' not'} appear in the sales data")
