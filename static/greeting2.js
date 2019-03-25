function pick_random(lst){
  var i = Math.floor(Math.random() * lst.length);
  return lst[i]
}

var greetings = [
  "You look great today.",
  "Ready to find your next apartment?",
  "Welcome back.",
  "We missed you.",
  "Your dream apartment awaits.",
  "That's a nice shirt!",
  "Wahoowa!",
  "Tony Bennet says hi.",
  "Where shall we look next?",
  "How have you been?",
  
]

var greeting2 = pick_random(greetings);
