from decimal import Decimal, ROUND_HALF_UP

# addition example
print(Decimal('10.34') + Decimal('2.66'))  # 13.0

# rounding example
value = Decimal('2234')
rounded_value = value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(rounded_value)
