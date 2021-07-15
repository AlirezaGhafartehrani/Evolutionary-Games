from player import Player
import random
import copy
import numpy as np
from config import CONFIG


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        pass

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        # N1 = len(prev_players)
        # N2 = num_players
        else:
            sum_probability = 0
            for index in range(len(prev_players)):
                sum_probability += prev_players[index].fitness

            probability_array = []
            accumulative_probability = []
            Sum = 0
            for i in range(len(prev_players)):
                probability_array.append(prev_players[i].fitness/sum_probability)
                Sum += probability_array[i]
                accumulative_probability.append(Sum)
            # print(accumulated_probability)
            # exit()

            new_players = []
            for i in range(num_players):
                n = random.random()
                for j in range(len(accumulative_probability)):
                    if accumulative_probability[j] < n:
                        continue
                    else:
                        new_players.append(copy.deepcopy(prev_players[j]))
                        self.mutate(prev_players[j])
                        break

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            return new_players

    def next_population_selection(self, players, num_players):


        # TODO
        # num_players example: 100
        # players: an array of `Player` objects
        sorted_players = sorted(players, key=lambda x: x.fitness, reverse=True)

        # for i in range(num_players):
        #     print(sorted_players[i].fitness)
        # exit()

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        return sorted_players[: num_players]
