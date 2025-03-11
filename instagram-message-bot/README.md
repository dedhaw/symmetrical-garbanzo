# Instgram message bot
This is an instagram auto response bot

## Hosting
This backend application will be hosted on AWS lambda, as cold starts will not effect the preformance of this tool.

<!-- Assuming Go High Level has a good database integration -->
The Database containing the conversation data will be stored on Go High Level.

## Integration
This will be used in a Go High Level workflow.

**Steps to set it up**

### 1. **Trigger the Workflow in Go High Level (Instagram Message)**

- **Trigger**: The workflow is triggered by receiving a new Instagram message. This will automatically capture information like:
  - The **Instagram handle** (username) of the customer.
  - The **message text** from the customer.

### 2. **Save the Message and Instagram Handle in Custom Fields**

- **Set Custom Fields**: 
  - In the workflow, use the **Set Custom Field** action to save both the Instagram handle and the message text into custom fields.
  - You’ll create two custom fields:
    - `Instagram_Handle` (to store the Instagram username)
    - `Customer_Message` (to store the message received from the customer)

  For example:
  - **Custom Field**: `Instagram_Handle` → **Value**: `{{contact.instagram_handle}}`
  - **Custom Field**: `Customer_Message` → **Value**: `{{contact.instagram_message}}`

### 3. **Send the Data to Your Backend API (FastAPI)**

- **Webhook Action**: Use the **Webhook Action** in Go High Level to send the data (Instagram handle and message) to your **FastAPI backend** for processing.
  - The webhook sends a `POST` request to your FastAPI endpoint (e.g., `https://your-api-url/process-message/`).
  - The body of the request will include the data from the custom fields:
  
    ```json
    {
      "username": "{{contact.Instagram_Handle}}",
      "message": "{{contact.Customer_Message}}"
    }
    ```

### 4. **Process the Data in Your Backend (FastAPI)**

- **Backend Logic**: Your FastAPI backend processes the incoming data. This might include:
  - Analyzing the customer’s message.
  - Generating a dynamic response.
  
- **Return the Response**: After processing, your FastAPI backend returns a response to Go High Level. The response could look like this:
  
  ```json
  {
    "response": "Thank you for your message! How can I help you today?"
  }