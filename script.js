document.querySelectorAll('p').forEach((el, idx) => {
    el.addEventListener('click', () => {
        const child = el.appendChild(document.createElement('p'))
        child.innerHTML = 'BOMBA'
    })
    // console.log(el.innerHTML)
})



// console.log(document.querySelector('p'))
// alert('bomba')