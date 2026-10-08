# Employee Salary Calculator
def calculate_salary(name, basic, bonus_pct, tax_pct):
    bonus = basic * bonus_pct / 100
    gross = basic + bonus
    tax = gross * tax_pct / 100
    final = gross - tax
    return {"name": name, "gross": gross, "tax": tax, "final": final}


employees = [
    ("Amit", 50000, 10, 12),
    ("Priya", 62000, 15, 15),
    ("Rahul", 45000, 8, 10),
    ("Sneha", 70000, 20, 18),
    ("Karan", 38000, 5, 5),
]

print(f"{'Name':<10}{'Gross':>12}{'Tax':>12}{'Final Salary':>16}")
for name, basic, bonus_pct, tax_pct in employees:
    r = calculate_salary(name, basic, bonus_pct, tax_pct)
    print(f"{r['name']:<10}{r['gross']:>12.2f}{r['tax']:>12.2f}{r['final']:>16.2f}")
