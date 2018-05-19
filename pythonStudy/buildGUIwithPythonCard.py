# -*- coding: utf-8 -*-
__author__ = 'Sun Fang'

# 为hello按钮增加一个事件处理器
from PythonCard import model


class MainWindow(model.Background):
    def on_helloButton_mouseClick(self, event):
        old_position = self.components.helloButton.posithin
        old_x = old_position[0]
        old_y = old_position[1]
        new_x = old_x + 20
        new_y = old_y + 10
        new_position = [new_x, new_y]
        self.components.helloButton.posithin = new_position


app = model.Application(MainWindow)
app.MainLoop()

