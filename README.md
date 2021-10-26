## Usage

### Obtain Token
> curl -d '{"username":"XXX", "password":"XXX"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/auth/

### View Posts
> curl -H "Content-Type: application/json" -H 'Authorization: Token TOKEN_HERE' http://127.0.0.1:8000/api/posts/

### Add Post
> curl -d '{"body": "XXX"}' -H "Content-Type: application/json" -H 'Authorization: Token TOKEN_HERE' -X POST http://127.0.0.1:8000/api/posts/

### Update post
> curl -d '{"body": "XXX"}' -H "Content-Type: application/json" -H 'Authorization: Token TOKEN_HERE' -X PUT http://127.0.0.1:8000/api/posts/ID_HERE/

### Dellete post
> curl -H "Content-Type: application/json" -H 'Authorization: Token TOKEN_HERE' -X DELETE http://127.0.0.1:8000/api/posts/ID_HERE/

### Add like
> curl -H "Content-Type: application/json" -H 'Authorization: Token TOKEN_HERE' -X POST http://127.0.0.1:8000/api/posts/like/ID_HERE/