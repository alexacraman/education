window.addEventListener('DOMContentLoaded', ()=>{
    const dataUrl = window.location.href
    const quizBox = document.getElementById('quiz-box');
    const quizContainer = document.getElementById('quizContainer');
    options = {
        method: 'GET',
        origin: 'same-origin',
       
    }
    fetch(`${dataUrl}data`, options)
    .then(response => {
        return response.json()
    })
    .then(data =>{
        
        data.data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="my-6 block">
                       <b> ${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                    <div class="block my-4">
                        <label for="${question}" class="">${answer} </label>
                       <input type='radio' class='ans mx-6' id="${question}-${answer}" name="${question}" value="${answer}">
                       
                    </div>

                    `
                })
            }
        });

    })

    .catch(error =>{
        console.log(error)
    })

    const quizForm = document.getElementById('quiz-form'); 

    const sendData = () =>{
        const elements = [...document.getElementsByClassName('ans')]
        
        const data = {}
        elements.forEach(el=>{
            if(el.checked){
                data[el.name] = el.value
            }else{
                if(!data[el.name]){
                    data[el.name] = null
                }
            }
        })

    const csrftoken = Cookies.get('csrftoken');
    options ={
        method: 'POST',
        headers:{
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    }
    fetch(`${dataUrl}save/`, options)
    .then(response =>{
        return response.json()
    })
   .then(data=>{
        let results = data.results;
        quizForm.classList.add('hidden');
        quizContainer.innerHTML = `<p>${data.passed ? 'Congratulations' : "Not passed, please try again."} Your result is ${data.score.toFixed(2)}%</p>`
        if (data.passed == false){
            quizContainer.innerHTML += `
            <div class="flex justify-center">
            <a href="${dataUrl}"  class="btn m-2">Take test Again?</a>
            </div>`
        }else{
            quizContainer.innerHTML += `
            <div class="flex justify-center">
            <a href="/students/dashboard/"  class="btn m-2">Go to Dashboard</a>
            </div>`

        }
        results.forEach(res =>{
            const resDiv = document.createElement('div');
            for (const [question, resp] of Object.entries(res)){
                resDiv.innerHTML += question;
                const cls = ['max-w-sm', 'p-6' , 'mx-auto'];
                resDiv.classList.add(...cls);

                if (resp == 'not answered'){
                    resDiv.innerHTML += '<br> - not answered';
                    resDiv.classList.add('text-red-700');
                } else {
                    const answer = resp['answered'];
                    const correct = resp['correct_answer'];
                    
                    if (answer == correct){
                        resDiv.classList.add('text-green-600');
                        resDiv.innerHTML += `<br>Correct. You answered: ${answer}`;
                    } else {
                        resDiv.classList.add('text-red-700');
                        resDiv.innerHTML += `<br>Incorrect. You answered: ${answer}`;
                        resDiv.innerHTML += `<br>The correct answer: ${correct}`;
                    }
                }
             
            };
            quizContainer.append(resDiv);
        }); // forEach loop
   }) // .then
    .catch(error =>{
        console.log(error)
    })

    } //send data function
    quizForm.addEventListener('submit', e=>{
        e.preventDefault()
        sendData()
    })
})