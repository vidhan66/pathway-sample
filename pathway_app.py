import pathway as pw

# Define schema
class TemperatureSchema(pw.Schema):
    city: str
    temperature: int

# Create table from rows
t = pw.debug.table_from_rows(
    schema=TemperatureSchema,
    rows=[
        ("Delhi", 32),
        ("Mumbai", 30),
        ("Bangalore", 27),
    ]
)

# Transformation
result = t.select(
    city=t.city,
    temp_c=t.temperature,
    temp_f=t.temperature * 9 / 5 + 32
)

pw.debug.compute_and_print(result)
