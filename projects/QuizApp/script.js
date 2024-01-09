const questions = [
    {
        question: "What is the result of a dot product?",
        answers: [
            { text: "A vector quantity", correct: false},
            { text: "A vector quantity, adding each component respectively", correct: false},
            { text: "A scaler quantity", correct: true},
            { text: "None of the above", correct: false},
        ]
    },
    {
        question: "Which of the following does green's therom apply to:",
        answers: [
            { text: "A conservative vector field, in an open region", correct: false},
            { text: "Any curve, C, that is closed and simply connected", correct: true},
            { text: "Any three dimension surface", correct: false},
            { text: "Any curve, C, that is closed and connected", correct: false},
        ]
    },
    {
        question: "Suppose a and b are nonzero, orthogonal vectors. Which of the following is true?",
        answers: [
            { text: "Projection b on to a equals projection a on to b", correct: true},
            { text: " a x b = b x a ", correct: false},
            { text: "I and II", correct: false},
            { text: "Neither I or II", correct: false},
        ]
    },


];

const questionElement = document.getElementById("question");
const answerButton = document.getElementById("answer-buttons")
const nextButton = document.getElementById("next-btn")

let currentQuestionIndex = 0;
let score = 0;

function startOfQuiz(){
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerHTML = "Next";
    showQuestion();
}

function showQuestion(){
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1; 
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButton.appendChild(button);
        if (answer.correct){
            button.dataset.correct = answer.correct;
        }
        button.addEventListener("click", selectAnswer);
    });
}

function resetState(){
    nextButton.style.display = "none";
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild);
    }
}

function selectAnswer(e){
    const selectedBtn = e.target;
    const isCorrect = selectedBtn.dataset.correct == "true";
    if (isCorrect){
        selectedBtn.classList.add("correct");
        score++;
    }else{
        selectedBtn.classList.add("incorrect")
    }
    Array.from(answerButton.children).forEach(button =>{
        if (button.dataset.correct == "true"){
            button.classList.add("correct");
        }
        button.disabled = true; 
    });
    nextButton.style.display = "block";
}

function handleNextButton(){
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length){
        showQuestion();
    }else{
        showScore();
    }
}

function showScore(){
    resetState();
    questionElement.innerHTML = `You scored ${score} out of ${questions.length}!`;
    nextButton.innerHTML = "Try Again!"
    nextButton.style.display = "block";
}

nextButton.addEventListener("click", ()=>{
    if(currentQuestionIndex < questions.length){
        handleNextButton();
    }else{
        startOfQuiz();
    }
})

startOfQuiz();