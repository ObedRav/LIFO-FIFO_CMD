<div align="center">
    <h1>Python - Stacks - LIFO, FIFO</h1>
    <img src="https://pbs.twimg.com/media/CFYYWy6UEAE9Ow-.png" width="600" height="350">
</div>


## Introduction :laughing:

This project provides a command-line interface (CLI) to manage two different data structures: stack and queue. It implements the Last-In, First-Out (LIFO) and First-In, First-Out (FIFO) principles for stack and queue respectively, using two different implementations for each data structure: List and Doubly Linked List. The CLI allows users to interact with the data structures in two modes, interactive and non-interactive, and also accepts files with opcodes as input.

## List of Files :disguised_face:

| File Name | Description |
|---------------- | -----------|
|[console.py](./console.py)    | The CLI that allows you to interact with the data structure|
|[clear](./clear) | The script that deletes the files generated after using the CLI|
|[generate_authors](./generate_authors) | A file with the names and corresponding emails of individual contributors |
|[doubly_linked_list.py](./classes/doubly_linked_list.py) | The file that manages the Doubly Linked List implementation |
|[list.py](./classes/list.py) | The file that manages the List implementation|
|[db_storage.py](./classes/engine/db_storage.py) | The file that manages the database storage|
|[file_storage.py](./classes/engine/file_storage.py) | The file that manages the file storage|

## Project Structure :woozy_face:

```
LIFO-FIFO/
├── classes/
│   ├── doubly_linked_list.py
│   ├── list.py
|   ├── __init__.py
│   └── engine/
│       ├── db_storage.py
│       └── file_storage.py
├── console.py
├── clear
├── AUTHORS
└── generate_authors

```

## Data Structures :monocle_face:

This project supports two different data structures: Doubly Linked List and List. By default, the program uses List. You can change the data structure used with the environment variable DATA_STRUCTURE when running the CLI.

For example, to use Doubly Linked List as the data structure, you can run:

```
DATA_STRUCTURE="linkedlist" ./console.py
```

## Storage :nerd_face:

This project supports two different storage types: file-storage and database. By default, the program uses file-storage with JSON, which stores all the data in a JSON file called storage.json. You can change the storage used with the environment variable STORAGE when running the CLI.

For example, to use database storage, you can run:

```
STORAGE="database" ./console.py
```

When you use database storage, a file called database.db will appear, since this project uses SQLite databases, which is a popular lightweight relational database management system that stores data in a file-based database.


## Allowable opcodes and what they do :space_invader:

This project supports the following opcodes:

<div align="center">

  <img src="https://cdn.programiz.com/sites/tutorial2program/files/stack.png" width="500">

  | Opcode | Functionality |
  |---------------- | -----------|
  | **push** | Add element to the 'top' of stack and 'end' of queue |
  | **pop** | Remove element from 'top' of stack and 'end' of queue|
  | **pall** | Print every member of the structure |
  | **pint** | Prints the member value at the top of stack |
  | **swap** | Swaps the order  of the 1st and 2nd elements in stack |

</div>

## Usage :robot:

<details open>
<summary> <strong> Files </strong> </summary>

Create a file with opcodes, for example:

```
$ cat someopcodes.txt
push 1
push 2
push 3
add 9
pall
```

Pass the file to the console using the following command:

```
$ cat someopcodes.txt | ./console.py
1
9
2
3
```

And if you want to use a environment variable you can run `cat <filename> | <variable_name>="<value>" ./console.py`, for example:

```
$ cat someopcodes.txt | STORAGE="database" ./console.py
1
9
2
3
```

</details>

<details open>
<summary> <strong> No-Interactive Mode </strong> </summary>

Pass opcodes to the console in non-interactive mode using the following command:

```
$ echo "push 1" | STORAGE="database" ./console.py
```

And the console will process in no-interative mode, you can run also:

```
$ echo "pall" | STORAGE="database" ./console.py
1
9
2
3
1
1
1
1
```

</details>

<details open>
<summary> <strong> Interactive Mode </strong> </summary>

Run the console with the desired environment variables to enter interactive mode, for example:

```
$ STORAGE="database" ./console.py
You're using List as a data_structure
(List)>
```

The prompt shows the data structure being used.

```
$ DATA_STRUCTURE="linkedlist" STORAGE="database" ./console.py
You're using LinkedList as a data_structure
(LinkedList)> 
```

Enter the desired command:

```
$ DATA_STRUCTURE="linkedlist" STORAGE="database" ./console.py
You're using LinkedList as a data_structure
(LinkedList)> push 6
(LinkedList)> push 7
(LinkedList)> push 8
(LinkedList)> push 9
(LinkedList)> add 3
(LinkedList)> pall
6
3
7
8
9
(LinkedList)> 
```
</details>

## Error Messages :collision:

The program may display several error messages during its execution. Some of the most common ones are:

* <strong>Invalid data, must be an integer:</strong> This error message is displayed when you run a command that expects an integer, but you provide another data type or no data at all. This error message will only appear if you use the `push` or `add` opcodes.
* <strong>There are no elements in the data structure:</strong> This error message is displayed when you try to use an opcode that requires elements in the data structure, but there are none. For example, if you try to `pop` an element from an empty data structure.
* <strong>There are not enough elements in the data structure:</strong> This error message is displayed when you try to `swap` elements, but there are not enough elements in the data structure to do so.


## Things to keep in mind :eye_speech_bubble:

Both linked list and list use the same storage, so information can be shared between them. For example:

```
$ DATA_STRUCTURE="linkedlist" STORAGE="database" ./console.py
You're using LinkedList as a data_structure
(LinkedList)> pall
6
3
7
8
9
(LinkedList)> quit
$ STORAGE="database" ./console.py
You're using List as a data_structure
(List)> pall
6
3
7
8
9
(List)> quit
```

## Bugs :bomb:
If you find any bug, please, let us know.

## Styling :page_with_curl:
All files have been written in the [Pycodestyle](https://github.com/PyCQA/pycodestyle/issues/466).

## Authors
* **Obed Rayo** <a href="https://github.com/ObedRav" rel="nofollow"><img align="center" alt="github" src="https://www.vectorlogo.zone/logos/github/github-tile.svg" height="24" /></a>





