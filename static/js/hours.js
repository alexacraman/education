document.addEventListener('DOMContentLoaded', ()=>{
  const sessionTime = document.querySelectorAll('#session_length')
  const learningTime = document.getElementById('session_time')
  const array = new Array()
  const sessLen = sessionTime.forEach((el) =>{
  array.push(parseInt(el.dataset.id))
  
 })
 
 let sum = 0;

  for (let i = 0; i < array.length; i++) {
      sum += array[i];
  }
  // console.log(sum);
  
  learningTime.innerHTML += `    <li class="border-8 bg-cream border-teal-200 rounded-full h-20 w-20 mx-auto text-center text-gray-600 shadow-2xl "id="pumpIt" >${sum} Hours</li>`
  
})