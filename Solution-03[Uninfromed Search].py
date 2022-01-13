import time
class Maze(object):

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
    
    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print ('#')
                else:
                    print (self.grid[r][c])
            print
        print

    def moves(self):

        """Return a list of possible moves given the current agent location."""
    def neighbor(self, move):

        """Return a list of possible moves given the current agent location."""
class Agent(object):

    def bfs(self, maze, goal):

        """Return a list of possible moves given the current agent location."""

def main():

    grid = """
    ##############################
    #         #              #   #
    # ####    ########       #   #
    #  o #    #              #   #
    #    ###     #####  ######   #
    #      #   ###   #           #
    #      #     #   #  #  #   ###
    #     #####    #    #  # x   #
    #              #       #     #
    ##############################
    """

    maze = Maze(grid, (1,1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19,18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.25)
        maze.display()

if __name__ == '__main__':
    main()

