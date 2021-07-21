# Watcherr interview tasks

This project has been done as interview task for Watcherr company. Backend is written in Python and task 2 has also frontend written in Angular. I spent about 100 minutes to complete this.


## Task 1

This part of task has 2 separate python scripts. The whole task is configurable by config.py file in task1 package.

### Rendering the list of stores in alphabetical order with location details
Run the main.py script in task1 python package to see rendered list of stores. The script will automatically open browser for you. 

### Searching stores in specific radius
Run the main_radius.py script in task1 python package. When you run it you'll be asked for UK based postcode and specific radius in metres. You're able to exit program anytime by inputting "q" and pressing enter.

## Task 2
### Store filter API
Run the main.py script in task2 python package to run the API server. You can pass any value in query parameter "find". If you don't pass any value you'll get all saved data. This part of task is using prepared (cached) file with all information to be faster.

Example API call
```sh
GET http://localhost:8888/filter?find=hav
```