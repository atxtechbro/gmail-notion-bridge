# Gmail-Notion Bridge Core

## Cloud Deployment

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

```mermaid
flowchart LR
    Gmail -->|Label Changes| PubSub[Pub/Sub]
    PubSub -->|Event| Validator{Schema Check}
    Validator -->|Valid| Notion
    Validator -->|Invalid| DLQ[Dead Letter Queue]
```
