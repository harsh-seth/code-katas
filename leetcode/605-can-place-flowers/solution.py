def canPlaceFlowers(flowerbed, n):
    temp = [0] + flowerbed + [0]
    i = 1
    while n != 0 and i < len(temp) - 1:
        if temp[i-1:i+2] == [0, 0, 0]:
            temp[i] = 1
            n -= 1
        i += 1
    return n == 0

flowerbed = [1, 0, 0, 0, 1]
n = 1
assert canPlaceFlowers(flowerbed, n) == True

flowerbed = [1, 0, 0, 0, 1]
n = 2
assert canPlaceFlowers(flowerbed, n) == False

flowerbed = [1, 0, 0, 0]
n = 1
assert canPlaceFlowers(flowerbed, n) == True

flowerbed = [0, 0, 0]
n = 2
assert canPlaceFlowers(flowerbed, n) == True

flowerbed = [0, 1, 0]
n = 1
assert canPlaceFlowers(flowerbed, n) == False

flowerbed = [0, 0, 1, 0, 0]
n = 1
assert canPlaceFlowers(flowerbed, n) == True