const recaps = document.querySelectorAll('.recap')


const observer = new IntersectionObserver((entries) =>{
    entries.forEach(entry => {
        if (entry.isIntersecting){
            entry.target.classList.add('slideIn');
           
        }else{
            entry.target.classList.remove('slideIn')
        }
    })
})
recaps.forEach((recap) =>{
    observer.observe(recap)
})


