def TowerOfHanoi(n, from_tower, to_tower, aux_tower):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_tower, aux_tower, to_tower)
	print("Move disk %i from %s tower to %s tower" %(n, from_tower, to_tower))
	TowerOfHanoi(n-1, aux_tower, to_tower, from_tower)

disk_count = int(input("disk count : "))

TowerOfHanoi(disk_count, '|Source|', '|Destin|', '|Helper|')