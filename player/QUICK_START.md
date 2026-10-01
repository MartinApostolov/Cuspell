# Cuspell Quick Start

Cuspell is written as a **flat sentence**, not as a spell-program tree.

## The six things to learn first

1. **End every sentence with its mood.**  
   `.` states something, `?` asks, and `!` commands.

2. **Put the head first, then its arguments.**  
   `Move This Here!`

3. **Read arguments left to right.**  
   Their types determine which registered frame they fill.

4. **Write tightly bound local pieces together when useful.**  
   `LifeThis.` means the same local application as `Life This.`

5. **Cuspell never guesses an ambiguous meaning.**  
   If more than one distinct typed reading is possible, rewrite the sentence.

6. **Missing required information is an error, not an invitation to infer intent.**

## First examples

`MatterSelf.`  
Self is Matter.

`LifeThis?`  
Is This alive?

`Move This Here!`  
Move This to Here.

`EndLifeThis!`  
End the Life state of This.

`If LifeThis MoveThisHere!`  
If This is alive, move This Here.

`Sequence MoveSelfHere MoveSelfThere!`  
Move Self Here, then move Self There.

`Concurrent MoveSelfHere MoveYouThere!`  
Require those two movements concurrently.

You can use useful basic Cuspell without learning binders, collections, named roles, quotation, or advanced mathematics.
