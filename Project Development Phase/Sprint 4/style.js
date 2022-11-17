document.addEventListener("DOMContentLoaded", function(event) {
    
    const showNavbar = (navId, bodyId, headerId) =>{
    const nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(nav && bodypd && headerpd)
    {
        nav.addEventListener('mouseover', ()=>{
            // show navbar
            nav.classList.add('show')
            // add padding to body
            bodypd.classList.add('body-pd')
            // add padding to header
            headerpd.classList.add('body-pd')
        })
        nav.addEventListener('mouseleave', ()=>{
            // remove navbar
            nav.classList.remove('show')
            // remove padding to body
            bodypd.classList.remove('body-pd')
            // remove padding to header
            headerpd.classList.remove('body-pd')
        })
    }
    }

    showNavbar('nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')

    function colorLink(){
        if(linkColor)
        {
            linkColor.forEach(l=> l.classList.remove('active'))
            this.classList.add('active')
        }
    }

    linkColor.forEach(l=> l.addEventListener('click', colorLink))
});