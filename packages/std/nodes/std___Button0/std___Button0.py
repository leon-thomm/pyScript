from NIENV import *


# USEFUL
# self.input(index)                   <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget
# self.exec_output(index)             <- executes an execution output
# self.create_new_input(type_, label, widget_name=None, widget_pos='under')
# self.delete_input(input or index)
# self.create_new_output(type_, label, append=True)
# self.delete_output(output or index)



class Button_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Button_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}

    def button_clicked(self):
        self.update()

    def update_event(self, input_called=-1):
        self.exec_output(0)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...


    def remove_event(self):
        pass
