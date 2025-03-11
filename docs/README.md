# Budget App


## General information

### System description
Budget App is a application that is designed to empower users in managing their expenses and incomes. Main functionalities are: 
- **Account creation:** 
- **Manual data entry:** record income or expenses with summary, amount and transaction date
- **Automated sync:** connected to supported financial institutions to synchronization of income and expenses
- **Visualization:** Generate date-limited charts that provide analysis of income and expenses

### Business benefits
blabla

## Stakeholders
1. **End Users** - Individuals who will use the application to manage their personal finances, including tracking expenses and incomes.
2. **Developers** - Team responsible for creating this application 
3. **Investors** - People that invested their money in development of that application with in order to earn money in case of its success.

## Actors
Application for budget management doesn't require any administrators for user management. Individuals create and manege their accounts by themselves. Due to that, only two actors were distinguished.

**User** is a primary actor who interact with application. User has the following attributes:
- email
- password

**System** is hidden, internal actor that performs automated tasks within application. It has following attributes:
- task_id
- task_type
- status

## Objects

**Expense** - represents money that user spent on something and was registered in application by user or financial institution sync. It has following attributes:
- id - unique identifier
- summary - a brief description of the expense
- amount - the amount of money spent in transaction
- transaction date - the date when transaction occurred
- category id - reference to existing category (e.g.: food, subscriptions, transportation)
- user id - identifier of the user which registered the expense

**Income** - represents money that user received. It can be registered manually or sync from financial institution. It has following attributes:
- id - unique identifier
- summary - a brief description of the income
- amount - the amount of money received
- transaction date - the date when transaction occurred
- source - income source (person of institution that send money)
- user id - identifier of the user which received money

**Connection** - represents connection to financial institution API service. It's created by user and used to automatically synchronize expenses and incomes. It has following attributes:
- id - unique identifier
- institution name - name of the financial institution 
- api key - api key generated when user authorized connection to financial institution
- status - the current status of connection (active / inactive / error)
- last sync - the timestamp of the last successful synchronization
- user id - identifier of the user which created connection 

**Budget** - represents budget created by the user for the specified time period to manage their expenses within limit. It can be used in notification, if declared limit is exceeded. It has the following attributes:
- id - unique identifier
- amount - the maximum amount of money allocated for specified budget
- period - time period for budget (weekly / monthly / yearly)
- status - the current status (under / exceeded)
- user id - identifier of the user which created budget

**Category** - represents expense category. It has the following attributes:
- id
- name
- user id - identifier of the user which created category

**Notification** - represents a notification send to the user when expenses reach specified budget threshold. It has following attributes:
- id - unique identifier
- budget id - identifier of the budget
- threshold - % of the budget, when exceeded will trigger notification
- status - notification status (pending / send)
- user id - identifier of the user which created notification

## Context diagram

## Functional requirements

## Non-functional requirements