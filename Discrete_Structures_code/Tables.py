#I want to make an algorithm that tries to fit several groups of friends 
#into an amount of tables arrangements of 8 spots each
#The algorithm should try to fit the groups in such a way that no group
#is split between tables if possible
#If a group is larger than 8, it cannot be split and
#a new special table should be created for them
#The algorithm should also try to minimize the number of tables used
#The algorithm should return the arrangement of tables and the groups assigned to each table

# class TableArrangement:
#     def __init__(self, groups):
#         self.groups = groups
#         self.tables = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Assuming a maximum of 10 tables for simplicity
#         self.remainder_groups = []
#
#     def arrange_tables(self):
#         # Sort groups in descending order to try to fit larger groups first
#         self.groups.sort(reverse=True)
#         
#         for group in self.groups:
#             if group > 8:
#                 # If the group is larger than 8, create a special table for them
#                 self.tables.append([group])
#             else:
#                 placed = False
#                 for table in self.tables:
#                     if sum(table) + group <= 8:
#                         table.append(group)
#                         placed = True
#                         break
#                 if not placed:
#                     # If the group couldn't be placed in any existing table,
#                     # append to a new list called remainder_groups
#                     self.remainder_groups.append(group)
#
#         return self.tables

class TableArrangement:
    def __init__(self, groups, allow_extra_tables=True):
        self.groups = groups
        self.allow_extra_tables = allow_extra_tables
        # Start with 10 empty tables, each with capacity 8
        self.tables = [[] for _ in range(10)]
        self.table_capacities = [8] * 10  
        self.remainder_groups = []  # oversized groups (>8)
        self.unseated = []          # groups that cannot be seated at all

    def arrange_tables(self):
        # Step 1: split normal vs oversized
        normal_groups = [friend_group for friend_group in self.groups if friend_group <= 8]
        self.remainder_groups = [friend_group for friend_group in self.groups if friend_group > 8]

        # Step 2: seat normal groups first (descending order)
        normal_groups.sort(reverse=True)
        for group in normal_groups:
            placed = False
            for i in range(len(self.tables)):
                if self.table_capacities[i] >= group:
                    self.tables[i].append(group)
                    self.table_capacities[i] -= group
                    placed = True
                    break
            if not placed:
                self.unseated.append(group)

        # Step 3: handle oversized groups
        for group in self.remainder_groups:
            extra_needed = group - 8
            adjusted = False

            # Try to steal capacity from last tables backwards
            for i in range(len(self.tables) - 1, -1, -1):
                if self.table_capacities[i] >= extra_needed:
                    # Create oversized table
                    self.tables.append([group])
                    self.table_capacities.append(0)
                    self.table_capacities[i] -= extra_needed
                    adjusted = True
                    break

            if not adjusted:
                if self.allow_extra_tables:
                    # Flexible mode: just add a new special table
                    self.tables.append([group])
                    self.table_capacities.append(0)
                else:
                    # Strict mode: no room → unseated
                    self.unseated.append(group)

        return self.tables, self.unseated, self.remainder_groups


if __name__ == "__main__":
    groups = [5, 3, 8, 10, 6, 10, 12, 4, 7, 6, 9]
    arrangement = TableArrangement(groups, allow_extra_tables=False)
    tables, unseated, oversized = arrangement.arrange_tables()
    print("Table Arrangements:", tables)
    print("Unseated Groups:", unseated)
    print("Oversized Groups:", oversized)