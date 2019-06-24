# CoderSchool FTW - Todo List

Created with love by: Anh Nguyen
    
[//]: # (One or two sentence summary of your project.)

[//]: # (## Video Walkthrough)

[//]: # (Here's a walkthrough of implemented user stories.)


## User Stories

The following **required** functionalities are completed:

THE USER is

* [ ] The user can run your program from the command line.
* [ ] If the user does not supply the correct arguments, or supplies a --help flag, the user sees a "usage" message.
* [ ] The user can add a todo from the command line, by calling add_todo. The fields specified should be text, due_date, and project_id. The fields due_date and project_id are optional. Text is required.
* [ ] Todos added, by default should be marked as incomplete.
* [ ] The user should see a message giving information about the todo that was added.
* [ ] The user can call a function called mark_complete and pass the id of the todo to mark complete.
* [ ] The user can see all todos from the command line by passing a list command, sorted with the ones due first.
* [ ] The user can supply arguments to the list command to only see todos that are complete.
* [ ] The user can supply arguments to the list command to only see todos of a particular project_id.
* [ ] The user can supply arguments to the list command to reverse the default sort, to now see the todos by due_date descending.
* [ ] The user can supply arguments to the list command to combine the above options.

The following **optional** features are implemented:
THE USER is

* [ ] The user can add a project by calling add_project. Each project must have a name.
* [ ] The user can see all projects from the command line.

**Bonus Requirements**

* [ ] The user can add a user_id to each todo.
* [ ] The user can add a user to the system by passing add_user. Each user should have a name, email_address, and id.
* [ ] The user can call a list_users command that shows all the users in the system.
* [ ] The user can call a staff command that shows each project, combined with each of the users working on that project.
* [ ] The user can call a who_to_fire command that lists all users who are not currently assigned a todo.



[//]: # (The following **additional** features are implemented:)

[//]: # (* [x] List anything else that you can get done to improve the page!)

## Time Spent and Lessons Learned


## Describe any challenges encountered while building the app (retrived several of my google queries).
* <a href="https://stackoverflow.com/questions/7783308/os-path-dirname-file-returns-empty">Why does os.path.dirname(__file__) returns empty</a> ???
* How to comment multi lines in python way
* Differentiate the notation for string datatype versus docstring
* <a href="https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory#273227">safely create a nested directories</a>
* Pass path-like object to <code>connect</code> instead of string ???

[//]: # (## Version 1.0.2)
[//]: # (May 2019 Added drag and drop feature)

## Version 1.0.0
Adapted from the <a href="https://www.youtube.com/watch?v=ekxGtZgORU8&feature=youtu.be" target="_blank">live demo</a> from Mr. Charles.

## License

    Copyright 2019 Anh Nguyen

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
