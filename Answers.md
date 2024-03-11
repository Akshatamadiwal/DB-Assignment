Question 1:- Explain the relationship between the "Product" and "Product_Category" entities from the above diagram.

Answer:- The Relationship between the 'product' and 'product_category'entities is a "many-to-one relationship" because many products can belong to one product category.

1)Each product in the "product" entity is linked to one product category through the 'category_id' foreign key column.

2)Also,each product category in the "product_category" entity can have many products associated with it.


Question 2:- How could you ensure that each product in the "Product" table has a valid category assigned to it?

Answer:- To ensure that each product in the "Product" table has a valid category assigned to it, referential integrity is enforced through the use of a foreign key constraint which ensures that the value stored in the category_id column of the "Product" table must correspond to a valid primary key value in the "Product_Category" table.

To ensure that each product in product table has a valid category assigned to it we can do the following:-

1) When creating or altering  the "product" table defining a foreign key constraint on the "category_id" column that refers to the primary key('id') column of the "product_category" table.

2) Specifying ON DELETE and ON UPDATE Actions:- This will prevent the updation or deletion of a product if the specified "category_id" doesnot exist in the "product_Category" table.

Sql query:-
CREATE TABLE Product (
FOREIGN KEY (category_id) REFERENCES Product_Category(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
