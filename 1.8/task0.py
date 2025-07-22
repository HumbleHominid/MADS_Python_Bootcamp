def calculate_revenue(sales_data: dict[str, tuple[int, int]]) -> int:
    return (
        sum(map(lambda item: item[1][0] * item[1][1], sales_data.items()))
        if sales_data
        else 0
    )


if __name__ == "__main__":
    sales_data = {"Laptop": (1000, 5), "Phone": (600, 10), "Tablet": (400, 7)}
    revenue = calculate_revenue(sales_data)
    print(revenue)
