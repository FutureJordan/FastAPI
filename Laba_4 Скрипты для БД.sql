Таблицы: Менеджер, Сотрудники, Администратор, Препараты, Поставки, Поставщики, Заказы, Клиенты, Склад, Остатки на складе, Покупки

CREATE TABLE Менеджер (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Имя VARCHAR(50)
    Фамилия(50)
    Телефон DECIMAL(20)
);

CREATE TABLE Сотрудники (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Имя VARCHAR(50)
    Фамилия(50)
    Должность VARCHAR(50)
    Телефон DECIMAL(20)
);

CREATE TABLE Администратор (
    id INT PRIMARY KEY AUTO_INCREMENT,
    имя VARCHAR(50),
    фамилия VARCHAR(50),
    Телефон DECIMAL(20)
);


CREATE TABLE Препараты (
    id INT PRIMARY KEY AUTO_INCREMENT,
    название VARCHAR(50),
    дозировка VARCHAR(20),
    тип VARCHAR(50)
);


CREATE TABLE Поставки (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_поставщика INT,
    id_препарата INT,
    количество INT,
    FOREIGN KEY (id_поставщика) REFERENCES Поставщики(id),
    FOREIGN KEY (id_препарата) REFERENCES Препараты(id)
);


CREATE TABLE Поставщики (
    id INT PRIMARY KEY AUTO_INCREMENT,
    название VARCHAR(50),
    адрес VARCHAR(100),
    телефон VARCHAR(20)
);


CREATE TABLE Заказы (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_клиента INT,
    дата_заказа DATE,
    FOREIGN KEY (id_клиента) REFERENCES Клиенты(id)
);


CREATE TABLE Клиенты (
    id INT PRIMARY KEY AUTO_INCREMENT,
    имя VARCHAR(50),
    фамилия VARCHAR(50),
    адрес VARCHAR(100),
    телефон VARCHAR(20)
);


CREATE TABLE Склад (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_препарата INT,
    количество INT,
    FOREIGN KEY (id_препарата) REFERENCES Препараты(id)
);


CREATE TABLE Остатки_на_складе (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_препарата INT,
    количество INT,
    FOREIGN KEY (id_препарата) REFERENCES Препараты(id)
);


CREATE TABLE Покупки (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_клиента INT,
    id_препарата INT,
    дата_покупки DATE,
    FOREIGN KEY (id_клиента) REFERENCES Клиенты(id),
    FOREIGN KEY (id_препарата) REFERENCES Препараты(id)
);

