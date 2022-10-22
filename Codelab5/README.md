To access:
1. Meal Recommendation: http://localhost:80
<img width="914" alt="Screen Shot 2022-10-22 at 2 42 48 AM" src="https://user-images.githubusercontent.com/52935613/197332631-b22c2ec4-3877-492c-9af4-e452ab572733.png">

2. DB Admin: http://localhost:5050/
- username: admin@admin.com
- password: pass
<img width="922" alt="Screen Shot 2022-10-22 at 2 42 00 AM" src="https://user-images.githubusercontent.com/52935613/197332603-a0655790-9457-43ef-a624-28f5a4566040.png">

- After logging in, add a server.
<img width="625" alt="Screen Shot 2022-10-22 at 2 43 19 AM" src="https://user-images.githubusercontent.com/52935613/197332671-62567501-3d7e-41ed-8c10-9f9654e390e0.png">

- Enter "db" in the Name test field. Keep the rest default and select on connection tab.
- Enter db in the Host name/Address.
- Username: root_user and password: pwd
<img width="921" alt="Screen Shot 2022-10-22 at 2 44 02 AM" src="https://user-images.githubusercontent.com/52935613/197332704-fcea6c11-e96e-41ce-aa67-5c411b3603b4.png">
- Keep the rest of the fields default.

To insert an Entry into the database use the below SQL command.

- INSERT INTO Menu(foodName, Price) VALUES ('Aloo Gobi', 12.00);
