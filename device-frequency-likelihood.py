# Define a list of known device types and their operating frequencies
device_types = [
    ("Garage door opener", 433.92),
    ("Wireless doorbell", 433.05),
    ("Remote control car", 27.145),
    ("Wireless microphone", 173.075),
    ("Wireless security camera", 2.4),
    ("Wireless baby monitor", 49.830),
    ("Wireless headphones", 2.402),
]

def find_closest_device(frequency):
    """
    Determine the most likely device operating at a given frequency.

    Args:
        frequency (float): The frequency to find the closest device for.

    Returns:
        str: The most likely device type operating at the given frequency.
    """
    min_diff = float('inf')
    likely_device = None

    for device_type, operating_frequency in device_types:
        diff = abs(frequency - operating_frequency)
        if diff < min_diff:
            min_diff = diff
            likely_device = device_type

    return likely_device

# Test the find_closest_device function with some example frequencies
print(find_closest_device(433.92))  # Should print "Garage door opener"
print(find_closest_device(433.05))  # Should print "Wireless doorbell"
print(find_closest_device(2.4))     # Should print "Wireless security camera"
