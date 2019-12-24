/* Create todo database */
sqlite3 todo.db

/* Create list and task tables */
CREATE TABLE lists (
    listId INTEGER PRIMARY KEY,
    listName VARCHAR(255)
);

CREATE TABLE tasks (
    taskId INTEGER PRIMARY KEY,
    listId INTEGER,
    description VARCHAR(255),
    priority CHAR(1),
    category1 VARCHAR(255),
    category2 VARCHAR(255),
    dueDate DATETIME,
    completionStatus TINYINT(1),
    FOREIGN KEY(listId) REFERENCES lists(listId) 
);

INSERT INTO tasks(taskId,listId,description,priority,category1,category2,dueDate,completionStatus)
VALUES(1,1,"Polish summary for Tuscaloosa ticket","A","Work","Tickets",12/16/2019,0);
