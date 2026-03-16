
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Cone: {"x": float, "y": float, "side": "left" | "right", "index": int}
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"}  
# CmdFeedback: {"throttle", "steer"}        

# ─── PLANNER ──────────────────────────────────────────────────────────────────
import numpy as np

def plan(cones: list[dict]) -> list[dict]:
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.

    Args:
        cones: List of cone dicts with keys x, y, side ("left"/"right"), index

    Returns:
        path: List of waypoints [{"x": float, "y": float}, ...]
              Ordered from start to finish.
    
    Tip: Try midline interpolation between matched left/right cones.
         You can also compute a curvature-optimised racing line.
    """
    path = []

    # TODO: implement your path planning here
    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])

    # implement a planning algorithm to generate a path from the blue and yellow cones


 n = min(len(blue), len(yellow))

    midpoints = []

    for i in range(n):

        lx = blue[i][0]
        ly = blue[i][1]

        rx = yellow[i][0]
        ry = yellow[i][1]

        mx = (lx + rx) / 2
        my = (ly + ry) / 2

        midpoints.append((mx, my))

    for i in range(len(midpoints)):
     if i == 0 or i == len(midpoints) - 1:
            x, y = midpoints[i]

        else:
            x1, y1 = midpoints[i-1]
            x2, y2 = midpoints[i]
            x3, y3 = midpoints[i+1]

            x = (x1 + x2 + x3) / 3
            y = (y1 + y2 + y3) / 3

        path.append({"x": float(x), "y": float(y)})





    return path

