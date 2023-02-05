# todo-cli
todo application for cli

status codes in db:
status:0 => undone 
status=1 => completed

---

to show all todos:
python3 todocli.py show
python3 todocli.py show --status=2

to show undone todos:
python3 todocli.py show --status=0

to show completed todos: 
python3 todocli.py show --status=2

to add new todo:
python3 todocli.py add "Adding new item to list" "Self-Learning"

to delete given item #:
python3 todocli.py delete 1

to update given item #:
python3 todocli.py update 5 "add show_undone function" "Self-Learning"

to complete given item #:
python3 todocli.py undone 3  

to undone an item:
python3 todocli.py undone 20
