
document.addEventListener('DOMContentLoaded', ()=>{

const dataPk = document.querySelector('#dataPk')
const dataId = dataPk.dataset.pk
const currentLoc = window.location.href



let originalRequest = new Request(currentLoc)
let newRequest = new Request(dataId, originalRequest);
console.log(originalRequest,newRequest.url)

const updateUrlWithPk = () =>{
    history.pushState({}, null, newRequest.url);
}


(function()
{
  if( window.localStorage )
  {
    if( !localStorage.getItem('firstLoad') )
    {
      localStorage['firstLoad'] = true;
      updateUrlWithPk()
      window.location.reload();
      return
    }  
    else
      localStorage.removeItem('firstLoad');
    return
  }
})();
})//dom





// const newUrl =  `${currentLoc}${dataId}`
// const newUrl = () =>{
//       redirect(dataId, 200)
// }
// let urlOne = new URL(dataId, window.location.href);
// console.log(urlOne.href)
    // fetch(dataId)
    // .then((response) =>{
    //     if(response.status === 200){
    //         // window.location.assign(response)
    //         console.log(response.url)
    //         return response.url
          
    //     }else{
    //     //    return window.location.assign(dataId)
    //       console.log(response.status)
    //     }
    // })
    // .then((data)=>{
    //    console.log(data)
      
    // })
    // .catch((err) =>{ 
    //     console.log(err)
    // })
