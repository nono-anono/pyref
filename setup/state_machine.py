from transitions import Machine

class state_machine:
    states = [
        {"name": "start"},
        {"name": "init", "on_enter": "on_enter_init"},
        {"name": "get", "on_enter": "on_enter_get"},
        {"name": "process", "on_enter": "on_enter_process"},
        {"name": "end", "on_enter": "on_enter_end"}
    ]

    def run(bot):

        # Attach 'bot' model to state machine
        Machine(
            model            = bot,
            states           = bot.states,
            initial          = 'start',
            transitions      = bot.transitions,
            auto_transitions = False
        )

        # Run the state machine till end and passes arguments to trigger condition-checking methods
        while bot.state != 'end':
            bot.trigger('next',
                system_exception   = bot.system_exception,
                retry_init_flag    = bot.retry_init_flag,
                transaction_item   = bot.transaction_item,
                business_exception = bot.business_exception
            )