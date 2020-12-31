var facts=[
    "I have a boyfriend since highschool",
    "My Dog's name is Waffle",
    "I write Poems",
    "I grew up in Ashdod",
    "I LOVE COFFEE",
    "I love to practice Yoga",
    "I'm currently living in Be'er Sheva",
    "I have two young sisters",
    "I enjoy a good book",
];

function generateFact(){
    let len = facts.length;
    let rand = Math.floor(Math.random()*len);
    let currFact = document.getElementsByClassName("fact-factory")[0].innerHTML;
    document.getElementsByClassName("fact-factory")[0].innerHTML = facts[rand];
    facts.splice(rand,1);
    if (currFact.length > 0)
        facts.push(currFact);
}

function sayThankYou(){
    alert("Thank You, Adventurer for Contacting me :)");
}