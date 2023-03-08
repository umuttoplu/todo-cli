# todo-cli terminal commands

---

show all todos

	python3 todocli.py show

	python3 todocli.py show --status=2
---

show undone todos:

	python3 todocli.py show --status=0
---
show completed todos: 

	python3 todocli.py show --status=2
---

add new todo:

	python3 todocli.py add "Adding new item to list" "Self-Learning"
---
delete given item #:

	python3 todocli.py delete 1
---
update given item #:

	python3 todocli.py update 5 "add show_undone function" "Self-Learning"
---
complete given item #:

	python3 todocli.py complete 3  
---
undone an item:

	python3 todocli.py undone 20
