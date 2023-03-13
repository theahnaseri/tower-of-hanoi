def TowerOfHanoi(n, from_tower, to_tower, aux_tower):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_tower, aux_tower, to_tower)

    to_tower.append(from_tower[-1])
    del from_tower[-1]
    print(source, helper, destin)
    TowerOfHanoi(n-1, aux_tower, to_tower, from_tower)


disk_count = int(input("disk count : "))
source = list(range(1, disk_count+1))
source.reverse()
destin = []
helper = []
print(source, helper, destin)
TowerOfHanoi(disk_count, source, destin, helper)
