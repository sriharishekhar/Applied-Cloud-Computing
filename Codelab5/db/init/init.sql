CREATE TABLE IF NOT EXISTS Menu (
  meal_id SERIAL PRIMARY KEY,
  foodName TEXT NOT NULL,
  price REAL NOT NULL
);

INSERT INTO Menu(foodName, price) VALUES ('Chicken Tikka', 20.00);
INSERT INTO Menu(foodName, price) VALUES ('Fish Tikka', 19.00);
INSERT INTO Menu(foodName, price) VALUES ('Tandoori chicken', 15.00);
INSERT INTO Menu(foodName, price) VALUES ('Seekh Kebab', 17.00);
INSERT INTO Menu(foodName, price) VALUES ('Gulauti Kebab', 15.50);
INSERT INTO Menu(foodName, price) VALUES ('Butter Chicken', 10.00);
INSERT INTO Menu(foodName, price) VALUES ('Kadhai Chicken', 22.00);
INSERT INTO Menu(foodName, price) VALUES ('Laal Maas', 21.00);
INSERT INTO Menu(foodName, price) VALUES ('Paneer Butter Masala', 16.00);
INSERT INTO Menu(foodName, price) VALUES ('Amritsari Cholle', 10.00);
INSERT INTO Menu(foodName, price) VALUES ('Arhar ki Dal', 9.50);
INSERT INTO Menu(foodName, price) VALUES ('Rajma Chawal', 15.00);
INSERT INTO Menu(foodName, price) VALUES ('Malai Kofta', 14.00);
INSERT INTO Menu(foodName, price) VALUES ('Mutton Biryani', 24.00);
INSERT INTO Menu(foodName, price) VALUES ('Anda Burji', 6.50);
INSERT INTO Menu(foodName, price) VALUES ('Rasmalai', 15.00);