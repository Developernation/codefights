/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/

var scores, roundScores, activePlayer;

//index 0 is player 1, index 1 is player 2
scores = [0,0];
roundScore = 0;
activePlayer = 0; //0 will represent player 1, 1 will represent player 2
//----------------------------------------------------------------------
//---Hides the dice--------------   CSS value ||CSS property
document.querySelector('.dice').style.display = 'none'

//document.querySelector('#score-0').textContent = scores[0];
//document.querySelector('#score-1').textContent = scores[1];

//--------------------Set Displayed Values to 0-------------------------
//---you don't need a # when using getElementById-----------
document.getElementById('score-0').textContent = scores[0];
document.getElementById('score-1').textContent = scores[1];
document.getElementById('current-0').textContent = 0;
document.getElementById('current-1').textContent = 0;
//-----------------------------------------------------------


//----------------EVENTS---------------------------------------------------
//---get the button                         Type of event/regular function
//document.querySelector('.btn-roll').addEventListener('click',btn)

//---get button
document.querySelector('.btn-roll').addEventListener('click',function(){
    var dice,diceDOM;
    //1. Random number generated when some hone hits button
    dice = Math.floor(Math.random()*6) + 1;
    //2. Display result
    diceDOM = document.querySelector('.dice');
    diceDOM.style.display = 'block';
    diceDOM.src = 'dice-' + dice + '.png';
    //console.log(dice);
    //3. Update the round score if the rolled number was Not a 1
    if (dice !== 1){
        //Adds score
        roundScore += dice;
        document.querySelector('#current-' + activePlayer).textContent = roundScore;
        //document.getElementById('score-' + activePlayer).textContent = roundScore;

    }else {
        roundScore = 0;
        scores[activePlayer] = roundScore;

        //-----------------------This allows you to modify a CSS class------------------------------------------------------
        //document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');//removes panel dot and color
        //terinary operator

        //if active player is 0 | activePlayer should change to 1| else  activePlayer is 0;
        //activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
        //document.querySelector('.player-' + activePlayer + '-panel').classList.add('active');//adds panel dot and color
        //---------------------------------------------------------------------------------------------------------------------

        //-------------------Toggle-------------------------------

        document.getElementById('score-' + activePlayer).textContent = '0';
        switch_player();

    };
});
document.querySelector('.btn-hold').addEventListener('click',function(){
   //1)add current score to global scoe
    scores[activePlayer] += roundScore;
    roundScore = 0;
    document.getElementById('score-' + activePlayer).textContent = scores[activePlayer];
    switch_player();

    //2) Update user interface
    //3) Check if player won game

});




//--------------------------------------END MAIN PROGRAM------------------------------------------------------------



//-----------------FUNCTIONS---------------------------------

function switch_player() {
    document.querySelector('#current-' + activePlayer).textContent = '0';
    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');
    document.querySelector('.dice').style.display = 'none';

    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
}
