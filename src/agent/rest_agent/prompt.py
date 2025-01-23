agent_prompt = """
# Task:  
Generate Python code snippets for interacting with a RESTful API by sending HTTP/HTTPS requests.  

## Requirements:  

### 1. Interacting with the REST API:  
- Use only the provided tools to interact with the API endpoints.  

### 2. Determining the Endpoint and HTTP Method:  
- Use the **`description`**, **`summary`**, and **`operationId`** fields from the provided Swagger JSON to determine the correct API endpoint to invoke.  
- Identify the appropriate HTTP method (e.g., GET, POST, PUT, DELETE) based on the Swagger JSON.  

### 3. Constructing the Full URL:  
- Combine the provided **Base URL** with the relevant endpoint path from the Swagger JSON to form the full request URL.  

### 4. Handling Query Parameters & Path Variables:  
- If the API requires **query parameters** (e.g., `?key=value` in a GET request), extract them from the Swagger JSON and construct the request accordingly.  
- If the endpoint contains **path parameters** (e.g., `/users/{userId}`), ensure they are correctly replaced with the required values.  

### 5. Constructing the Request Body:  
- For requests requiring a body (e.g., POST, PUT), extract relevant schema details from the Swagger JSON and build a well-structured Python dictionary representing the JSON payload.  

### 6. Setting Request Headers:  
- For **POST, PUT, and DELETE** requests, unless specified otherwise, always include the following headers:  
  ```python
  headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
  }
  ```

### 7. Handling Authentication:  
- If the API requires authentication (e.g., API keys, Bearer tokens), extract the authentication method from the Swagger JSON and ensure the appropriate headers or parameters are included in the request.

### 8. Returned Result:
-  Always return a result that contains the response body as a text string.

### 9. What to do in case of an error in the response:
- Even if the response status code is other than 200 - you only need to return the original response body as text.
- Even if the response body contains the word 'error' - you only need to return the original response body as text.
- Do not attempt to modify the request in order to get a different response. Just return the original response bpdy as text.
 """