# Throttling

Throttling is a technique used in APIs to limit the number of requests a client can make within a specified time period. This ensures that the server is not overloaded and that all users have fair access to resources. It's similar to traffic control on highways—there's a limit to how many cars (requests) can enter at any given time.

- **Anonymous Throttling:** Limits requests from unauthenticated users (e.g., users not logged in).

- **User Throttling:** Limits requests based on authenticated users, ensuring each individual user has their own rate limit.

- **Scoped Throttling:** Limits requests for specific parts of the API. For example, the API should allow 1000 requests per day for general usage, but only 20 requests per day for uploading files. You define a throttle_scope in your view and link it to a key like 'burst', 'uploads', etc.

- **Custom Throttling:** You can even create custom throttles for more complex scenarios. For instance, you might want to randomly throttle 1 in every 10 requests.

When a client exceeds the allowed rate limit, the API will return an HTTP response with the status code 429 Too Many Requests. The response might also include a `Retry-After` header that tells the client how long to wait before making another request.

Throttling relies on Django's cache system to keep track of how many requests have been made by a user or an IP address. The default caching backend (e.g., `LocMemCache`) might be fine for small apps, but for large apps, you might want to use a more scalable solution like `Redis`.

Throttling is not a security feature. It's not designed to prevent attacks like brute force or denial-of-service (DoS) attacks. It can be imperfect under high concurrency due to race conditions, so custom throttling might be necessary for certain applications.

## Demo Project

```bash
django-admin startproject drf_throttle_demo .
python manage.py startapp api

python manage.py migrate
python manage.py runserver
```

