# User Stories And Story Points

_“Some people say, “Give the customers what they want.” But that’s not my approach. Our job is to figure out what they’re going to want before they do. I think Henry Ford once said, “If I’d asked customers what they wanted, they would have told me, ‘A faster horse!’” People don’t know what they want until you show it to them._ - Steve Jobs

Writing the user stories and estimating the story point can be quite tedious. In fact, it's also considered among the most difficult–if not the most difficult–aspects of software development [[1](https://www.atlassian.com/agile/project-management/estimation)]. Let's look at some questions I had during my agile exploration.

|Table of Contents |
|------------|
|[Q1. What are User Stories?](https://github.com/blessinvarkey/musings/blob/main/posts/Scrum/15-07-2021-user-stories-and-story-points.md#q1-what-are-user-stories)    |
|[Q2. How do we write a user story?](https://github.com/blessinvarkey/musings/blob/main/posts/Scrum/15-07-2021-user-stories-and-story-points.md#q2-how-do-we-write-a-user-story)|
|[Q3. How many user stories should be selected per sprint?](https://github.com/blessinvarkey/musings/blob/main/posts/Scrum/15-07-2021-user-stories-and-story-points.md#q3-how-many-user-stories-should-be-selected-per-sprint)|
|[Q4. How do we calculate the story points?](https://github.com/blessinvarkey/musings/blob/main/posts/Scrum/15-07-2021-user-stories-and-story-points.md#q4-how-do-we-calculate-the-story-points)|


### Q1. What are User Stories?

A user story describes functionality that will be valuable to either a user or purchaser of a system or software. User stories are composed of three aspects:   
- a written description of the story used for planning and as a reminder.  
- conversations about the story that serve to flesh out the details of the story.  
- tests that convey and document details and that can be used to determine when a story is complete.  

Spend time understanding a customer's habit, belief and problems rather than asking what they want [[2](https://productcoalition.com/dont-ask-users-what-they-want-8a842bce274b)]. To avoid the customer saying _"You built what I asked for, but its not what I need"_.  

Stories are easier to remember. 
User stories are an example of a participatory design. [[3](https://www.youtube.com/watch?v=6q5-cVeNjCE)] 

### Q2. How do we write a user story?

For writing a good user story, Roman Pichler suggests 10 tips on his [blog](https://www.romanpichler.com/blog/10-tips-writing-good-user-stories/):
1. Put Users First: a user story describes how a customer or user employs the product; it is told from the user’s perspective
2. Use Personas to Discover the Right Stories: Adding name, a picture with relevant characteristics, behaviours, and attitudes; and a goal.
3. Create stories collaboratively: The product owner and the team should discuss the stories together.
4. Keep your Stories Simple and Concise: Check the Rachel Davies format.
5. Start with Epics: a placeholder for more detailed stories
6. Refine the Stories until They are Ready: Break the Epics till the stories are ready
7. Add Acceptance Criteria: They allow you to describe the conditions that have to be fulfilled so that the story is done.*
8. Use Paper Cards: First, paper cards are cheap and easy to use. Second, they facilitate collaboration: Every one can take a card and jot down an idea. Third, cards can be easily grouped on the table or wall to check for consistency and completeness and to visualise dependencies.
9. Keep your Stories Visible and Accessible.    
10. Don’t Solely Rely on User Stories

*The definition of done is common to all your work but acceptance criteria are specific to individual pieces of work.

### Rachel Davies format
User stories are written in the following format: As a < __user role__ >, I < __want/need/can/etc__ > < __goal__ > so that < __reason__ >. This template originated with agile coach Rachel Davies at an English company, Connextra, in the early 2000s. It has since become a recognized standard for expressing user stories.

Examples of user stories. 
- As a user, I want to reserve a hotel room
- As a user, I want to cancel a reservation
- As a premium user, I can cancel a reservation at the last minute
- As a non-premium user, I can cancel 24 hours before the trip.  
- As a frequent flyer, I want to rebook a past trip so that I can save time booking trips I take often

Visit this [link](https://www.mountaingoatsoftware.com/uploads/documents/example-user-stories.pdf) to view more than 200 examples of user stories.

Here's a user story card sample by [productplan.com](https://www.productplan.com)

<img src = "https://www.productplan.com/uploads/2019/01/user-story-1024x536.png" width= 600>

### Q3. How many user stories should be selected per sprint?

- 5 to 15 user stories for a 2-4 week sprint can be seen as a general trend, provided no user story takes more than 3 days. [[4](https://www.leadingagile.com/2015/05/how-many-user-stories-per-sprint-rules-of-thumb/)] 
- From Mike Cohn's blog: _"One possible solution to this common problem is that these teams are doing too many product backlog items per sprint. Based on data I analyzed on successfully finished sprints, I determined that a team should average around 1 to 1-1/2 user stories (product backlog items of any sort, really) per person per sprint. So, a six-person team should get somewhere around 6-9 user stories done per sprint."_ [[5](https://www.mountaingoatsoftware.com/blog/should-the-daily-standup-be-person-by-person-or-story-by-story)]



### Q4. How do we calculate the story points?

Story points are the estimates of effort as influenced by the amount of work, complexity, risk and uncertainity. Estimating the story point in a new project while implementing a scrum/agile methodology can be challenging. Story points are intended to make estimating easier by comparing the effort it will take for one user story, relative to the other user stories in the product backlog. 

The following estimated time per story point is taken from [this video](https://www.youtube.com/watch?v=NrHpXvDXVrw) by Dan Chuparkoff. It is quite easy to implement, however it is not the standard.  

| Time  | Story point  |
|---|---|
| 30 minutes |1 |
| 1 hour | 2  |
| 2 hours | 4  |
| 4 hours | 8  |
| 1 day  | 16  |
| 2 days | 32  |
| 3 days | 48  |


Another way to assign story points is by taking the shirt size example. Like the size of a shirt S, M, L, XL, XXL, a story that is assigned 2 story points (XL) should be twice as much as a story that is assigned 1(L) story point. It should also be two-thirds of a story that is estimated 3 (XXL) story points.

## Reccomended Reading:
1. [10 Tips Writing Good User Stories](https://www.romanpichler.com/blog/10-tips-writing-good-user-stories/)
2. [Beyond Coding](https://agilecoach.typepad.com/agile-coaching/)

[↑ Back to top](https://github.com/blessinvarkey/musings/blob/main/posts/Scrum/15-07-2021-user-stories-and-story-points.md)
