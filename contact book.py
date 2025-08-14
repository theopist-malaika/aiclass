contact_book={}

contact_book["Emma"]="0993046123"
contact_book["Eric"]="0999636478"
contact_book["Theo"]="0887585317"
contact_book["Ma Joshua"]="0995624548"

for item in contact_book.keys():
    print(item)

for phone_number in contact_book.values():
    print(phone_number)

for item, phone_number in contact_book.items():
    print(f"{item}: {phone_number}")

