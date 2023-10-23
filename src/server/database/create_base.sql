CREATE TABLE manager (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phone FLOAT(20)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    job VARCHAR(50),
    phone FLOAT(20)
);

CREATE TABLE admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    phone FLOAT(20)
);


CREATE TABLE medicine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    dosage VARCHAR(20),
    type VARCHAR(50)
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    address VARCHAR(100),
    phone FLOAT(20)
);

CREATE TABLE supplies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_supply INTEGER,
    id_medicine INTEGER,
    quantity INTEGER,
    FOREIGN KEY (id_supply) REFERENCES suppliers(id),
    FOREIGN KEY (id_medicine) REFERENCES medicine(id)
);

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    address VARCHAR(100),
    phone FLOAT(20)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER,
    order_date DATE,
    FOREIGN KEY (id_client) REFERENCES clients(id)
);

CREATE TABLE sclad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicine INTEGER,
    quantity INTEGER,
    FOREIGN KEY (id_medicine) REFERENCES medicine(id)
);


CREATE TABLE ostatki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicine INTEGER,
    quantity INTEGER,
    FOREIGN KEY (id_medicine) REFERENCES medicine(id)
);


CREATE TABLE pokupky (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER,
    id_medicine INTEGER,
    pokupka_date DATE,
    FOREIGN KEY (id_client) REFERENCES clients(id),
    FOREIGN KEY (id_medicine) REFERENCES medicine(id)
);
