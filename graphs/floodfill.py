#!/usr/bin/env python

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    print(sr, sc, color)
    # find source tile
    # update the source tile to color
    # find 4 direction if their number equals original tile
    # source = [sr][sc], above = [sr-1][sc], below = [sr+1][sc], left = [sr][sc-1], right = [sr][sc+1]
    # break if sr or sc = 0 or len(sr, sc)
    # call flood
    if image[sr][sc] == color:
        return image
    origin_tile = image[sr][sc]
    image[sr][sc] = color

    # above
    above = sr-1
    if above >= 0:
        if image[above][sc] == origin_tile:
            image = self.floodFill(image, above, sc, color)
    # below
    below = sr+1
    if below < len(image):
        if image[below][sc] == origin_tile:
            image = self.floodFill(image, below, sc, color)
    # left
    left = sc-1
    if left >= 0:
        if image[sr][left] == origin_tile:
            image = self.floodFill(image, sr, left, color)
    # right
    right = sc+1
    if right < len(image[sr]):
        if image[sr][right] == origin_tile: 
            image = self.floodFill(image, sr, sc+1, color)
    

    return image

if __name__ == "__main__":
    main()
