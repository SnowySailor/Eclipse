import gphoto2 as gp

def list_connected_cameras():
    """
    Lists all cameras connected via USB.
    """
    # Use gp.check_result for error handling
    gp.check_result(gp.use_python_logging())
    context = gp.Context()

    # Autodetect the cameras and list them
    camera_list = gp.Camera.autodetect(context)
    
    if not camera_list:
        print("No cameras detected.")
    else:
        print("Connected cameras:")
        for index, (name, addr) in enumerate(camera_list):
            print(f"{index + 1}: {name} at {addr}")

list_connected_cameras()

