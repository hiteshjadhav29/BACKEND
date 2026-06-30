cursor.executemany("""
# INSERT INTO Result (sid, sname, dcn, java, mic)
# VALUES (?, ?, ?, ?, ?)
# """, [
#     (1, 'Kunal', 85, 90, 88),
#     (2, 'Rahul', 78, 82, 80),
#     (3, 'Soham', 92, 89, 95),
#     (4, 'Amit', 70, 75, 72),
#     (5, 'Rohit', 88, 91, 87),
#     (6, 'Priya', 95, 93, 96),
#     (7, 'Sneha', 81, 84, 79),
#     (8, 'Neha', 76, 80, 78),
#     (9, 'Om', 89, 87, 90),
#     (10, 'Akash', 83, 85, 82)
# ])