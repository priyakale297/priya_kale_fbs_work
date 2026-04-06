amount = int(input('Enter the amount:'))

denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

note_count = {}

remaining_amount = amount

for note in denominations:
    count = remaining_amount // note  
    if count > 0:
        note_count[note] = count
        remaining_amount -= note * count

print(f'Minimum number of notes for {amount}:')
total_notes = 0
for note, count in note_count.items():
    print(f'{note} : {count}')
    total_notes += count

print(f'Total notes needed: {total_notes}')