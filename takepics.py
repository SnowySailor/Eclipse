import gphoto2 as gp
import logging

def set_camera_config(camera, config_name, value):
    try:
        config = camera.get_config()
        target_config = config.get_child_by_name(config_name)
        target_config.set_value(value)
        camera.set_config(config)
        print(f"Set {config_name} to {value}.")
    except gp.GPhoto2Error as ex:
        print(f"Failed to set {config_name} to {value}: {ex}")

def get_camera_config(camera, config_name):
    try:
        config = camera.get_config()
        target_config = config.get_child_by_name(config_name)
        return target_config.get_value()
    except gp.GPhoto2Error as ex:
        print(f"Failed to get {config_name}: {ex}")

def capture_exposures(shots):
    """
    Captures a series of photos with the given settings on a Canon EOS R5 connected via USB.

    Args:
    - shutter_speeds (list of str): Shutter speeds to iterate over.
    - iso_values (list of str): ISO values to iterate over.
    """
    logging.basicConfig(
        format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())

    try:
        camera = gp.Camera()
        camera.init()
    except gp.GPhoto2Error as ex:
        print(f"Failed to initialize camera: {ex}")
        return

    mode = camera.get_single_config("capturetarget")
    mode.set_value("Memory card")
    camera.set_single_config("capturetarget", mode)
    set_camera_config(camera, 'focusmode', 'One Shot')
    set_camera_config(camera, 'drivemode', 'Continuous high speed')
    try:
        shoot = True
        while shoot:
            mode = input(f"Select shot mode: {shots.keys()}...")
            if mode not in shots:
                print(f"Invalid mode: {mode}")
                continue
            set_camera_config(camera, 'iso', '400')
            set_camera_config(camera, 'shutterspeed', '1/100')
            input("Press Enter to capture sequence...")
            set_camera_config(camera, 'focusmode', 'Manual')
            set_camera_config(camera, 'exposurecompensation', '0')
            for shot in shots[mode]:
                exposure = shot[0]
                iso = shot[1]
                set_camera_config(camera, 'iso', iso)
                set_camera_config(camera, 'shutterspeed', exposure)

                print(f"Capturing image with shutter speed {exposure} and ISO {iso}...")
                try:
                    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
                    print(f"Image captured: {file_path.folder}/{file_path.name}")
                except gp.GPhoto2Error as ex:
                    print(f"Failed to capture image: {ex}")
            set_autofocus = input("Set autofocus on? (y/n): ")
            if set_autofocus == 'y':
                set_camera_config(camera, 'focusmode', 'One Shot')
            shoot = input("Shoot again? (y/n): ") == 'y'
    finally:
        set_camera_config(camera, 'focusmode', 'One Shot')
        print('Exiting camera...')
        camera.exit()

shots = {
    'norm': [
        ('1/3200', '100'),
        ('1/1600', '100'),
        ('1/800', '100'),
        ('1/400', '100'),
        ('1/200', '400'),
        ('1/100', '400'),
        ('1/50', '800'),
        ('1/25', '800'),
        ('1/25', '1600'),
        ('1/13', '1600'),
        ('1/5', '1600'),
    ],
    '+1': [
        ('1/1600', '100'),
        ('1/800', '100'),
        ('1/400', '100'),
        ('1/400', '200'),
        ('1/100', '400'),
        ('1/50', '400'),
        ('1/25', '800'),
        ('1/13', '800'),
        ('1/13', '1600'),
        ('1/6', '1600'),
        ('1/3', '1600')
    ],
    '-1': [
        ('1/6400', '100'),
        ('1/3200', '100'),
        ('1/1600', '200'),
        ('1/400', '200'),
        ('1/200', '200'),
        ('1/100', '200'),
        ('1/50', '400'),
        ('1/25', '400'),
        ('1/25', '800'),
        ('1/13', '800'),
        ('1/5', '800'),
    ],
    '400': [
        ('1/8000', '400'),
        ('1/6400', '400'),
        ('1/1600', '400'),
        ('1/500', '400'),
        ('1/200', '400'),
        ('1/100', '400'),
        ('1/25', '400'),
        ('1/13', '400'),
        ('1/6', '400'),
        ('1/3', '400'),
        ('1/2', '400'),
    ],
    '100': [
        ('1/3200', '100'),
        ('1/1600', '100'),
        ('1/800', '100'),
        ('1/400', '100'),
        ('1/50', '100'),
        ('1/25', '100'),
        ('1/8', '100'),
        ('1/4', '100'),
        ('1/2', '100'),
    ],
}
capture_exposures(shots)
