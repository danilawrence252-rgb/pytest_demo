class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solution = []

    def setGrid(self, grid):
        self.grid = grid

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    def getSolution(self):
        self.solution = []

        # Validate grid and dictionary
        if not self.grid or not self.dictionary:
            return []
        if not isinstance(self.grid, list) or not all(isinstance(row, list) for row in self.grid):
            return []
        row_len = len(self.grid[0])
        if any(len(row) != row_len for row in self.grid):
            return []
        if not isinstance(self.dictionary, list):
            return []

        rows = len(self.grid)
        cols = len(self.grid[0])

        # Special multi-letter tiles
        SPECIAL_TILES = {"Qu": "qu", "St": "st", "Ie": "ie"}

        # Normalize grid: store lowercase string values per cell
        norm_grid = []
        for r in range(rows):
            row_vals = []
            for c in range(cols):
                tile = self.grid[r][c]
                if tile in SPECIAL_TILES:
                    row_vals.append(SPECIAL_TILES[tile])
                else:
                    row_vals.append(tile.lower())
            norm_grid.append(row_vals)

        # Build a trie from the dictionary for fast prefix lookups
        trie = {}
        for word in self.dictionary:
            if not isinstance(word, str) or len(word) < 3:
                continue
            node = trie
            for ch in word.lower():
                node = node.setdefault(ch, {})
            node["$"] = True  # end of word marker

        def dfs(r, c, node, path, visited, current_word):
            tile_val = norm_grid[r][c]  # e.g. "a", "qu", "st"

            # Traverse trie with each character of the tile
            curr_node = node
            for ch in tile_val:
                if ch not in curr_node:
                    return
                curr_node = curr_node[ch]

            current_word += tile_val
            visited.add((r, c))

            # If end-of-word marker exists and word is long enough
            if "$" in curr_node and len(current_word) >= 3:
                word_found = current_word
                if word_found not in self.solution:
                    self.solution.append(word_found)

            # Explore all 8 adjacent neighbors
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        dfs(nr, nc, curr_node, path + [(nr, nc)], visited, current_word)

            visited.remove((r, c))

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie, [(r, c)], set(), "")

        # Return matched original-case words from the dictionary
        solution_set = set(self.solution)
        result = [w for w in self.dictionary if isinstance(w, str) and w.lower() in solution_set]
        self.solution = result
        return self.solution


def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet",
        "arty", "rhr", "not", "quar"
    ]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
