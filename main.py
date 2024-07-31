from framework import MyApp
from pinching import PinchingListener
import time
import leap



def main():
    app = MyApp()
    
    listener = PinchingListener(app.update_camera_position)
    
    connection = leap.Connection()
    connection.add_listener(listener)
    
    with connection.open():
        try:
            app.run()
        except KeyboardInterrupt:
            pass
        finally:
            connection.remove_listener(listener)

if __name__ == "__main__":
    main()