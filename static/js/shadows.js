const shadowScroll = document.querySelectorAll('.shadowScroll');

const myObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        if(entry.isIntersecting){
            entry.target.classList.add('shadow-class')
        }else{
            entry.target.classList.remove('shadow-class')
        }
    })
})

shadowScroll.forEach((shadow) =>{
    myObserver.observe(shadow)
})