# Tower Of Hanoi main algorithm function for n disks
def TowerOfHanoi(n, from_tower, to_tower, aux_tower):
	# Base case (continue until move all disks)
	if n == 0:
		return
	
	# Move subproblem of n-1 disks from source tower to helper tower
	TowerOfHanoi(n-1, from_tower, aux_tower, to_tower)

	# Print status
	print("Move disk %i from %s tower to %s tower" %(n, from_tower, to_tower))

	# Move subproblem of n-1 disks from helper tower to destination tower
	TowerOfHanoi(n-1, aux_tower, to_tower, from_tower)

# Get disk count from user
disk_count = int(input("disk count : "))

# Call main function
TowerOfHanoi(disk_count, '|Source|', '|Destin|', '|Helper|')