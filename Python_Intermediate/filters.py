items = [
    ("Item01", 11),
    ("Item02", 12),
    ("Item03", 13)
]

# filtered_list = list(filter(lambda item: item[1] > 11, items))
filtered_list = [item for item in items if item[1] > 11] # a more clean expression
print(filtered_list)
