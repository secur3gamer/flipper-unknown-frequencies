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

# Function to determine the likelihood of a device operating at a given frequency
def likelihood(frequency):
    # Initialize likelihood to 0
    likelihood = 0
    
    # Loop through the known device types and calculate the difference between the given frequency
    # and the operating frequency for each device. The device with the smallest difference is the 
    # most likely to be operating at the given frequency.
    for device_type, operating_frequency in device_types:
        diff = abs(frequency - operating_frequency)
        if diff < likelihood or likelihood == 0:
            likelihood = diff
            likely_device = device_type
    
    # Return the most likely device type
    return likely_device

# Test the likelihood function with some example frequencies
print(likelihood(433.92))  # Should print "Garage door opener"
print(likelihood(433.05))  # Should print "Wireless doorbell"
print(likelihood(2.4))     # Should print "Wireless security camera"
