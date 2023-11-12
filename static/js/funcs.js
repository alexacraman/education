document.addEventListener('DOMContentLoaded', ()=>{
    const msg = document.querySelector('.messages')
    let btn = document.querySelector('.close');
    
    if (typeof(btn) != 'undefined' && btn != null){
    btn.addEventListener('click', ()=>{
        msg.classList.add('disappear')
        msg.classList.remove('appear')
        setTimeout(()=>{
            msg.style.display = 'none'
        },1000)
        
    })
    }
})

const navs = document.querySelectorAll('.navbar_items')

let toggleBtn = document.querySelector('.navbar_btn')

    toggleBtn.addEventListener('click', (e)=>{
        navs.forEach((nav) => {
        if(nav.classList.contains('rev_navbar_toggleShow')){
           nav.classList.remove('rev_navbar_toggleShow')
           nav.classList.add('navbar_toggleShow')   
       }
       else if(nav.classList.contains('navbar_toggleShow')) {
        nav.classList.add('rev_navbar_toggleShow')    
       }
    });
})



    const revBtn = document.getElementById('revBtn');
    if (revBtn != null){

   
    if (revBtn.style.display = 'none'){
        const showBtn = () => {
            revBtn.style.display = 'block' 
        };
    setTimeout(showBtn, 2000);
    }
    }

// document.addEventListener('scroll', ()=>{
//     var prxOne = document.getElementById('prxONe');
//     prxOne.style.top = (window.pageYOffset / 4) + "px"
// }, false)