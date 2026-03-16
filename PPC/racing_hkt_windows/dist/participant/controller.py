
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Path: list of waypoints [{"x": float, "y": float}, ...]
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"} 
# CmdFeedback: {"throttle", "steer"}         

# ─── CONTROLLER ───────────────────────────────────────────────────────────────
import numpy as np



def steering(path: list[dict], state: dict):

    length_of_car = 2.6
    # Calculate steering angle based on path and vehicle state



    if len(path) == 0:
        return 0.0

    x = state["x"]
    y = state["y"]
    yaw = state["yaw"]
    v = np.sqrt(state["vx"]**2 + state["vy"]**2)

    car_loc = np.array([x, y])

    waypoints = np.array([[p["x"], p["y"]] for p in path])

    distances = np.linalg.norm(waypoints - car_loc, axis=1)

    closest_idx = np.argmin(distances)

    lookahead_offset = int(2 + 0.5 * v)


target_idx = min(closest_idx + lookahead_offset, len(waypoints) - 1)

    target = waypoints[target_idx]

    target_vec = target - car_loc

    target_yaw = np.arctan2(target_vec[1], target_vec[0])

    alpha = (target_yaw - yaw + np.pi) % (2 * np.pi) - np.pi

    k_p = 1.2

    steer = k_p * alpha

    

    steer = 0.0 # Default steer value
    # 0.5 in the max steering angle in radians (about 28.6 degrees)
    return np.clip(steer, -0.5, 0.5)


def throttle_algorithm(target_speed, current_speed, dt):

 error = target_speed - current_speed

    k_p = 0.4

    throttle = k_p * error

    if throttle < 0:
        brake = -throttle
        throttle = 0
    else:
        brake = 0



    
    
    # generate the output for throttle command
    
    # clip throttle and brake to [0, 1]
    return np.clip(throttle, 0.0, 1.0), np.clip(brake, 0.0, 1.0)

def control(
    path: list[dict],
    state: dict,
    cmd_feedback: dict,
    step: int,
) -> tuple[float, float, float]:
    """
    Generate throttle, steer, brake for the current timestep.
    Called every 50ms during simulation.

    Args:
        path:         Your planned path (waypoints)
        state:        Noisy vehicle state observation
                        x, y        : position (m)
                        yaw         : heading (rad)
                        vx, vy      : velocity in body frame (m/s)
                        yaw_rate    : (rad/s)
        cmd_feedback: Last applied command with noise
                        throttle, steer, brake
        step:         Current simulation timestep index

    Returns:
        throttle  : float in [0.0, 1.0]   — 0=none, 1=full
        steer     : float in [-0.5, 0.5]  — rad, neg=left
        brake     : float in [0.0, 1.0]   — 0=none, 1=full
    
    Note: throttle and brake cannot both be > 0 simultaneously.
    """
    throttle = 0.0
    steer    = 0.0
    brake = 0.0
   
    # TODO: implement your controller here
    steer = steering(path, state)
    target_speed = 5.0  # m/s, adjust as needed
    global integral
    throttle, brake = throttle_algorithm(target_speed, state["vx"], 0.05)

    return throttle, steer, brake
