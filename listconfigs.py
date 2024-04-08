import gphoto2 as gp

def list_all_configs(camera):
    """
    Lists all configuration options for the specified camera.

    Args:
        camera: The camera object initialized by gphoto2.
    """
    # Get the camera configuration tree
    config = camera.get_config()
    
    # Recursive function to traverse the configuration tree
    def list_configs(config, indent=0):
        # Iterate through all child nodes
        for child in config.get_children():
            name = child.get_name()
            label = child.get_label()
            
            # Try to get the current value; not all configs have a 'get_value'
            try:
                value = child.get_value()
            except gp.GPhoto2Error:
                value = None

            # Print the config name, label, and value
            print(f"{' ' * indent}{name} ({label}): {value}")

            # Recurse into sub-configs if they exist
            if child.count_children() > 0:
                list_configs(child, indent + 2)
    
    # Start the recursive listing from the root config
    list_configs(config)

# Initialize camera
camera = gp.Camera()
camera.init()

# List all configurations
list_all_configs(camera)

# Clean up
camera.exit()

