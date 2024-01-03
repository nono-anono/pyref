class transitions:
    transitions= [
        {"trigger": "next", "source": "start", "dest": "init"},

        {"trigger": "next", "source": "init", "dest": "get", "conditions": "init_OK"},
        {"trigger": "next", "source": "init", "dest": "init", "conditions": "init_Retry"},
        {"trigger": "next", "source": "init", "dest": "end", "conditions": "init_SE"},

        {"trigger": "next", "source": "get", "dest": "process", "conditions": "new_data"},
        {"trigger": "next", "source": "get", "dest": "end", "conditions": "no_data"},

        {"trigger": "next", "source": "process", "dest": "get", "conditions": "process_OK"},
        {"trigger": "next", "source": "process", "dest": "get", "conditions": "process_BE"},
        {"trigger": "next", "source": "process", "dest": "init", "conditions": "process_SE"}
    ]

    # region - Transition condition checks
    def init_OK(**kwargs):
        return kwargs['system_exception'] == None

    def init_Retry(**kwargs):
        return kwargs['retry_init_flag']

    def init_SE(**kwargs):
        return kwargs['system_exception'] != None

    def new_data(**kwargs):
        return kwargs['transaction_item'] != None

    def no_data(**kwargs):
        return kwargs['transaction_item'] == None

    def process_OK(**kwargs):
        return kwargs['system_exception'] == None and kwargs['business_exception'] == None

    def process_BE(**kwargs):
        return kwargs['business_exception'] != None

    def process_SE(**kwargs):
        return kwargs['system_exception'] != None
    # endregion