class ChristmasTreeFarm: 
    """A christmas tree farm."""
    plots: list[int] = []
    
    def __init__(self, plots: int, intial_planting: int) -> None:
        """Intialize the farm."""
        self.plots = []
        for i in range(0, intial_planting):
            self.plots.append(1)
        for i in range(0, plots - intial_planting):
            self.plots.append(0)
    
    def plant(self, plot_idx: int) -> None:
        """Plant method."""
        self.plots[plot_idx] = 1
    
    def growth(self) -> None:
        """Growht method."""
        for i in range(0, len(self.plots)):
            if self.plots[i] != 0:
                self.plots[i] += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvest method."""
        harvested: int = 0
        if replant is True:
            for i in range(0, len(self.plots)):
                if self.plots[i] >= 5:
                    harvested += 1
                    self.plots[i] = 1
            return harvested
        else:
            for i in range(0, len(self.plots)):
                if self.plots[i] >= 5:
                    harvested += 1
                    self.plots[i] = 0
            return harvested 
    
    def __add__(self, add_from: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Add method."""
        plotting: int = 0
        for plot in self.plots:
            if plot > 0:
                plotting += 1
        for plot in add_from.plots:
            if plot > 0:
                plotting += 1
        return ChristmasTreeFarm(len(self.plots)+len(add_from.plots), plotting)
