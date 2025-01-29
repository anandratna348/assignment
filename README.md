## **Project Overview**  
This project provides analytics and insights for Telegram group activity using a Flask-based API. The system processes and analyzes group, member, and message data to generate valuable insights for admins and users. The project also includes a Dockerized environment for easy deployment.  

## **Folder Structure**  
```
├── logs/
│   ├── app.log
│   ├── error.log
├── app.py
├── config.py
├── code_file.py  # Contains analytics implementation
├── analytics_ideas.py  # Defines analytics descriptions
├── Dockerfile
├── README.md
├── requirements.txt
```

## **How to Run the Project**  

### **1. Clone the Repository**  
```
git clone <repository_link>
cd telegram-group-analytics
```

### **2. Set Up Virtual Environment (Optional but Recommended)**  
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**  
```
pip install -r requirements.txt
```

### **4. Run the Flask Application**  
```
python app.py
```
Once the server is running, access the API at:  
`http://127.0.0.1:5000`

## **Docker Setup**  

### **1. Build the Docker Image**  
```
docker build -t telegram-analytics .
```

### **2. Run the Container**  
```
docker run -p 5000:5000 telegram-analytics
```

## **Available API Endpoints**  

| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/`           | GET    | Home endpoint, returns a welcome message. |
| `/analytics`  | GET    | Fetches a list of 20 analytics ideas. |
| `/dashboard`  | GET    | Retrieves analytics for admin dashboard. |

## **20 Analytics Implemented**  
The system provides the following analytics based on Telegram group activity:  

1. **Daily Messages Sent** - Tracks the number of messages sent per day.  
2. **Group Member Growth** - Monitors the growth of group members.  
3. **Top Active Groups** - Identifies the most active groups.  
4. **Messages Per Member** - Calculates the average messages per member.  
5. **Admin-to-Member Ratio** - Ensures effective group management.  
6. **Bot Usage Analysis** - Analyzes bot participation trends.  
7. **Pinned Message Trends** - Tracks how often messages are pinned.  
8. **Member Retention Rate** - Measures member retention over time.  
9. **Daily Join and Leave Rates** - Monitors membership fluctuation.  
10. **Hashtag Usage Frequency** - Analyzes trending topics.  
11. **Message Types Distribution** - Tracks the types of messages sent.  
12. **Message Replies Analysis** - Identifies engagement levels.  
13. **Top Contributors** - Highlights the most active members.  
14. **Inactive Members Count** - Detects inactive users.  
15. **Bot-to-Human Ratio** - Maintains a balanced community.  
16. **Group Visibility Trends** - Monitors changes in group privacy settings.  
17. **Message Forwarding Trends** - Identifies frequently forwarded messages.  
18. **URL Sharing Frequency** - Tracks the presence of external links.  
19. **Daily Active Members** - Measures daily user engagement.  
20. **Average Message Views** - Calculates message reach.  

## **Logging**  
Logs are stored in the `logs/` directory and capture application activity, including:  
- `app.log`: General application logs.  
- `error.log`: Captures errors encountered during execution.  
 
