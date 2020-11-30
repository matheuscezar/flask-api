# Tests

Below codes show how use this API.

PS: If you want to test endpoints that need authentication, create your user first.



![](homer.gif)



## 1. Authentication

Url: URL_BASE/login

Method: POST

Example: 

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"mail":"xyz","password":"xyz"}' \
  http://URL_BASE/login
```

PS: If success, returns your token

## 2. User Registration

Url: URL_BASE/users

Method: POST

Example: 

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"John","mail":"test@test.net","password":"xyz"}' \
  http://URL_BASE/users
```

## 3. Get all users

Url: URL_BASE/users/

Method: GET

Example:

```
curl --location --request GET URL_BASE/users/ --header 'token: your_token'

```

## 4. Get user by id

Url: URL_BASE/users/[id_user]

Method: GET

Example:

```
curl --location --request GET URL_BASE/users/[id_user] --header 'token: your_token'
```

## 5. Update user by id

Url: URL_BASE/users/[id_user]

Method: PUT

Example:

```
curl --location --request PUT URL_BASE/users/[id_user] \
--header 'token: your_token' \
--header 'Content-Type: application/json' \
--data-raw '    {
        "mail": "test2@teste.net",
        "name": "Test 2 name"
    }'
```

## 6. Delete user by id

Url: URL_BASE/users/[id_user]

Method: DELETE

Example:

```
curl --location --request DELETE URL_BASE/users/[id_user] \
--header 'token: your_token' 
```

## 7. Get all phones

Url: URL_BASE/phones/

Method: GET

Example:

```
curl --location --request GET URL_BASE/phones/ \
--header 'token: your_token' 
```

## 8. Get phone by id

Url: URL_BASE/phones/[id_phone]

Method: GET

Example:

```
curl --location --request GET URL_BASE/phones/[id_phone] \
--header 'token: your_token' 
```

## 9. Insert phone

Url: URL_BASE/phones

Method: POST

Example:

```
curl --location --request POST URL_BASE/phones \
--header 'token: your_token' \
--header 'Content-Type: application/json' \
--data-raw '{
  "value": "+55 84 91234-4321",
  "monthyPrice": "0.03",
  "setupPrice": "3.40",
  "currency": "U$"
}'
```

## 10. Update phone by id

Url: URL_BASE/phones/[id_phone]

Method: PUT

Example:

```
curl --location --request PUT localhost:5000/phones/[id_phone] \
--header 'token: your_token' \
--data-raw '{
  "value": "+55 84 81234-4321",
  "monthyPrice": "10",
  "setupPrice": "100",
  "currency": "$"
}'
```

## 11. Delete phone by id

Url: URL_BASE/phones/[id_phone]

Method: DELETE

Example:

```
curl --location --request DELETE URL_BASE/phones/[id_phone] \
--header 'token: your_token'
```

