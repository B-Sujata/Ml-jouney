class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        four_seats = 0
        reserved = {}
        # answer = 0
        if not reservedSeats:
            return n*2
        
        for row, seat in reservedSeats:
            if row in reserved:
                reserved[row].add(seat)
            else:
                reserved[row] = {seat}
        
        for row, seats in reserved.items():
            if not (seats & {2, 3, 4, 5}) and not (seats & {6, 7, 8, 9}) :
                four_seats+=2
            elif not (seats & {2, 3, 4, 5}):
                four_seats+=1
            elif not (seats & {6, 7, 8, 9}) :
                four_seats+=1
            elif not (seats & {4, 5, 6, 7}):
                four_seats+=1
            
            
        unaffected_rows = n - len(reserved)
        answer = four_seats+unaffected_rows*2
        return answer
        
        
'''
Approach

For each row, a family can occupy one of these 4-seat ranges:

2–5 → left group
4–7 → middle group
6–9 → right group

The left and right groups don't overlap, so if both are available, 2 families can sit in that row. If only one of them is available, 1 family can sit. If both are blocked, we check whether the middle group 4–7 is available.

Instead of processing all n rows, we store the reserved seats grouped by row using a dictionary. This allows us to process only the rows that actually contain reservations.

All rows that don't appear in the dictionary are completely empty and can automatically accommodate 2 families each.

Algorithm
Create a dictionary reserved where:
key = row number
value = set of reserved seats in that row.
Iterate through reservedSeats and populate the dictionary.
For every row containing reservations:
Check whether seats 2–5 are free.
Check whether seats 6–9 are free.
If both are free, add 2 families.
If either one is free, add 1 family.
If both are blocked, check seats 4–7.
If 4–7 is free, add 1 family; otherwise add 0.

Calculate the number of unaffected rows:

unaffected_rows = n - number of affected rows

Each unaffected row can accommodate 2 families, so add:

unaffected_rows × 2

Return the total number of families.
Complexity

Let m be the number of reserved seats.

Time Complexity: O(m)

Building the dictionary: O(m)
Processing affected rows: O(m) in the worst case
Checking each 4-seat range takes O(1) because each range contains only 4 seats.

Therefore:

Overall: O(m)

Space Complexity: O(m)

The dictionary stores the reserved seats, so in the worst case it can contain all m reservations.

Final

Time: O(m)
Space: O(m)
'''