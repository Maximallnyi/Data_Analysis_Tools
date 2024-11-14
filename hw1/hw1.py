import time
import numpy as np


def match_timestamps(timestamps1: np.ndarray, timestamps2: np.ndarray) -> np.ndarray:
    """
    Timestamp matching function. It returns such array `matching` of length len(timestamps1),
    that for each index i of timestamps1 the output element matching[i] contains
    the index j of timestamps2, so that the difference between
    timestamps2[j] and timestamps1[i] is minimal.
    Example:
        timestamps1 = [0, 0.091, 0.5]
        timestamps2 = [0.001, 0.09, 0.12, 0.6]
        => matching = [0, 1, 3]
    """
    # Put your code here!

    matching = []

    index_1 = 0
    index_2 = 0

    while index_1 != len(timestamps1):
        if (timestamps1[index_1] > timestamps2[index_2] and timestamps1[index_1] < timestamps2[index_2+1]):
            if (timestamps1[index_1] - timestamps2[index_2] > timestamps2[index_2+1] - timestamps1[index_1]):
                matching.append(index_2+1)
                index_2 += 2
            else: 
                matching.append(index_2)
                index_2 += 1
            index_1 += 1
        elif (timestamps1[index_1] <= timestamps2[index_2]):
            matching.append(index_2)
            index_2 += 1
            index_1 += 1
        else:
            index_2 += 1

    return matching


def make_timestamps(fps: int, st_ts: float, fn_ts: float) -> np.ndarray:
    """
    Create array of timestamps. This array is discretized with fps,
    but not evenly.
    Timestamps are assumed sorted nad unique.
    Parameters:
    - fps: int
        Average frame per second
    - st_ts: float
        First timestamp in the sequence
    - fn_ts: float
        Last timestamp in the sequence
    Returns:
        np.ndarray: synthetic timestamps
    """
    # generate uniform timestamps
    timestamps = np.linspace(st_ts, fn_ts, int((fn_ts - st_ts) * fps))
    # add an fps noise
    timestamps += np.random.randn(len(timestamps))
    timestamps = np.unique(np.sort(timestamps))
    return timestamps


def main():
    """
    Setup:
        Say we have two cameras, each filming the same scene. We make
        a prediction based on this scene (e.g. detect a human pose).
        To improve the robustness of the detection algorithm,
        we average the predictions from both cameras at each moment.
        The camera data is a pair (frame, timestamp), where the timestamp
        represents the moment when the frame was captured by the camera.
        The structure of the prediction does not matter here. 

    Problem:
        For each frame of camera1, we need to find the index of the
        corresponding frame received by camera2. The frame i from camera2
        corresponds to the frame j from camera1, if
        abs(timestamps[i] - timestamps[j]) is minimal for all i.

    Estimation criteria:
        - The solution has to be optimal algorithmically. If the
    best solution turns out to have the O(n^3) complexity [just an example],
    the solution with O(n^3 * logn) will have -1 point,
    the solution O(n^4) will have -2 points and so on.
    Make sure your algorithm cannot be optimized!
        - The solution has to be optimal python-wise.
    If it can be optimized ~x5 times by rewriting the algorithm in Python,
    this will be a -1 point. x20 times optimization will give -2 points, and so on.
    You may use any library, even write your own
    one in C++.
        - All corner cases must be handled correctly. A wrong solution
    will have -3 points.
        - Top 3 solutions get 10 points. The measurement will be done in a single thread. 
        - The base score is 9.
        - Parallel implementation adds +1 point, provided it is effective
    (cannot be optimized x5 times)
        - Maximal score is 10 points, minimal score is 5 points.
        - The deadline is November 14 23:59. Failing the deadline will
    result in -2 points, and each additional week will result in -1 point.
        - The solution can be improved/fixed after the deadline provided that the initial
    version is submitted on time.

    Optimize the solution to work with ~2-3 hours of data.
    Good luck!
    """
    # generate timestamps for the first camera
    timestamps1 = make_timestamps(30, time.time() - 100, time.time() + 3600 * 2)
    # generate timestamps for the second camera
    timestamps2 = make_timestamps(60, time.time() + 200, time.time() + 3600 * 2.5)
    matching = match_timestamps(timestamps1, timestamps2)



if __name__ == '__main__':
    main()