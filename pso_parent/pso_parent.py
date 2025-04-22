import random
from pso.pso_particle import PsoParticle


class PsoParent():
    def __init__(self, name, func, num_dimensions, bounds, num_particles):
        print("Start   -   " + name + "   -   " + func.__name__)

        # Nazwa algorytmu
        self.name = name
        # Funkcja celu
        self.func = func
        # Liczba wymiarów
        self.num_dimensions = num_dimensions
        # Graniczne wartości cząsteczek
        self.bounds = bounds
        # Liczba cząsteczek
        self.num_particles = num_particles
        # Rój
        self.swarm = []
        # Pozycja najlepszej cząsteczki w roju
        self.g_pos_best = []
        # Wartość funkcji celu najlepszej cząsteczki w roju
        self.g_value_best = None
        # Pozycja najgorszej cząsteczki roju
        self.g_pos_worst = []
        # Wartość funkcji celu najgorszej cząsteczki w roju
        self.g_value_worst = None

    def reset(self):
        # Zresetuj wartości algorytmu
        #
        self.g_pos_best = []
        self.g_value_best = None
        self.g_pos_worst = []
        self.g_value_worst = None
        self.swarm = []

    def init_swarm(self):
        # Zainicjalizuj rój
        #
        for i in range(0, self.num_particles):
            initial_pos = []
            for j in range(0, self.num_dimensions):
                initial_pos.append(random.uniform(
                    self.bounds[0], self.bounds[1]))
            self.swarm.append(PsoParticle(initial_pos))

    def main(self, iter):
        # Główna pętla
        #
        for j in range(0, self.num_particles):
            self.swarm[j].evaluate(self.func)

            # Sprawdź, czy wartość aktualnej cząsteczki jest lepsza niż najlepsza znaleziona wartość
            if self.g_value_best == None or self.swarm[j].value < self.g_value_best:
                self.g_pos_best = list(self.swarm[j].position)
                self.g_value_best = float(self.swarm[j].value)
            # Sprawdź, czy wartość aktualnej cząsteczki jest gorsza niż najgorsza znaleziona wartość
            if self.g_value_worst == None or self.swarm[j].value > self.g_value_worst:
                self.g_pos_worst = list(self.swarm[j].position)
                self.g_value_worst = float(self.swarm[j].value)

        self.update_velocity_and_position(iter)

    def update_velocity_and_position(self, iter):
        # Zaktualizuj prędkość i pozycję wszystkich cząsteczek w roju
        #
        for i in range(0, self.num_particles):
            self.swarm[i].update_velocity(self.g_pos_best, iter)
            self.swarm[i].update_position(self.bounds)
