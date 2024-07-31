from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # TODO 2: change .obj model to .egg or .bam to be able to render textures.
        self.donut = self.loader.loadModel("./assets/donut.obj", )
        self.donut.setScale(50, 50, 50)
        self.donut.setPos(0, 0, 3.5)
        self.donut.reparentTo(self.render)

        # Initial camera control variables
        self.hand_pos = (0, 0, 0)
        self.angleDegrees = [0, 0, 0]

    def spinCameraTask(self, task):
        angleRadians = [angle * (pi / 180.0) for angle in self.angleDegrees]
        
        x = 20 * sin(angleRadians[0])
        y = -20 * cos(angleRadians[0])
        
        self.camera.setPos(x, y, 3 + self.angleDegrees[2] / 10.0)  # Use z-axis for height adjustment
        self.camera.setHpr(self.angleDegrees[0], self.angleDegrees[1], self.angleDegrees[2])
        
        self.camera.lookAt(self.donut)
        
        return Task.cont
    
    def update_camera_position(self, x, y, z):
        self.angleDegrees = [x / 1.5, y, z]