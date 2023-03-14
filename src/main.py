# Define towers as an object
class Towers:
    # Initialize tower
    def __init__(self, disks_count):
        self.disks_count = disks_count

        # Make a list of towers list
        self.towers = [[]] * 3

        # Define source tower list which have numbers as disks : [disks_count, disks_count-1, ..., 1]
        self.towers[0] = [i for i in range(self.disks_count, 0, -1)]

        # Define helper tower which is empty : []
        self.towers[1] = []

        # Define helper tower which is empty : []
        self.towers[2] = []

    # Print the towers in which steps
    def __str__(self):
        output = ''
        for i in range(self.disks_count, -1, -1):  # Choose disk
            for j in range(3):  # Choose tower
                if len(self.towers[j]) > i:
                    output += ' ' + str(self.towers[j][i])
                else:
                    output += ' -'
            output += '\n'
        return output + '~.~ ~.~\n'

    # Move disk from source tower to destination tower
    def move(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)

# Tower Of Hanoi main algorithm function for n disks


def TowerOfHanoi(towers, n, from_tower, to_tower, aux_tower):
    # Base case (continue until move all disks)
    if n == 0:
        return

    # Move subproblem of n-1 disks from source tower to helper tower
    TowerOfHanoi(towers, n-1, from_tower, aux_tower, to_tower)

    # Move disk to destination tower and print towers
    towers.move(from_tower, to_tower)
    print(towers)

    # Move subproblem of n-1 disks from helper tower to destination tower
    TowerOfHanoi(towers, n-1, aux_tower, to_tower, from_tower)


# Welcome
print("===> Hello, Welcome to Hanoi Tower Solver <=== \n")

# Get disk count from user
_disks_count = int(input("Enter the disk count : "))

# Run until user enter 0
while _disks_count != 0:
    # Make towers object and print it
    t = Towers(_disks_count)
    print(t)

    # Call main function
    TowerOfHanoi(t, t.disks_count, 0, 2, 1)

    # Takes the disks count from user
    _disks_count = int(
        input("Enter the disk count (Enter 0 if you want to end this!) : "))

# Developers
print("\nThank you for choosing us :)\n>>>Developed by Maryam Fakhraei and Amirhossein Naseri<<<")
