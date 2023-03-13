# Tower Of Hanoi main algorithm function for n disks
def TowerOfHanoi(n, from_tower, to_tower, aux_tower):
    # Base case (continue until move all disks)
    if n == 0:
        return

    # Move subproblem of n-1 disks from source tower to helper tower
    TowerOfHanoi(n-1, from_tower, aux_tower, to_tower)

    # Move disk to destination tower and print towers
    to_tower.append(from_tower[-1])
    del from_tower[-1]
    print(source, helper, destin)

    # Move subproblem of n-1 disks from helper tower to destination tower
    TowerOfHanoi(n-1, aux_tower, to_tower, from_tower)


# Get disk count from user
disk_count = int(input("disk count : "))

# Initialize towers
source = list(range(1, disk_count+1))
source.reverse()
destin = []
helper = []
print(source, helper, destin)

# Call main function
TowerOfHanoi(disk_count, source, destin, helper)
