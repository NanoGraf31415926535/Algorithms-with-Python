import random
import math

def estimate_pi(num_points):
    points_inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
    return 4 * (points_inside_circle / num_points)

# Example Usage
if __name__ == "__main__":
    num_samples = 10000
    estimated_pi = estimate_pi(num_samples)
    print(f"Estimated value of pi with {num_samples} samples: {estimated_pi}")
    print(f"Value of math.pi: {math.pi}")