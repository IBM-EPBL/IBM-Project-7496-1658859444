function register()
{
    $.ajax({
        type: 'POST',
        url: '/register',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax-container").innerHTML=response; 
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
            document.getElementById("ajax-container").innerHTML=response; 
        }
    });
}
function dashboard()
{
    $.ajax({
        type: 'POST',
        url: '/dashboard',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}
function profile()
{
    $.ajax({
        type:'POST',
        url:'/profile',
        data:{},
        success: function(response)
        {
            document.getElementById('ajax').innerHTML = response;
        }
    })
}
function users()
{
    $.ajax({
        type:'POST',
        url:'/users',
        data:{},
        success: function(response)
        {
            document.getElementById('ajax').innerHTML = response;
        }
    })
}
function items()
{
    $.ajax({
        type:'POST',
        url:'/items',
        data:{},
        success: function(response)
        {
            document.getElementById('ajax').innerHTML = response;
        }
    })
}
function add_item()
{
    $.ajax({
        type:'POST',
        url:'/add_item',
        data:{},
        success: function(response)
        {
            document.getElementById('ajax').innerHTML = response;
        }
    })
}
function logout(){
    if(confirm('Are you sure you want to logout?'))
    {
        alertify.set('notifier','position','top-center');
        alertify.notify('You are logging out...', 'success', 3, function(){
            window.location.href='/logout';
        });
    }
}
window.onload = function() 
{ 
    $.ajax({
        type: 'POST',
        url: '/dashboard',
        data: {},
        success: function (response) 
        {
            document.getElementById("ajax").innerHTML=response; 
        }
    });
}

