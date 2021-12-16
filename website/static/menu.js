let show = true 

const menuSection = document.querySelector('.menu__section')
const menuTogge = document.querySelector('.menu__toggle')

menuTogge.addEventListener('click', () => {

    // Roll off
    document.body.style.overflow = show ? 'hidden' : 'initial'

    menuSection.classList.toggle('on', show)
    show = !show;
})