

# PlantUML for UML designs


## Installation for Mac

```
brew install libtool
brew link libtool
brew install graphviz
brew link --overwrite graphviz
```
For more details on installation, click [here](https://plantuml.com/graphviz-dot)

## Sequence Diagram

![](sequence.png)
```
@startuml
Requester -> DataRequestTrackerApp : Bob raises a Request
Requester <- DataRequestTrackerApp : Email Notification with Request Details
DataRequestTrackerApp -> "SuperAdmin" as Admin : Email notification with Request Summary sent to Alice
Admin -> "Approver" : Assigns the request to Ted
DataRequestTrackerApp -> "Approver" : Email notification with Request Summary
"Approver" -> DataRequestTrackerApp : Ted responds to the Request from Bob
Requester <- DataRequestTrackerApp : Email Notification with Approver comments
Requester -> DataRequestTrackerApp :   Checks the Request details
@enduml
```

## Use Case Diagram
```
@startuml
left to right direction
actor Guest as g
actor "<<service>> authentication" as auth
actor "Identity Provider" as idp
actor "Credit Payment Service" as cps
actor "PayPal" as pp

package Online_Shopping_System {
  usecase "View Items" as UC1
  usecase "Make Purchase" as UC2
  usecase "Complete Checkout" as UC3
  usecase "Login" as UC4
}

UC2 -> UC1 : include
UC2 -> UC3 : include
g --> UC1
g --> UC2
g --> UC4
UC4 --> auth
UC1 --> auth
UC3 --> auth
UC1 --> idp
UC3 --> idp
UC3 --> cps
UC4 --> pp
@enduml
```
