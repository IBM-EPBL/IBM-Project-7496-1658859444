function signup()
{
    $.ajax({
        type: 'POST',
        url: '/signup',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}
function about()
{
    $.ajax({
        type: 'POST',
        url: '/about',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}
function login()
{
    $.ajax({
        type: 'POST',
        url: '/login',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}
function home()
{
    $.ajax({
        type: 'POST',
        url: '/home',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}
window.onload = function() 
{ 
    $.ajax({
        type: 'POST',
        url: '/home',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
};