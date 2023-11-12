function toggleModal() {
    document.getElementById('modal').classList.toggle('hidden')
    }
document.addEventListener('DOMContentLoaded', ()=>{
const modalBtns     = [...document.getElementsByClassName('modal-button')];
const modalBody     = document.getElementById('model-body-confirm');
const startBtn      = document.getElementById('start-button');
const url           = window.location.href


modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const slug          = modalBtn.getAttribute('data-slug')
    const name          = modalBtn.getAttribute('data-quiz')
    const numQuestions  = modalBtn.getAttribute('data-questions')
    const difficulty    = modalBtn.getAttribute('data-difficulty')
    const scoreToPass   = modalBtn.getAttribute('data-pass')
    const time          = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
        <div class="mb-3">Are you ready to begin?<b> ${name} </b></div>
        <ul>
            <li>Difficulty: ${difficulty}</li>
            <li>Number of Questions: ${numQuestions}</li>
            <li>Score to pass: ${scoreToPass}%</li>
            
           
        </ul>
    `
startBtn.addEventListener('click', ()=>{
window.location.href = url + slug
})
}))


})
