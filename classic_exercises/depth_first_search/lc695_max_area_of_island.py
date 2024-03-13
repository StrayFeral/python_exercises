from typing import List


class DepthFirstSearch:
    def lc659_max_area_of_island(self, grid: List[List[int]]) -> int:
        """Leetcode 695: Max area of an island."""
        
        max_area: int = 0
        land: int = 1
        water: int = 0
        nuke: int = water
        maxy: int = len(grid)

        if maxy == 0:
            return max_area  # So far it is zero

        maxx: int = len(grid[0])

        def island_area(grid: List[List[int]], y: int, x: int) -> int:
            area: int = 0
            if (0 <= y < maxy) and (0 <= x < maxx) and grid[y][x] == land:
                area += 1
                grid[y][x] = nuke

                directions: List[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for yofs, xofs in directions:
                    area += island_area(grid, y + yofs, x + xofs)

            return area

        for y in range(maxy):
            for x in range(maxx):
                if grid[y][x] == land:
                    max_area = max(max_area, island_area(grid, y, x))

        return max_area


grid1: List[List[int]] = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
grid2: List[List[int]] = [
    [0, 0, 0, 0, 0],
]

data: list = [[6, grid1], [0, grid2]]

if __name__ == "__main__":
    o = DepthFirstSearch()

    for case in data:
        expected, grid = case
        actual = o.lc659_max_area_of_island(grid)
        print(f"a={actual}, e={expected}")
        assert actual == expected
