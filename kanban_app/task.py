class Task:
    def __init__(self, name, date, isSeries, reminderDate, taskDesc, state):
        self.name = name
        self.date = date
        self.isSeries = isSeries
        self.reminderDate = reminderDate
        self.taskDesc = taskDesc
        self.state = state # Default have backlog open closed