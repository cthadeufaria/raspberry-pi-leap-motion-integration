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

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        # TODO 1: implement leap motion control on camera.
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


app = MyApp()
app.run()