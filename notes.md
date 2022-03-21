- website is just html, server gives you html file you open in browser
- how to print literal < > " characters in html
- including javascript in html
  - initially for stuff like input validation so that the server doesn't have to validate
- javascript very very powerful, 
  - can write changes to the webpage once the client loads it
  - request sensitive authenticated enpoint that reveals info
  - access local cookies/storage
  - send requests from same domain
  - webcam
  - mine bitcoin
  - etc.
- so being able to run js in another user's browser gives me this ability, and this is basically and why it's bad xss
  - xss is abusing the trust user has in the domain, b/c user thinks they're allowing bank.com to run js,
    but instead it's js that hacker provided

- reflected xss demo
- xss in different contexts
- Templates introduced in part to help prevent this, if used correctly the will properly output encode these various 
  dangerous characters
- in our webapps case, the template is 
- demo Jinja2 template with autoescapeing off, then with on
- serverside template injection abuses features within the templating engine (such as Jinja) in order to ultimately read files or run arbitrary code
- clientside ti?
