## API Endpoints
Export postman collection: [https://github.com/varshamohan08/e_com_system/blob/main/e_com_system.postman_collection.json](https://github.com/varshamohan08/e_com_system/blob/main/e_com_system.postman_collection.json)
### User Authentication
#### Login

POST /api/login/

Request Body:

```
{
  "username": "your_username",
  "password": "your_password"
}
```
Response:

```
{
  "success": true,
  "details": {
    "email": "user@example.com",
    "username": "your_username",
    "access_token": "your_access_token"
  }
}
```
#### Logout

GET /api/logout/

Response:

```
{
  "success": true,
  "details": "Logged out successfully"
}
```
### Categories
#### List Categories

GET /api/categories/
Response:

```
{
  "success": true,
  "details": [
    {
      "id": 1,
      "name": "Category 1",
      "description": "Description of category 1",
      "created_by": "user_id",
      "created_date": "01-01-2024 12:00 PM",
      "updated_by": "user_id",
      "updated_date": "01-01-2024 12:00 PM"
    }
  ]
}
```
#### Create Category

POST /api/categories/

Request Body:

```
{
  "name": "New Category",
  "description": "Description of new category"
}
```

Response:

```
{
  "success": true,
  "details": {
    "id": 2,
    "name": "New Category",
    "description": "Description of new category",
    ...
  }
}
```

#### Update Category

PUT /api/categories/{category_id}/

Request Body: (Any field can be updated)

```
{
  "name": "Updated Category Name"
}
```

Response:

```
{
  "success": true,
  "details": {
    ...
  }
}
```

#### Delete Category

DELETE /api/categories/{category_id}/
Response:

```
{
  "success": true,
  "details": "Deleted Successfully"
}
```
### Products
#### List Products

GET /api/products/

- All products: /api/products/
- Filter by category: /api/products?category=<category_id>/
- Pagination: /api/products?&page=<page_number>
- Pagination with custom number of records in page: /api/products?count=<count_of_records>&page=<page_number>

Response:

```
{
  "success": true,
  "details": [
    {
      "id": 1,
      "name": "Product 1",
      "description": "Description of product 1",
      "price": 100.0,
      ...
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_products": 10
  }
}
```

Create Product

POST /api/products/
Request Body:

```
{
  "name": "New Product",
  "description": "Description of new product",
  "price": 200.0,
  "category": 1
}
```

Response:

```
{
  "success": true,
  "details": {
    ...
  }
}
```

#### Update Product

PUT /api/products/{product_id}/
Request Body:

```
{
  "name": "Updated Product Name",
  "price": 250.0
}
```

Response:

```
{
  "success": true,
  "details": {
    ...
  }
}
```

Delete Product

DELETE /api/products/{product_id}/

Response:

```
{
  "success": true,
  "details": "Deleted Successfully"
}
```
