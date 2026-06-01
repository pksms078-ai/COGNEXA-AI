Markdown
# API Specification

Base URL

/api/v1

---

## Authentication

POST /auth/login

Request

{
  "email": "user@example.com",
  "password": "password"
}

Response

{
  "token": "jwt_token"
}

---

## Workflow Query

POST /workflow/query

Request

{
  "query": "Which projects are delayed?"
}

Response

{
  "result": [
    {
      "project": "Project A",
      "status": "Delayed"
    }
  ]
}

---

## Risk Assessment

GET /risk/summary

Response

{
  "high_risk": 3,
  "medium_risk": 5,
  "low_risk": 12
}

---

## Analytics

GET /analytics/dashboard

Response

{
  "efficiency": 82,
  "utilization": 74,
  "customer_satisfaction": 89
}

---

## Recommendations

GET /recommendations

Response

{
  "recommendation":
  "Prioritize workflow automation."
}
