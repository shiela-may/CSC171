hoofer(tony).
hoofer(shi-kuo).
hoofer(ellen).

hoofer(X):- skier(X) ; climber(X).
climber(X) :- not(likes(X,rain)).
skier(X) :- likes(X,snow).

likes(tony,rain).
likes(tony,snow).
likes(tony,Y) :- not(likes(ellen,Y)).
likes(ellen,Y) :- not(likes(tony,Y)).

start(X) :- hoofer(X),climber(X),not(skier(X)).