
numRows = 5
out = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def create_new_row(prev: list[int]) -> list[int]:
    row = [1]

    for i in range(len(prev)-1):
        row.append(prev[i] + prev[i+1])
    row.append(1)

    return row

def getPascalTriangle(n: int) -> list[int]:
    row = [1]
    result = [row]

    for _ in range(n):
        row = create_new_row(row)
        result.append(row)
    return result 


def test_pascal():
    result = getPascalTriangle(numRows)
    if result == out: print("OK")

if __name__ == "__main__":
    test_pascal()



