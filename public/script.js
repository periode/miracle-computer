var voice = new p5.Speech('Google français');
voice.onEnd = nextWord;

var words;
var current_word = 0;

var timer = 1000;
var current_time;

var canSpeak = true;

function preload(){
	words = loadStrings('poem.txt');
}

function setup(){
	console.log(words);
	voice.listVoices();
	voice.setVoice('Tessa');
	voice.setPitch(0.3);
	current_time = millis();

	// voice.speak('This audio book is loosely based on their inspiring work, and is intended for mature audiences only. Chapter One. To continue listening, you can buy the whole book at w w w  dot a million random digits dot com.');
}

function draw(){
	if(words != null && millis() - current_time > timer && canSpeak && current_word < words.length)
		say();
}

function say(){
	voice.speak(words[current_word]);
	canSpeak = false;

	//available parameters:
	//voice
	//pitch
	//voice
}

function nextWord(){
	current_word++;
	current_time = millis();
	canSpeak = true;
}

function keyPressed(){
	if(key == ' '){
		canSpeak = !canSpeak;
	}
	console.log(canSpeak);
}
