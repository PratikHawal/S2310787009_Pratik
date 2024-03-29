import argparse
import matplotlib.pyplot as pyplot
import numpy as np

class BrakingDistance:
    def __init__(self, initial_velocity, deceleration):
        self.initial_velocity = initial_velocity
        self.deceleration = deceleration

    def calculate_braking_distance(self):
        return (self.initial_velocity ** 2) / (2 * self.deceleration)

    def calculate_velocities(self, time_points):
        return self.initial_velocity - self.deceleration * time_points

    def calculate_distances(self, time_points):
        return self.initial_velocity * time_points - 0.5 * self.deceleration * time_points**2

def plot_graphs(time_points, velocities, distances):
    # Velocity-time graph
    pyplot.subplot(2, 1, 1)
    pyplot.plot(time_points, velocities, label='Velocity')
    pyplot.title('Velocity-Time Graph')
    pyplot.xlabel('Time (s)')
    pyplot.ylabel('Velocity (m/s)')
    pyplot.legend()

    # Distance-time graph
    pyplot.subplot(2, 1, 2)
    pyplot.plot(time_points, distances, label='Distance')
    pyplot.title('Distance-Time Graph')
    pyplot.xlabel('Time (s)')
    pyplot.ylabel('Distance (m)')
    pyplot.legend()

    pyplot.tight_layout()
    pyplot.show()

def main():
    parser = argparse.ArgumentParser(description="Calculate braking distance and plot distance, velocity graphs.")
    parser.add_argument('--initial_velocity', required=True, type=float, help="Initial velocity of the vehicle (m/s)")
    parser.add_argument('--deceleration', required=True, type=float, help="Deceleration or braking acceleration (m/s^2)")
    args = parser.parse_args()

    initial_velocity = args.initial_velocity
    deceleration = args.deceleration

    time_interval = 10.0  # in seconds

    braking_distance_calculator = BrakingDistance(initial_velocity, deceleration)
    b_distance = braking_distance_calculator.calculate_braking_distance()
    print(f"The braking distance is: {b_distance} meters")

    time_points = np.arange(0, time_interval + 0.1, 0.1)
    velocities = braking_distance_calculator.calculate_velocities(time_points)
    distances = braking_distance_calculator.calculate_distances(time_points)

    plot_graphs(time_points, velocities, distances)

if __name__ == "__main__":
    main()