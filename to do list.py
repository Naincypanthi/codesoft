task=[]
def add():
    """
    Add a task to to_do_list
    """
    add=input("\nenter your new task")
    date=input("\nenter date")
    description=input("\nenter description")
    add.append(task)
    date.appened(task)
    description.append(task)
    print("Successfully added your task")
def view():
    """
    view the task in to_d-_list
    """
    if len(task)==0:
        print("No task")
    else:
        for i,tasks in task:
            print({i+1},{task})