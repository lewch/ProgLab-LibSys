class Option:
    '''
    A class for options shown on the screens.
    '''
    def __init__(self, description, func = None, *args, **kwargs):
        '''
        A constructor of option class.
        :param description: The description of the option shown on the screen, such as "Show all titles" or "Add a title"
        :param func: The function of the option, which defines its behaviour
        :param args: The arguments which the function may need
        :param kwargs: The dictionary of keyword arguments which the function may need
        '''
        self.description = description
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        '''
        It runs the function of the option when the function is defined.
        :return: None
        '''
        if self.func is not None:
            self.func(*self.args, **self.kwargs)