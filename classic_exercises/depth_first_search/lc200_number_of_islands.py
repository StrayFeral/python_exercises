from typing import List


class DepthFirstSearch:
    def lc200_number_of_islands(self, grid: List[List[str]]) -> int:
        """Leetcode 200: Number of islands.
        
        I won't make this the fastest, but will make it clear."""

        islands: int = 0
        land: str = "1"
        water: str = "0"
        nuke: str = water
        maxy: int = len(grid)

        if maxy == 0:
            return islands  # So far - zero

        maxx: int = len(grid[0])

        # De facto: Mark the island as visited
        def nuke_the_island(grid: List[List[str]], y: int, x: int) -> None:
            if (0 <= y < maxy) and (0 <= x < maxx) and grid[y][x] == land:
                grid[y][x] = nuke

                directions: List[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for yofs, xofs in directions:
                    nuke_the_island(grid, y + yofs, x + xofs)

        for y in range(maxy):
            for x in range(maxx):
                if grid[y][x] == land:
                    islands += 1
                    nuke_the_island(grid, y, x)

        return islands


grid1: List[List[str]] = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid2: List[List[str]] = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

data: list = [[1, grid1], [3, grid2]]

if __name__ == "__main__":
    o = DepthFirstSearch()

    for case in data:
        expected, grid = case
        actual = o.lc200_number_of_islands(grid)
        print(f"a={actual}, e={expected}")
        assert actual == expected
